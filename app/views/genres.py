from flask_restx import Namespace, Resource

from app.dao.model.genre import GenreSchema
from app.implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid):
        genre_id = genre_service.get_one(gid)
        return genre_schema.dump(genre_id), 200
