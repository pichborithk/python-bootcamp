from songs_manager import SongsManager
from sp import SP


def main():
    songs_manager = SongsManager.get()
    song_titles = songs_manager.get_titles()
    date = songs_manager.date
    year = songs_manager.year
    sp = SP()

    song_uris = []

    for song in song_titles:
        uri = sp.get_song_uri(song=song, year=year)
        if uri:
            song_uris.append(uri)

    sp.create_playlist(date=date, list_uris=song_uris)


if __name__ == "__main__":
    main()
