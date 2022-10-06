import fs from 'fs'


function fromTxt(filename) {
    // TODO: implement .txt parser
}

function fromJson(filename) {
    const rawData = fs.readFileSync(filename)
    return JSON.parse(rawData)
}

function fromCsv(filename) {
    // TODO: implement .csv parser
}

function fromXml(filename) {
    // TODO: implement .csv parser
}

function fromYaml(filename) {
    // TODO: implement .csv parser
}

export { fromJson }