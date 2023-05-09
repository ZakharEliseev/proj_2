from datetime import datetime
from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm, EditProfile, EditProfilePasswd
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, UserPasswords
from flask import request
from urllib.parse import urlsplit

list_endpoints = [
    "main_index",
    "index",
    "login",
    "logout",
    "register",
    "edit_profile",
    "user",
    "main_admins",
    "administrators",
    "experts",
    "bak",
    "it",
    "admins",
    "baks",
    "its",
]
for i in list_endpoints:
    if i in app.view_functions:
        del app.view_functions[i]


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route("/")
@app.route("/index", endpoint="index")
@login_required
def main_index():
    return render_template("index.html")


@app.route("/admins", endpoint="admins")
@login_required
def main_admins():
    return render_template("administrators.html")


@app.route("/experts", endpoint="experts")
@login_required
def main_experts():
    return render_template("experts.html")


@app.route("/baks", endpoint="baks")
@login_required
def main_baks():
    return render_template("bak.html")


@app.route("/its", endpoint="its")
@login_required
def main_its():
    return render_template("it.html")


@app.route("/login", endpoint="login", methods=["GET", "POST"])
def main():
    if current_user.is_authenticated:
        return render_template(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Неверный логин или пароль!")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            date_of_birth=form.date_of_birth.data,
            phone_number=form.phone_number.data,
            fio=form.fio.data,
            position=form.position.data,
        )
        user.set_password(form.password.data)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        flash("Поздравляю! Вы зарегестрированы!")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template("user.html", user=user)


@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfile()
    form_passwd = EditProfilePasswd()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        current_user.position = form.position.data
        db.session.query(UserPasswords).filter_by(
            UserPasswords.user_id == current_user.id
        ).update({"password_ais": 123})
        db.session.commit()
        flash("Изменения сохранены")
        return redirect(url_for("user", username=current_user.username))
    elif request.method == "GET":
        current_user.email = current_user.email
        current_user.phone_number = current_user.phone_number
        current_user.position = current_user.position
    return render_template("edit_profile.html", form=form, form_passwd=form_passwd)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
