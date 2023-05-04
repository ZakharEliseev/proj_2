from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from flask import request
from urllib.parse import urlsplit



list_endpoints = ['main_index', 'index', 'login', 'logout', 'register', 'edit_profile', 'user', 'main_admins',
                  'administrators', 'experts', 'bak', 'it', 'admins', 'baks', 'its']
for i in list_endpoints:
    if i in app.view_functions:
        del app.view_functions[i]


@app.route('/')
@app.route('/index', endpoint='index')
@login_required
def main_index():
    return render_template('index.html')


@app.route('/admins', endpoint='admins')
@login_required
def main_admins():
    return render_template('administrators.html')


@app.route('/experts', endpoint='experts')
@login_required
def main_experts():
    return render_template('experts.html')


@app.route('/baks', endpoint='baks')
@login_required
def main_baks():
    return render_template('bak.html')


@app.route('/its', endpoint='its')
@login_required
def main_its():
    return render_template('it.html')


@app.route('/login', endpoint='login', methods=['GET', 'POST'])
def main():
    if current_user.is_authenticated:
        return render_template(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверный логин или пароль!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        flash('Поздравляю! Вы зарегестрированы!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
