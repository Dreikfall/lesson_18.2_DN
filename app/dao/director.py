from app.dao.model.director import Director

# Создаем DAO класс для таблицы класса Director

class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        director_query = self.session.query(Director)
        return director_query.all()

    def get_one(self, did):
        return self.session.query(Director).filter(Director.id == did).one()
