class Track:
    """
    For a single track
    """
    def __init__(self, name, id, artist):
        """
        name: Name of the song
        id: Spotify track id
        artist: Artist Name
        """
        self.name = name
        self.id = id
        self.artist = artist
    
    def create_uri(self):
        return f"spotify:track:{self.id}"
    
    def __str__(self):
        return self.name + " by " + self.artist