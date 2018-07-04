import media 
import fresh_tomatoes #create an HTML file 

#Create a list of movie 
toy_story = media.Movie("Toy Story",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")
interstellar = media.Movie("Interstellar",
	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
	"https://www.youtube.com/watch?v=zSWdZVtXT7E")
the_godfather = media.Movie( "The Godfather",
	"https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
	"https://www.youtube.com/watch?v=sY1S34973zA")
the_dark_knight = media.Movie("The Dark Knight",
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY")
#list of movies object
movies  = [toy_story, avatar, interstellar,the_godfather,the_dark_knight]
#creates a HTML file and runs it
fresh_tomatoes.open_movies_page(movies)
