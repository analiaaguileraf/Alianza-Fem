#importar la libreria para poder construir la aplicacion 

from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Usuario, Profesional, Ticket
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)




@app.route('/')
def inicio():
    return render_template('landing.html')


@app.route('/nosotras')
def nosotras():
    return render_template('sitio/nosotras.html')


@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')


@app.route('/admin/nosotras')
def admin_nosotras():
    return render_template('admin/nosotras.html')



# ---------- Profesional-------------

@app.route('/prof/')
def prof_index():
    return render_template('prof/index.html')

@app.route('/prof/nosotras')
def prof_nosotras():
    return render_template('prof/nosotras.html')





# ----------Fin prof--------------


@app.route('/admin/lista_usu.html')
def admin_lista_usu():

    usuarios= Usuario.query.all()

    return render_template('admin/lista_usu.html', usuarios=usuarios)

@app.route('/lista_prof.html', methods=['POST', "GET"]) 
def lista_prof():

    profesionales= Profesional.query.all()
   

    return render_template('match.html', profesionales=profesionales)

 
 
@app.route('/user_registro', methods=['POST', "GET"])
def user_registro():
    if request.method =='POST':
        print("hola")

        # Obtener los datos de mi formulario
        nombre_y_apellido = request.form.get('nombre_y_apellido')
        city= request.form.get('city')
        email= request.form.get('email')
        contrasenha= request.form.get('contrasenha')

        # Creamos el objeto de tipo alumno
        usuario = Usuario(nombre_y_apellido= nombre_y_apellido, city= city, email=email, contrasenha=contrasenha)

        # Agregamos el objeto a la db
        db.session.add(usuario)

        # Guardamos los cambios
        db.session.commit()
        return redirect(url_for('lista_prof'))
    return render_template('cuenta_usuario.html')


@app.route('/prof_registro', methods=['POST', "GET"])
def prof_registro():
    if request.method =='POST':

        # Obtener los datos de mi formulario
        nombre_y_apellido = request.form.get('nombre_y_apellido')
        city= request.form.get('ciudad')
        email= request.form.get('email')
        numero_phone= request.form.get('numero_phone')
        contrasenha= request.form.get('contrasenha')
        profesion= request.form.get('profesion')
        descripcion= request.form.get('descripcion')

        # Creamos el objeto de tipo alumno
        profesional = Profesional(nombre_y_apellido= nombre_y_apellido, city= city, email=email, numero_phone=numero_phone, contrasenha=contrasenha, profesion=profesion, descripcion=descripcion)

        # Agregamos el objeto a la db
        db.session.add(profesional)

        # Guardamos los cambios
        db.session.commit()
        return redirect(url_for('usuarios'))
    return render_template('cuenta_profesional.html')




@app.route('/user_editar/<id>', methods=['GET', 'POST'])
def user_editar(id):

    # Obtenemos la alumna a modificar
    usuarios = Usuario.query.get(id)
    
    if request.method == 'POST':
        usuarios.nombre_y_apellido = request.form.get('nombre_y_apellido')
        usuarios.city= request.form.get('city')
        usuarios.email= request.form.get('email')
        usuarios.contrasenha= request.form.get('contrasenha')
        db.session.commit()
        return redirect(url_for('inicio'))
    
    return render_template('admin/user_editar.html', usuarios=usuarios)
    
    

@app.route('/prof_editar/<id>', methods=['GET', 'POST'])
def prof_editar(id):

    # Obtenemos la alumna a modificar
    profesionales = Profesional.query.get(id)

    if request.method == 'POST':
        profesionales.nombre_y_apellido = request.form.get('nombre_y_apellido')
        profesionales.city= request.form.get('city')
        profesionales.email= request.form.get('email')
        profesionales.numero_phone= request.form.get('numero_phone')
        profesionales.contrasenha= request.form.get('contrasenha')
        profesionales.profesion= request.form.get('profesion')
        profesionales.descripcion= request.form.get('descripcion')
        db.session.commit()

        return redirect(url_for('inicio'))

    return render_template('admin/prof_editar.html', profesionales=profesionales)

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    profesionales= Profesional.query.all()
    usuarios = Usuario.query.all()
    tickets= Ticket.query.all()
    
    return render_template('historias.html', profesionales=profesionales, tickets=tickets,usuarios=usuarios)


@app.route('/ver_perfil/<id>', methods=['GET', 'POST'])
def ver_perfil(id):

    # Obtenemos la alumna a modificar
    profesionales = Profesional.query.get(id)
    
    if request.method == 'POST':
        profesionales.nombre_y_apellido = request.form.get('nombre_y_apellido')
        profesionales.profesion= request.form.get('profesion')
        profesionales.descripcion_det= request.form.get('descripcion_det')
        db.session.commit()
        return redirect(url_for('cursos'))
    
    return render_template('perfil_profesional.html', profesionales=profesionales)



@app.route('/ayudar/<id>', methods=['GET', 'POST'])
def ayudar(id):

    # Obtenemos la alumna a modificar
    usuario = Usuario.query.get(id)
    tickets = Ticket.query.get(id)


    if request.method == 'POST':
        usuario.nombre_y_apellido = request.form.get('nombre_y_apellido')
        usuario.descripcion= request.form.get('descripcion')
        usuario.email= request.form.get('email')
        db.session.commit()
        return redirect(url_for('/index'))

    return render_template('perfil_usuario.html', usuario=usuario,tickets=tickets)



@app.route('/ticket.html', methods=['POST', "GET"])
def ticket():
    if request.method =='POST':

        # Obtener los datos de mi formulario
        tipo_trabajo= request.form.get('tipo_trabajo')
        descripcion= request.form.get('descripcion')
        ciudad= request.form.get('ciudad')

        # Creamos el objeto de tipo alumno
        ticket= Ticket(tipo_trabajo=tipo_trabajo, descripcion=descripcion, ciudad=ciudad)

        # Agregamos el objeto a la db
        db.session.add(ticket)

        # Guardamos los cambios
        db.session.commit()
        return redirect(url_for('inicio'))
    return render_template('tickets.html')

        

  
 
 
if __name__== '__main__':
    app.run (debug=True)