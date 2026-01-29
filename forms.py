from wtforms import Form, StringField, TextAreaField, SubmitField, IntegerField, validators
from wtforms.fields.simple import EmailField, HiddenField


class UserForm(Form):

    matricula = IntegerField("Matricula", validators=[
        validators.DataRequired(message="Matricula es requerida"),
        validators.NumberRange(min=100, max=1000, message="Matricula no está en el rango"),

    ])
    nombre = StringField("Nombre", validators=[
        validators.DataRequired(message="Nombre es requerido"),
        validators.Length(min=3, max=10, message="Nombre no tiene una longitud valida"),
    ])
    apellido_uno = StringField("Apellido uno", validators=[
        validators.DataRequired(message="Apellido uno es requerido"),
    ])
    apellido_dos = StringField("Apellido dos", validators=[
        validators.DataRequired(message="Apellido dos es requerido"),
    ])
    correo = EmailField("Correo", validators=[
        validators.DataRequired(message="Correo es requerido"),
    ])
