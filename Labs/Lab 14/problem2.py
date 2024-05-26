from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList

class Playlist:

    def __init__(self):
        self.pList = ChainingHashTableMap()
        self.dll = DoublyLinkedList()
        #n = 0

    def add_song(self, songName):
        #self.n += 1

        song = DoublyLinkedList.Node(songName)
        self.pList[songName] = song
        self.dll.add_last(song)

    def add_song_after(self, old_song, new_song):

        songAfter = self.pList[old_song]

        song = DoublyLinkedList.Node(new_song)
        self.pList[new_song] = song

        self.dll.add_after(songAfter, song)


    def play_song(self, str):
        if str in self.pList:
            print("Playing", str)
        else:
            raise IndexError

    def play_list(self):
        for i in self.dll:
            print("Playing", i)


p1 = Playlist()
p1.add_song("hello")
p1.add_song("goodbye")
p1.add_song("world")
p1.add_song("mr blue sky")
p1.add_song("help")
p1.add_song_after("hello", "im still standing")
p1.play_song("world")
p1.play_list()