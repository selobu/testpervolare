# coding:utf-8
__all__ = ["create_users", "create_emails"]
from config import settings
from sqlalchemy.orm import Session
from sqlalchemy import select
from tools import digest
from json import dumps


def create_emails(users: list[int], emails: list, passwords: list):
    Tb = settings.app.Tb
    with Session(settings.engine) as session:
        not2add = select(Tb.Login.user_id).filter(Tb.Login.user_id.in_(users))
        not2add = session.execute(not2add).all()
        # testing under heroku server
        # raise Exception(dumps(session.execute(select(Tb.User.correo)).all()))
        toadd = [
            {"email": email, "password": digest(password), "user_id": user}
            for user, email, password in zip(users, emails, passwords)
            if user not in not2add
        ]
        for logindata in toadd:
            session.add(Tb.Login(**logindata))
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
        not2add = select(Tb.User.nombre_completo).filter(
            Tb.User.nombre_completo.in_(nombres)
        )
        not2add = session.execute(not2add).all()
        not2add = [x for l in not2add for x in l]
        # testing under heroku server
        # raise Exception(dumps(session.execute(select(Tb.User.correo)).all()))
        toadd = [usr for usr in default_users if usr["nombre_completo"] not in not2add]
        res = []
        for user in toadd:
            res.append(Tb.User(**user))
            session.add(res[-1])
        session.commit()
        [session.refresh(r) for r in res]
    return [r.id for r in res]


def fake_hash_password(password: str):
    return "fakehashed" + password
