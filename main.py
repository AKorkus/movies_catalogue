from flask import Flask, render_template, url_for, redirect, request
import tmdb_client
import random
import json

app = Flask(__name__)

with open("list_types.json", "r") as f:
    list_of_lists = json.load(f)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size = "w342"):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/movies/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    try:
        movies = tmdb_client.get_movies(randomize=True, list_type = selected_list)
        return render_template("homepage.html", movies = movies, list_of_lists = list_of_lists, selected_list = selected_list)
    except:
        return redirect(url_for("homepage", list_type = "popular"))

@app.route('/movies/random')
def randompage():
    movie_id = random.randint(1,1000000)
    return redirect(f"/movie/{movie_id}")


@app.route('/movies/cnt<int:cnt>')
def homepage_cnt(cnt):
    movies = tmdb_client.get_movies(cnt)
    return render_template("homepage.html", movies = movies, list_of_lists = list_of_lists)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    try:
        movie = tmdb_client.get__movie_by_id(movie_id)
        cast = tmdb_client.get_single_movie_cast(movie_id)
        return render_template("movie_details.html", movie = movie, cast = cast)
    except:
        return redirect(url_for("randompage"))


 # ODPALATOR:.........................................................................................................
print(list_of_lists)
if __name__ ==("__main__"):
    app.run(debug=True)