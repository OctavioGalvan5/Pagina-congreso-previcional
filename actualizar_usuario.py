from dotenv import load_dotenv
load_dotenv()

from werkzeug.security import generate_password_hash
from app import app, db, Usuario

USUARIOS = [
    {'email': 'ale_terra@hotmail.com', 'password': '27686344', 'nombre': 'ale_terra@hotmail.com', 'modalidad': 'presencial'},
    {'email': 'admin@gmail.com',       'password': 'admin123',  'nombre': 'Administrador',          'modalidad': 'presencial'},
]

with app.app_context():
    for u in USUARIOS:
        usuario = Usuario.query.filter_by(email=u['email']).first()
        if usuario:
            usuario.password_hash = generate_password_hash(u['password'])
            db.session.commit()
            print(f"Contraseña actualizada para: {u['email']}")
        else:
            nuevo = Usuario(
                email=u['email'],
                password_hash=generate_password_hash(u['password']),
                nombre_completo=u['nombre'],
                modalidad=u['modalidad']
            )
            db.session.add(nuevo)
            db.session.commit()
            print(f"Usuario creado: {u['email']} | modalidad: {u['modalidad']}")
