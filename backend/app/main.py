# coding: utf-8
from sys import path
from pathlib import Path
from os.path import abspath, isfile, exists

if abspath('.') not in path:
    path.append(abspath('.'))

from fastapi import FastAPI, HTTPException, Depends
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fake import createusers, setpqroptions
from tools import  Tb, digest
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from sqlmodel import create_engine, SQLModel, Session, select
import modules
import importlib
import pkgutil

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

# create connection
if USESQLALCMEHY:
    engine = create_engine(settings.database_uri)
else:
    engine = create_engine(settings.database_user_uri) 
    
settings.engine = engine

def _import_submodules(module,item='model'):
    """Import all submodules of a module, recursively."""
    res = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(
            module.__path__, module.__name__ + '.'):
        if is_pkg:
            try:
                importlib.import_module(f'{module_name}.{item}')
            except:
                print(f'No se pudo importar  {module_name}.{item}')
            res.append(module_name.split('.')[1])
    return res

def modulesResolver(app, enabled_modules=None, **kwargs):
    enabled_modules = _import_submodules(modules, 'model')
    # Import router endpoints
    for module_name in enabled_modules:
        route = importlib.import_module(f'modules.{module_name}.routes', package=__name__)
        for element in dir(route):
            attr =  getattr(route, element)
            if isinstance(attr, APIRouter):
                app.include_router(attr)

modulesResolver(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"api": "/docs","message":"please visit localhost/docs to interact with api"}

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # getting the user
    with Session(engine) as session:
        res = select(Tb.User).filter(Tb.User.correo == form_data.username)
        user = session.exec(res).first()
        if user is None:
            HTTPException(status_code=404, detail='Usuario no encontrado')
    if digest(form_data.password) != user.password:
        raise HTTPException(
            status_code=400, detail="Usuario o contraseña equivocada")

    return {"access_token": user.correo, "token_type": "bearer"}

if USESQLALCMEHY:
    import uvicorn

    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)