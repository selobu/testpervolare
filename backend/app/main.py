# coding: utf-8
from sys import path
from pathlib import Path
from os.path import abspath

cp = Path(__file__).parent
if abspath(cp) not in path:
    path.append(abspath(cp))

from fastapi import FastAPI, HTTPException, Depends

from tools import  Tb
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from sqlmodel import create_engine, Session, select
from imp_modules import modulesResolver

USESQLALCMEHY = True

app = FastAPI(
    title= settings.api_name,
    version= settings.version,
    description= settings.api_description,
    contact= settings.api_contact,
    license_info={'name': 'GPL V3',
                  'url': 'https://www.gnu.org/licenses/gpl-3.0.en.html'})

# making app globally available by calling settings
settings.app = app
setattr(app,'Tb', Tb)

# Select engine
if USESQLALCMEHY:
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

if USESQLALCMEHY:
    import uvicorn

    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)