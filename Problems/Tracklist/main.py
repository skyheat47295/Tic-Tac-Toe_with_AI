def tracklist(**bands):
    for band in bands:
        print(band)
        for album, track in bands[band].items():
            print('ALBUM:', album, 'TRACK:', track)