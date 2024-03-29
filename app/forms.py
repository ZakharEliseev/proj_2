from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import (
    PasswordField,
    BooleanField,
    StringField,
    SubmitField,
    DateField,
    FileField,
    IntegerField,
)
from wtforms.validators import (
    ValidationError,
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
)
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(
        "Имя пользователя",
        validators=[DataRequired(message="Введите свое имя пользователя")],
    )
    password = PasswordField(
        "Пароль", validators=[DataRequired(message="Введите свой пароль")]
    )
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class RegistrationForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    fio = StringField("ФИО", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password2 = PasswordField(
        "Повторите пароль", validators=[DataRequired(), EqualTo("password")]
    )
    phone_number = StringField(
        "Телефон", validators=[DataRequired(),],)
    date_of_birth = DateField("Дата рождения", validators=[DataRequired()], format="%d.%m.%Y")
    position = StringField("Должность", validators=[DataRequired()])
    submit = SubmitField("Регистрация")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Пожалуйста используйте другое имя пользователя")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Пожалуйста используйте другой email")


class EditProfile(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Номер телефона", validators=[DataRequired()])
    position = StringField("Должность", validators=[DataRequired()])
    submit = SubmitField("Сохранить")

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(
                    "Пожалуйста, используйте другое имя пользователя."
                )


class EditProfilePasswd(FlaskForm):
    password_ais = StringField("Пароль АИС",
                               validators=[Length(min=6, max=20)])
    password_pvd = StringField("Пароль ПВД",
                               validators=[Length(min=6, max=20)])
    password_enter = StringField("Пароль СУО",
                                 validators=[Length(min=6, max=20)])
    password_mail = StringField("Пароль почта",
                                validators=[Length(min=6, max=20)])
    password_home = StringField(
        "Пароль от этого сайта", validators=[Length(min=6, max=20)])
    password_delo = StringField("Пароль СЭД",
                                validators=[Length(min=6, max=20)])
    submit = SubmitField("Обновить пароли!")


class UploadFormTIFF(FlaskForm):
    file = FileField(validators=[FileRequired()])
    reduction = IntegerField(
        "Процент сжатия  до %(меньше значение - больше сжатия)",
        render_kw={"placeholder": "50%"},
        validators=[DataRequired(), NumberRange(min=1, max=99)],
    )
    submit = SubmitField("Загрузить для сжатия")


class UploadFormPDF(FlaskForm):
    file = FileField("File", validators=[DataRequired()])
    resolution = IntegerField(
        "DPI для сжатия как при сканировании, например 150.",
        default=150,
        validators=[DataRequired(), NumberRange(min=10, max=300)],
    )
    submit = SubmitField("Загрузить для сжатия")


class PhoneBookForm(FlaskForm):
    fio = StringField('ФИО', validators=[DataRequired()])
    position = StringField('Должность')
    phone_number = StringField('Телефон', validators=[DataRequired()])
    organization = StringField('Организация')
    short_number = StringField('Короткий телефон')
    personal_email = StringField('Электронная почта')
    submit = SubmitField('Сохранить')


class SearchPhoneBookForm(FlaskForm):
    search_field = StringField('Поиск')
    submit = SubmitField('Найти')


class UploadFormXLSX(FlaskForm):
    file = FileField("File", validators=[DataRequired()])
    submit = SubmitField("Загрузить для добавления контактов")
