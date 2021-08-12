import requests
import random
from keyapi import api_key
 

def get_movies_list(list_type):
    """
    Request specific list of movies json from api (popular movies by default) from tmdb.
    """
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"

    response = requests.get(f"{endpoint}?api_key={api_key}")
    response.raise_for_status()
    return response.json()

def get__movie_by_id(movie_id):
    """
    Request json from api for a specific movie by id from tmdb.
    """
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"

    response = requests.get(f"{endpoint}?api_key={api_key}")
    return response.json()

def get_single_movie_cast(movie_id):
    """
    Request json from api for a specific movie by id from tmdb.
    """
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"

    response = requests.get(f"{endpoint}?api_key={api_key}")
    return response.json()["cast"]

def get_movie_info(movie):
    return {"title": movie["original_title"], "poster": get_poster_url(movie["poster_path"])}

def get_movies(how_many = 16, list_type = "popular", randomize = False):
    result = get_movies_list(list_type)["results"]
    if randomize:
        random.shuffle(result)
    result = result[:how_many]
    return result

def get_poster_url(poster_path, size = "w342"):
    """
    Combines link to poster image from base domain, deisred size (w342 in default) and poster_path.
    """
    baselink = "https://image.tmdb.org/t/p/"
    endlink = f"{baselink}{size}{poster_path}"
    return endlink


def get_posters(list_type = "popular", size = "w342"):
    """
    get_poster_url applied to json data (popular in default) and size (w342 in default) from movies api.
    """
    linx = []
    for result in get_movies_list(list_type)["results"]:
        endlink = get_poster_url(result["poster_path"], size)
        linx.append(endlink)
    return linx



if __name__ == "__main__":
    image_linx = get_posters()
    for img_link in image_linx:
        print(img_link)