from flask import Flask
from modelos import db , Usuario, Profesional, Ticket

app= Flask('app')

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

with app.app_context():
    
    #usuarios     
    usuario_1= Usuario(nombre_y_apellido= 'Arami Paraschiw', city='pengui', email='aramiverap@gmail.com', contrasenha='name')
    usuario_2= Usuario(nombre_y_apellido= 'Aru Martinez', city='cabo', email='arumar@gmail.com', contrasenha='nul')
    
    #profesional
    prof_1 = Profesional(nombre_y_apellido='Agustina Fanego', city='Luque', email='agussfan@gmail.com', numero_phone='0971863549', contrasenha='654321', profesion='Psicologa', descripcion ='Soy una profesional empática y calificada, dedicada a ayudar a mis pacientes a superar desafíos emocionales y mentales. Con amplia experiencia y formación en diversas técnicas terapéuticas, proporciono un espacio seguro y de apoyo, fomentando la reflexión y el crecimiento personal', descripcion_det='La psicóloga es una profesional empática y calificada, dedicada a ayudar a sus pacientes a superar desafíos emocionales y mentales. Con amplia experiencia y formación en diversas técnicas terapéuticas, proporciona un espacio seguro y de apoyo, fomentando la reflexión y el crecimiento personal')
    prof_2 = Profesional(nombre_y_apellido='Adriana Caballero', city='Asuncion', email='adricab@gmail.com', numero_phone='0981378654', contrasenha='987654', profesion='Periodista', descripcion ='Soy una periodista que ofrece un servicio informativo y veraz, dedicándome a la investigación exhaustiva y al análisis crítico de eventos actuales. Mi habilidad para comunicar de manera clara y concisa me permiten transmitir noticias y perspectivas importantes al público.', descripcion_det='La periodista ofrece un servicio informativo y veraz, dedicándose a la investigación exhaustiva y al análisis crítico de eventos actuales. Su habilidad para comunicar de manera clara y concisa permite transmitir noticias y perspectivas importantes al público.')
    
    db.session.add(usuario_1)
    db.session.add(usuario_2)
    db.session.add(prof_1)
    db.session.add(prof_2)
    db.session.commit()


