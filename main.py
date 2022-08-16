from client import Client

def main():
    AUTH_TOKEN = input("Enter Authorization token: ")
    User_ID = input("Enter Username: ")

    spotify_client = Client(AUTH_TOKEN,User_ID)

    #last played tracks:
    tracks_to_visualize = int(input("Tracks to visualize?: "))
    last_played_tracks = spotify_client.last_played_tracks(tracks_to_visualize)

    print(f"Here are the last {tracks_to_visualize} tracks you listened to: ")
    for i, track in enumerate(last_played_tracks):
        print(f"{i}:{track}")

    #Songs to use as seeds: 
    indices = input("Enter a list of upto 5 tracks to use as seeds.(Use indices separated by space): ")
    indices = indices.split()
    seed_tracks = [last_played_tracks[int(i)-1] for i in indices]

    #Recommended tracks from seeds:
    recommended_tracks = spotify_client.track_recommendations(seed_tracks)
    print("\nHere are the recommended tracks that will be included in the new playlist: ")
    for i,track in enumerate(recommended_tracks):
        print(f"{i-1}:{track}")

    #New Playlist:
    playlist_name = input("Name of the new playlist: ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"Playlist '{playlist.name}' created successfully...")

    #Fill Playlist
    spotify_client.fill_playlist(playlist,recommended_tracks)
    print(f"\nTracks successfully added to Playlist '{playlist.name}'")
    

if __name__ == '__main__':
    main()