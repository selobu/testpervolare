from pydantic import BaseSettings
from os import environ

adminpassword = environ.get("MYSQL_ROOT_PASSWORD")
adminuser = environ.get("MYSQL_ROOT_USER")
port = environ.get("MYSQL_PORT")
database = environ.get(
    "MYSQL_DATABASE",
)
host = environ.get("MYSQL_HOST")
user = environ.get("MYSQL_USER")
userpassword = environ.get("MYSQL_PASSWORD")


class Settings(BaseSettings):
    api_name: str = "Backend api"
    version: str = "0.0.1"
    api_description: str = "[source code](https://github.com/selobu/my_url)"
    admin_email: str = ""
    items_per_user: int = 50
    database_uri: str = "sqlite:///database.db"
    api_contact: object = {
        "name": "Sebastian López Buriticá",
        "email": "sebastian.lopez@gestionhseq.com",
        "url": "https://gestionhseq.com",
    }
    database_user_uri: str = (
        f"mysql+pymysql://{user}:{userpassword}@{host}:{port}/{database}"
    )
    app: object = {}
    engine: object = {}


settings = Settings()
