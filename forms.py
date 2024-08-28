from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, ValidationError, DataRequired


def correct_size_validator(form, field):
    if not field.data.isdigit() or int(field.data) > 9 or int(field.data) < 3:
        raise ValidationError('Некорректное значение числа')


def digit_validator(form, field):
    if not field.data.isdigit():
        raise ValidationError('Некорректное значение числа')


class StartForm(FlaskForm):
    size = StringField(
        "Число какой длины Вам загадать? (введите целое число от 3 до 9, например 4)",
        validators=[InputRequired()]
    )

    play = SubmitField("Играть")


class PlayForm(FlaskForm):
    attempt = StringField("Введите число (вашу догадку):", validators=[DataRequired()])
    check = SubmitField("Проверить")
