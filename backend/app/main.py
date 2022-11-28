# coding: utf-8
from sys import path
from pathlib import Path
from os.path import abspath

cp = Path(__file__).parent
if abspath(cp) not in path:
    path.append(abspath(cp))

from fastapi import FastAPI
from tools import Tb
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from sqlmodel import SQLModel, create_engine
from imp_modules import modulesResolver
from fake import create_emails, create_users

app = FastAPI(
    title=settings.api_name,
    version=settings.version,
    description=settings.api_description,
    contact=settings.api_contact,
    license_info={
        "name": "GPL V3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
)

# making app globally available by calling settings
settings.app = app
setattr(app, "Tb", Tb)

# authentication
import auth

# select between SQLALCHEMY and MYsql engine
USESQLALCMEHY = False
if len(settings.database_user_uri.split("None")) > 4:
    USESQLALCMEHY = True
    engine = create_engine(settings.database_uri)
else:
    engine = create_engine(settings.database_user_uri)
settings.engine = engine

modulesResolver(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create data structure
SQLModel.metadata.create_all(engine)

# populate initial data
users = create_users()
create_emails(
    users,
    emails=["newmail@mail.com", "secondmail@gmail.com"],
    passwords=["123easdte", "4dsd9845"],
)

if USESQLALCMEHY:
    import uvicorn

    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)
