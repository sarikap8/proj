import json
import requests
from secrets import spotify_user_id, spotify_token, playlist_id
#emotion = "sad"

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.playlist_id = playlist_id
        self.searchresults = []

    def get_tracks(self, list_id):
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            list_id)

        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.spotify_token)})
        response_json = response.json()
        print(response)

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)

        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()

        print(response)

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        self.add_search_songs()
        return self.tracks



    def search_mood(self, emotion):
        query = "https://api.spotify.com/v1/search?q=sad&type=playlist"
        response = requests.get(query,
                                headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(self.spotify_token)})
        response_json = response.json()
        print(response_json)
        for item in response_json['playlists']['items']:
            #print(item['id'])
            self.searchresults.append(item['id'])
        print(self.searchresults)


    def create_playlist(self, emotion):
        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
        request_body = json.dumps({
            "name":  "My " + str(emotion) + " playlist",
            "description": "Fire songs for when I'm " + str(emotion),
            "public": True}
        )
        response = requests.post(query, data=request_body, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })

        response_json = response.json()
        print(response_json)

        self.playlist_id=response_json['id']
        print(self.playlist_id)

    def add_search_songs(self):
        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.playlist_id, self.tracks)

        response = requests.post(query, headers={"Content-Type": "application/json",
                                                 "Authorization": "Bearer {}".format(self.spotify_token)})
        print(response.json)

a = SaveSongs()
a.search_mood("sad")
a.create_playlist("sad")
