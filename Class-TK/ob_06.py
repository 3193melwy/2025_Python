class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = [] 

    def add(self, track):
        self.tracks.append(track)

    def count(self):
        return len(self.tracks)

    def show(self):
        tracks_str = ', '.join([f"'{t}'" for t in self.tracks])
        return f"플레이명: {self.name}, 곡 수: {self.count()}, 곡들: [{tracks_str}]"

pl = Playlist("MyList")
pl.add("Dynamite"); pl.add("Butter")
print(pl.show()) #플리명: MyList, 곡 수: 2, 곡들: [Dynamite, Butter]