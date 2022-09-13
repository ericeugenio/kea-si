import json

from fastapi import FastAPI
from scripts import Song, fromTxt, fromJson, fromXml, fromCsv, fromYaml

app = FastAPI()

# ------------------------------------------------------------------------------------
# API Routes
# ------------------------------------------------------------------------------------

@app.get("/api/parser/txt")
def read_txt():
    filename = "res/data.txt"
    songs = fromTxt(filename)
    return json.dumps([song.__dict__ for song in songs])

@app.get("/api/parser/json")
def read_json():
    return {"Todo": "Implement"}

@app.get("/api/parser/csv")
def read_csv():
    filename = "res/data.csv"
    songs = fromCsv(filename)
    return json.dumps([song.__dict__ for song in songs])

@app.get("/api/parser/xml")
def read_xml():
    return {"Todo": "Implement"}

@app.get("/api/parser/yaml")
def read_yaml():
    return {"Todo": "Implement"}