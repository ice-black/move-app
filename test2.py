from imdbmovies import IMDB
imdb_other = IMDB()
movies = imdb_other.get_by_id("tt0944947")
movie_type = movies['type']
movie_name = movies['name']

movie_poster_url = movies['poster']

