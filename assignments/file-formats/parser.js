/* NOTICE: Node script only accepts json and yaml files */

const fs = require('fs')

module.exports = {
    fromTxt: function (filename) {
        // TODO: implement .txt parser
    },
    fromJson: function (filename) {
        const rawData = fs.readFileSync(filename)
        return JSON.parse(rawData)
    },
    fromCsv: function (filename) {
        // TODO: implement .csv parser
    },
    fromXml: function (filename) {
        // TODO: implement .xml parser
    },
    fromYaml: function (filename) {
        // TODO: implement .yaml parser
    }
}