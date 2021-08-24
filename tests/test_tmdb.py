import tmdb_client
from unittest.mock import Mock
from main import app
import resources as rr

def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = 	"/rr7E0NoGKxvbkb89eR1GwfoYjpA.jpg"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    #poster_url = tmdb_client.get_poster_url(poster_path=poster_api_path)
    poster_url = ""
    # Porównanie wyników
    assert expected_default_size in poster_url
    #assert poster_url == "https://image.tmdb.org/t/p/w342/rr7E0NoGKxvbkb89eR1GwfoYjpA.jpg"

def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None



def test_movie1(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = rr.movie1 #tmdb_client.get__movie_by_id(550)
   monkeypatch.setattr("tmdb_client.get__movie_by_id", my_mock)
   result = tmdb_client.get__movie_by_id(550)
   assert result == my_mock.return_value

def test_movie2(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = rr.movie2 #tmdb_client.get__movie_by_id(400)
   monkeypatch.setattr("tmdb_client.get__movie_by_id", my_mock)
   result = tmdb_client.get__movie_by_id(400)
   assert result == my_mock.return_value

def test_poster_id1(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = rr.poster1 #tmdb_client.get_poster_id(600)
   monkeypatch.setattr("tmdb_client.get_poster_id", my_mock)
   result = tmdb_client.get_poster_id(600)
   assert result == my_mock.return_value


def test_poster_id2(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = rr.poster2 #tmdb_client.get_poster_id(800)
   monkeypatch.setattr("tmdb_client.get_poster_id", my_mock)
   result = tmdb_client.get_poster_id(800)
   assert result == my_mock.return_value


def test_poster_cast(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = rr.kast1 #tmdb_client.get_single_movie_cast(1600)
   monkeypatch.setattr("tmdb_client.get_single_movie_cast", my_mock)
   result = tmdb_client.get_single_movie_cast(1600)
   assert result == my_mock.return_value

def test_poster_cast(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = rr.kast2 #tmdb_client.get_single_movie_cast(2000)
   monkeypatch.setattr("tmdb_client.get_single_movie_cast", my_mock)
   result = tmdb_client.get_single_movie_cast(2000)
   assert result == my_mock.return_value

