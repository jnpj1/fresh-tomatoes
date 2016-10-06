import media
import fresh_tomatoes

# Create instances of Movie class
up = media.Movie("Up",
                 "http://www.gstatic.com/tv/thumb/movieposters/190662/p190662_p_v8_aq.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

water = media.Movie("Water",
                    "http://www.gstatic.com/tv/thumb/movieposters/160031/p160031_p_v8_aa.jpg",
                    "https://www.youtube.com/watch?v=2R0pRl18js8")

piano = media.Movie("The Piano",
					"https://upload.wikimedia.org/wikipedia/en/9/90/The-piano-poster.jpg",
					"https://www.youtube.com/watch?v=cyTn4XIYH8M")

lion_king = media.Movie("The Lion King",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=uUfs9fVpdvw")

princess_bride = media.Movie("The Princess Bride",
							"https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
							"https://www.youtube.com/watch?v=VYgcrny2hRs")

holy_grail = media.Movie("Monty Python and the Holy Grail",
						"https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",
						"https://www.youtube.com/watch?v=scD4_ZVDD-8")

# Add movies to list and call function for opening movie page
movies = [up, water, piano, lion_king, princess_bride, holy_grail]
fresh_tomatoes.open_movies_page(movies)
