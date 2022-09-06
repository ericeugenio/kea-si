import json

from fastapi import FastAPI
from ..file_formats.parser import TxtParser, CsvParser

app = FastAPI()

# ------------------------------------------------------------------------------------
# API Routes
# ------------------------------------------------------------------------------------

@app.get("/api/parser/txt")
def read_txt():
    filename = "../../file_formats/res/data.txt"
    parser = TxtParser(filename)
    songs = parser.parse()
    return json.dumps(songs)

@app.get("/api/parser/json")
def read_json():
    return {"Todo": "Implement"}

@app.get("/api/parser/csv")
def read_csv():
    filename = "../../file_formats/res/data.csv"
    parser = CsvParser(filename)
    songs = parser.parse()
    return json.dumps(songs)

@app.get("/api/parser/xml")
def read_xml():
    return {"Todo": "Implement"}

@app.get("/api/parser/yaml")
def read_yaml():
    return {"Todo": "Implement"}