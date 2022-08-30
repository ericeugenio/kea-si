/* NOTICE: Nodejs script only accepts json file */

const filename = 'data.json';
const fs = require('fs');

let rawdata = fs.readFileSync(filename);
let songs = JSON.parse(rawdata);

for (const song of songs) {
    console.log(song.title + ' (' + song.genre + ') ' + 'is played by ' + song.artists + '.');
}
