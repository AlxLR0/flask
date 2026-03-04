from flask_wtf import FlaskForm
from wtforms import HiddenField, IntegerField, SubmitField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired


class ClienteForma( FlaskForm):
    id = HiddenField('Id')
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia = IntegerField('Membresia', validators=[DataRequired()])
    guardar = SubmitField('Guardar')

    