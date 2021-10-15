song = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
import re
def song_decoder(song):
    original_song = re.sub('WUB',' ',song)
    return ' '.join((original_song.strip(' ')).split())

print(song_decoder(song))