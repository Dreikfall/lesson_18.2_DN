from flask import Flask
from flask_restx import Api
from app.config import Config
from app.dao.model.director import Director
from app.dao.model.movie import Movie
from app.setup_db import db
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.directors import director_ns


# функция создания основного объекта app

def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)

def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


# Функция создания-наполнения таблиц
def create_data():
    genre_1 = Director(name="Юэнь У-Пин")
    movie_1 = Movie(title="Пьяный мастер",
                    description="Молодой Вонг Фей-Хун, будущий народный герой Китая, защитник обе"
                                "здоленных и обиженных, в молодости был весьма строптив и дерзок."
                                " Настолько, что отец отослал неуправляемого сына к дяде, известно"
                                "му мастеру кунг-фу и большому эксперту в двух вещах: распитии"
                                " крепких спиртных напитков и выбивании дури из самонадеянных"
                                " юнцов. Неудивительно, что герой сбегает от дяди-садиста при"
                                " первой же возможности",
                    trailer="https://www.kinopoisk.ru/film/24726/video/40256/", year=1978, rating=7.3, genre_id=1,
                    director_id=21)
    #db.drop_all()
    #db.create_all()
    with db.session.begin():
        db.session.add(genre_1)
        db.session.add(movie_1)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    register_extensions(app)
    #create_data()  объекты в таблицы бд уже добавлены
    app.run()
