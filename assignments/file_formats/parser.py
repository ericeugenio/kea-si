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

class Parser:
    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        pass


class TxtParser(Parser):
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


class JsonParser(Parser):
    # TODO: implement .json parser
    pass


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


class XmlParser(Parser):
    # TODO: implement .xml parser
    pass


class YamlParser(Parser):
    # TODO: implement .yaml parser
    pass