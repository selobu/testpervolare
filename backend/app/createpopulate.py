# coding: utf-8
from os import environ
from sys import path
from os.path import abspath

if abspath(".") not in path:
    path.append(abspath("."))
from fake import create_users, create_emails
from main import Tb, settings
from sqlmodel import create_engine, SQLModel

engine = create_engine(settings.database_user_uri)
# creating database structure
SQLModel.metadata.create_all(engine)

# populating structure

# populate initial data
users = create_users()
create_emails(
    users,
    emails=["newmail@mail.com", "secondmail@gmail.com"],
    passwords=["123easdte", "4dsd9845"],
)

print("//----db updated----//")
