import webbrowser

# Define class Movie
class Movie():
    def __init__(self, movie_title, poster_image, trailer_url):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
