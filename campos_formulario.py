from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import Flaskfrom
from wtforms import (StringField, Submitfield, BooleanField,DataTimeField, RadioField, SelectField,TextAreaFiel)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'

class Formulario(FlaskForm):
    nombre = StringField('Nombre es', validators=[DataRequired()])
    edad = BooleanField('Eres mayor de edad')
    sexo = RadioField('Sexo', choices=[('H','Hombre'), ('M','Mujer')])
    color = SelectField('Color favorito:', choices=[('Rojo','R'),('Verde','V'),('Azul','A')])

    comentario = TextAreaFiel()
    botton = SelectField('Enviar')

@app.route("/informacion")
def informacion():
    return render_template('campos_formulario.html')

@app.route('/datos', methods=['GET', 'POST'])
def datos():
    miformulario = Formulario()
    if miformulario.validate_on_submit():
        session['nombre'] = miformulario.nombre.data
        session['edad'] = miformulario.edad.data
        session['sexo'] = miformulario.sexo.data
        session['color'] = miformulario.color.data
        session['comentario'] = miformulario.comentario.data
        session['botton'] = miformulario.botton
        return redirect(url_for('informacion'))
    
    return render_template('campos_formulario2.html', formulario=miformulario)

if __name__=='__main__':
    app.run(debug=True)
