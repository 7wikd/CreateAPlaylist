import json
import requests
from requests.models import Response
from track import Track
from playlist import Playlist

class Client:
    def __init__(self,auth_token,user_id):
        self.auth_token = auth_token
        self.user_id = user_id

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
            }
        )
        return response

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
            }
        )
        return response

    def last_played_tracks(self, limit=10):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in response_json["items"]]        
        return tracks

    def track_recommendations(self,seed_tracks,limit=50):
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ','
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in response_json["tracks"]]        
        return tracks

    
    def create_playlist(self,name):
        data = json.dumps({
            "name":name,
            "description":"Recommended Songs: ",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = self._place_post_api_request(url,data)
        response_json = response.json()

        #Create playlist
        
        p_id = response_json["id"]
        playlist = Playlist(name, p_id)
        return playlist

    def fill_playlist(self,playlist,tracks):
        track_uris = [track.create_uri() for track in tracks]
        data = json.dumps(track_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self._place_post_api_request(url,data)
        response_json = response.json()
        return response_json
    
