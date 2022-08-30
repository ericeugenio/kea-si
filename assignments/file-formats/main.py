# NOTICE: Python script only accepts txt and csv file

import csv

class Song:
    def __init__(self, title, genre, artists):
        self.title = title
        self.genre = genre
        self.artists = artists

    def __str__(self):
        return self.title + " (" + self.genre + ") is played by " + ", ".join(self.artists) + "."

class Parser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        pass

class TextParser(Parser):
    def parse(self):
        extension = self.filename.split(".")[1]
        if extension != "txt":
            raise Exception("Expected file type is .txt, got ." + extension)

        with open(self.filename) as f:
            songs = []
            for i in range(int(f.readline())):
                title = f.readline()[:-1]
                genre = f.readline()[:-1]
                artists = []
                for j in range(int(f.readline())):
                    artists.append(f.readline()[:-1])
                songs.append(Song(title, genre, artists))
            return songs

class CsvParser(Parser):
    def parse(self):
        extension = self.filename.split(".")[1]
        if extension != "csv":
            raise Exception("Expected file type is .csv, got ." + extension)

        with open(self.filename, newline='') as f:
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

# ------------------------------------------------------------------------------------
# TODO: Change filename and parser to prefered file type 
# ------------------------------------------------------------------------------------

try:
    filename = "data.csv"
    parser = CsvParser(filename)
    songs = parser.parse()
    for song in songs:
        print(song)
except Exception as e:
    print(e)