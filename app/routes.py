from tqdm import tqdm
import os
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from app import app, db
from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    send_file,
    abort,
    request,
    session,
    g,
)
from app.forms import (
    LoginForm,
    RegistrationForm,
    EditProfile,
    EditProfilePasswd,
    UploadFormTIFF,
    UploadFormPDF,
)
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, UserPasswords
from flask import request
from urllib.parse import urlsplit
from io import BytesIO
from PIL import Image

app.config["UPLOAD_FOLDER"] = "uploads"
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
    "edit_passwords",
    "compressed_files_tiff",
    "compressed_pdf",
    "resize_pdf",
    "compressed_files_pdf",
]
for i in list_endpoints:
    if i in app.view_functions:
        del app.view_functions[i]


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        session.permanent = True
        g.user = current_user


@app.route("/")
@app.route("/index", endpoint="index")
@login_required
def main_index():
    session.permanent = True
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
def login():
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
        new_passwords = UserPasswords(
            password_ais="задайте пароль!",
            password_pvd="задайте пароль!",
            password_enter="задайте пароль!",
            password_mail="задайте пароль!",
            password_home="задайте пароль!",
            password_delo="задайте пароль!",
            user_pswd=user,
        )
        with app.app_context():
            db.session.add(user)
            db.session.add(new_passwords)
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
    form = EditProfile(current_user.username)
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        current_user.position = form.position.data
        db.session.commit()
        flash("Изменения сохранены")
        return redirect(url_for("user", username=current_user.username))
    elif request.method == "GET":
        form.email.data = current_user.email
        form.phone_number.data = current_user.phone_number
        form.position.data = current_user.position
    return render_template("edit_profile.html", form=form)


@app.route("/edit_passwords/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit_passwords(user_id):
    form_passwd = EditProfilePasswd()
    user = User.query.get_or_404(user_id)
    passwords = user.passwords.first()
    if form_passwd.validate_on_submit():
        UserPasswords.query.filter(UserPasswords.user_id == current_user.id).update(
            {
                UserPasswords.password_ais: form_passwd.password_ais.data,
                UserPasswords.password_pvd: form_passwd.password_pvd.data,
                UserPasswords.password_enter: form_passwd.password_enter.data,
                UserPasswords.password_mail: form_passwd.password_mail.data,
                UserPasswords.password_home: form_passwd.password_home.data,
                UserPasswords.password_delo: form_passwd.password_delo.data,
            }
        )
        db.session.commit()
        flash("Изменения сохранены")
        return redirect(url_for("user", username=current_user.username))
    elif request.method == "GET":
        form_passwd.password_ais.data = passwords.password_ais
        form_passwd.password_pvd.data = passwords.password_pvd
        form_passwd.password_enter.data = passwords.password_enter
        form_passwd.password_mail.data = passwords.password_mail
        form_passwd.password_home.data = passwords.password_home
        form_passwd.password_delo.data = passwords.password_delo
    return render_template("edit_passwords.html", form_passwd=form_passwd, user=user)


def resize_tiff(image_file, percent):
    with Image.open(image_file) as img:
        width, height = img.size
        # Делим ширину полученную из формы на 100
        new_width = int(width * (percent / 100))
        # Делим высоту полученную из формы на 100
        new_height = int(height * (percent / 100))
        resized_img = img.resize((new_width, new_height))
        buffer = BytesIO()  # Сохраняем в память
        resized_img.save(buffer, format="TIFF")
        buffer.seek(0)
    return buffer


@app.route("/compressed_files_tiff", methods=["GET", "POST"])
@login_required
def compressed_files_tiff():
    form = UploadFormTIFF()
    if form.validate_on_submit():
        file = form.file.data  # получение файла из формы
        percent = form.reduction.data  # получение процента из формы
        buffer = resize_tiff(file, percent)
        return send_file(
            buffer,
            as_attachment=True,
            mimetype="image/tiff",
            download_name=form.file.data.filename,
        )
    return render_template("compressed_files_tiff.html", form=form)


def compress_pdf(input_file, output_file, resolution):
    # Конвертируем PDF в изображения
    images = convert_from_path(input_file, dpi=resolution)
    # Создаем папку для временных изображений
    temp_dir = "temp_images"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir, exist_ok=True)

    out_images = []
    for i, image in tqdm(
        enumerate(images), total=len(images), desc="Compressing images"
    ):
        # Уменьшаем разрешение изображения
        reduced_image = image.resize(
            (int(image.width * resolution / 72), int(image.height * resolution / 72))
        )
        out_images.append(reduced_image)

        # Сохраняем временное изображение
        temp_path = os.path.join(temp_dir, f"temp_{i}.jpg")
        reduced_image.save(temp_path)

    # Соединяем изображения в PDF
    out_images[0].save(output_file, save_all=True, append_images=out_images[1:])

    # Удаляем временные изображения
    for temp_image in os.listdir(temp_dir):
        temp_image_path = os.path.join(temp_dir, temp_image)
        os.remove(temp_image_path)

    os.rmdir(temp_dir)


@app.route("/compressed_files_pdf", methods=["GET", "POST"])
@login_required
def compressed_files_pdf():
    form = UploadFormPDF()
    if request.method == "POST" and form.validate_on_submit():
        pdf_file = form.file.data
        # reduction_percentage = form.reduction.data
        resolution = form.resolution.data  # Установите желаемое разрешение здесь

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf_file.filename)
        pdf_file.save(file_path)

        pdf_reader = PdfReader(file_path)
        pdf_writer = PdfWriter()

        for page in tqdm(pdf_reader.pages, desc="Compressing pages"):
            page.compress_content_streams()
            pdf_writer.add_page(page)

        reduced_path = os.path.join(
            app.config["UPLOAD_FOLDER"], "сжато-" + pdf_file.filename
        )

        # Вызываем функцию compress_pdf
        compress_pdf(file_path, reduced_path, resolution)

        with open(reduced_path, "rb") as f:
            data = BytesIO(f.read())
        data.seek(0)
        return send_file(
            data,
            as_attachment=True,
            download_name="сжато-" + pdf_file.filename,
            mimetype="application/pdf",
        )

    return render_template("compressed_files_pdf.html", form=form)
    return render_template("edit_passwords.html", form_passwd=form_passwd, user=user)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
