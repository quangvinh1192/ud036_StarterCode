import webbrowser


class Movie():
    """
    Movie encapsulates a movie title, a poster URL and a youtube link trailor
    """
    def __init__(self, movie_title, poster_img, trailer_youtube):
        """
        Construct a new Movie object
        :param title: The title of Movie
        :pram poster_image_url: The poster URL of Movie
        :param trailer_youtube_url: The youtube link of Movie
        :return: returns nothing
        """
        self.title = movie_title
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        show_trailer will show the youtube trailor
        :return: returns nothing
        """
        webbrowser.open(self.trailer_youtube_url)
