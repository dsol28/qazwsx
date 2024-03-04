from flask import Flask
from data import db_session
from data.users import User
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/mars_explorer.db')

def main():
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_0"
    user.email = "scott_chief1@mars.org"
    user.set_password("cap")

    session = db_session.create_session()
    session.add(user)

    session.commit()

main()