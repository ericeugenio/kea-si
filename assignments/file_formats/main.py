from python.parser import TxtParser, CsvParser

filename = "res/data.txt"
parser = TxtParser(filename)
songs = parser.parse()

for song in songs:
    print(song)