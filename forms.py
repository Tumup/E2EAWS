from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField , SelectField
from wtforms.validators import DataRequired, Length

class VideojuegoForm(FlaskForm):
    titulo = StringField('Título del Juego', validators=[DataRequired(), Length(max=100)])
    empresa_desarrolladora = StringField('Empresa Desarolladora del Juego', validators=[DataRequired(), Length(max=100)])
    genero = StringField('Género del Juego', validators=[DataRequired(), Length(max=50)])
    anio_publicacion = IntegerField('Año de Publicación', validators=[DataRequired()])
    competicion = SelectField('Competitivo', choices=[('True', 'Sí'), ('False', 'No')], validators=[DataRequired()])
    submit = SubmitField('Registrar Juego')