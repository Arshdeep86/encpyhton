"""
1> think of object
   song: title, artists, duration

2> write its class
"""

class song:
    def __init__(self, title, artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.nextSong = None
        self.previousSong = None

    def showSongDetails(self):
        print("{}\t{}\t{}".format(self.title,self.artist,self.duration))

# from class create real object in memory
song1 = song("1.Muqabla","yash",2.56)
song2 = song("2.ek toh","neha kakkar",3.44)
song3 = song("3.jeene do na","arijit",5.56)
song4 = song("4.dil","yash",4.00)
song5 = song("5.gulaabi","juggy",2.26)

print(song1)
print(song2)
print(song3)
print(song4)
print(song5)

# refernce copy operation
song1.nextSong = song2
song2.nextSong = song3
song3.nextSong = song4
song4.nextSong = song5
song5.nextSong = song1

song1.previousSong = song5
song2.previousSong = song1
song3.previousSong = song2
song4.previousSong = song3
song5.previousSong = song4


#song1.showSongDetails()
#song1.nextSong.showSongDetails()
#song3.previousSong.showSongDetails()

temp = song1
while temp.nextSong != song1:
    temp.showSongDetails()
    temp = temp.nextSong

song5.showSongDetails()   # for last song

print("~~~~~~~~~~`iterating  backward~~~~~~~~~~~~~~```")
current = song5
while current.previousSong != song5:
     current.showSongDetails()
     current = current.previousSong

current.showSongDetails()




