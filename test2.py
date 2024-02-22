import imdb
from imdbmovies import IMDB

ia = imdb.Cinemagoer()

imdb_other = IMDB()


movies = imdb_other.get_by_id("tt1190634")
movie_name = movies['name']
movie_type = movies['type']
movie_genre = ", ".join(i for i in movies['genre'])
movie_datePublished = movies['datePublished']
movie_ratingValue = movies['rating']['ratingValue']
movie_poster_url = movies['poster']
movie_actor = ", ".join(i['name'] for i in movies['actor'])
movie_description = movies['description']

print(movies)
