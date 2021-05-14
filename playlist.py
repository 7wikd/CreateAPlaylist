class Playlist:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    def __str__(self):
        return f"Playlist: {self.name}"