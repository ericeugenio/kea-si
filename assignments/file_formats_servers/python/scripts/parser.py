import csv

# ------------------------------------------------------------------------------------
# Model
# ------------------------------------------------------------------------------------

class Song:
    def __init__(self, title, genre, artists):
        self.title = title
        self.genre = genre
        self.artists = artists

    def __str__(self):
        return self.title + " (" + self.genre + ") is played by " + ", ".join(self.artists) + "."


# ------------------------------------------------------------------------------------
# Parsers
# ------------------------------------------------------------------------------------

def fromTxt(filename):
    extension = filename.split(".")[1]
    if extension != "txt":
        raise Exception("Expected file type is .txt, got ." + extension)

    with open(filename) as f:
        songs = []
        for i in range(int(f.readline())):
            title = f.readline()[:-1]
            genre = f.readline()[:-1]
            artists = []
            for j in range(int(f.readline())):
                artists.append(f.readline()[:-1])
            songs.append(Song(title, genre, artists))
    return songs


def fromJson(filename):
    pass


def fromCsv(filename):
    extension = filename.split(".")[1]
    if extension != "csv":
        raise Exception("Expected file type is .csv, got ." + extension)

    with open(filename, newline='') as f:
        flag = 1
        songs = []
        reader = csv.DictReader(f)
        for row in reader:
            if flag == 1:
                flag = 0

            title = row["title"]
            genre = row["genre"]
            artists = row["artists"].split(", ")
            songs.append(Song(title, genre, artists))
        return songs


def fromXml(filename):
    pass


def fromYaml(filename):
    pass