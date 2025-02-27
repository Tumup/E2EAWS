import logging
from flask import Flask, render_template, redirect, url_for
from forms import VideojuegoForm
import boto3
from botocore.exceptions import NoCredentialsError
import uuid
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
csrf = CSRFProtect(app)

# Configura el cliente de DynamoDB usando el rol asignado a la instancia EC2
session = boto3.Session()
dynamodb = session.resource('dynamodb', region_name='us-east-2')

table_name = 'videojuegos'

# Configura el logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    form = VideojuegoForm()
    return render_template('index.html', form=form)


@app.route('/registrar_videojuego', methods=['GET', 'POST'])
def registrar_videojuego():
    logging.info('Acceso al método para registrar un Videojuego')
    form = VideojuegoForm()
    if form.validate_on_submit():
        # Procesa el formulario solo si es una solicitud POST válida
        id = str(uuid.uuid4())
        titulo = form.titulo.data
        empresa_desarrolladora = form.empresa_desarrolladora.data
        genero = form.genero.data
        anio_publicacion = form.anio_publicacion.data
        competicion = form.competicion.data

        # Conecta con la tabla DynamoDB y registra el videojuego
        try:
            table = dynamodb.Table(table_name)
            response = table.put_item(
                Item={
                    'id': id,
                    'titulo': titulo,
                    'empresa_desarrolladora': empresa_desarrolladora,
                    'genero': genero,
                    'anio_publicacion': anio_publicacion,
                    'competicion': competicion
                }
            )
            logging.info('Videojuego registrado con éxito')
            return render_template('exito.html')
        except Exception as ex:
            logging.error(f'Ocurrió un error al registrar el Videojuego: {ex}')
            return render_template('error.html')  # Página de error genérico
    return render_template('exito.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
