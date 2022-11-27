# coding:utf-8
__all__ = ["create_users", "create_emails"]
from config import settings
from sqlmodel import Session, select
from tools import digest
from json import dumps


def create_emails():
    Tb = settings.app.Tb
    with Session(settings.engine) as session:
        not2add = select(Tb.TipoSolicitud.tipo).filter(Tb.TipoSolicitud.tipo.in_(tipos))
        not2add = session.exec(not2add).all()
        # testing under heroku server
        # raise Exception(dumps(session.exec(select(Tb.User.correo)).all()))
        toadd = [pqr for pqr in pqrs if pqr["tipo"] not in not2add]
        for pqr in toadd:
            session.add(Tb.TipoSolicitud(**pqr))
        session.commit()


def create_users():
    Tb = settings.app.Tb
    default_users = [
        {
            "nombre_completo": "selobu Perez Doe",
            "cedula": "123213",
            "departamento": "Cundinamarca",
            "municipio": "cota",
            "direccion": "calle",
            "activo": True,
        },
        {
            "nombre_completo": "johndo Mendez",
            "cedula": "123214",
            "departamento": "Cundinamarca",
            "municipio": "cota",
            "direccion": "calle",
            "activo": False,
        },
    ]
    nombres = [u["nombre_completo"] for u in default_users]
    with Session(settings.engine) as session:
        not2add = select(Tb.User.nombre_completo).\
            filter(Tb.User.nombre_completo.in_(nombres))
        not2add = session.exec(not2add).all()
        # testing under heroku server
        # raise Exception(dumps(session.exec(select(Tb.User.correo)).all()))
        toadd = [usr for usr in default_users if usr["nombre_completo"] not in not2add]
        for user in toadd:
            session.add(Tb.User(**user))
        session.commit()

def fake_hash_password(password: str):
    return "fakehashed" + password
