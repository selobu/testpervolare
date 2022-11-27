# coding: utf-8
from os import environ
from sys import path
from os.path import abspath

if abspath(".") not in path:
    path.append(abspath("."))
from fake import create_users, create_emails
from main import Tb, settings
from sqlmodel import create_engine, SQLModel

engine = create_engine(settings.database_maria_uri)
# creating database structure
SQLModel.metadata.create_all(engine)

# populating structure
create_users()
create_emails()
print("//----db updated----//")
