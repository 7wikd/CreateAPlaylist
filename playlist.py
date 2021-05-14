class Playlist:
    """
    A Spotify Playlist
    """
    def __init__(self,name,id) -> None:
        """
        name: Name of the Playlist
        id: Spotify Playlist id
        """
        self.name = name
        self.id = id

    def __str__(self):
        return f"Playlist: {self.name}"