const express = require('express')
const app = express()
const port = 3000

const parser = require('../../file-formats/parser')

// ------------------------------------------------------------------------------------
// API Routes
// ------------------------------------------------------------------------------------

app.get('/api/parser/txt', (req, res) => {
    res.send('To be implemented...')
})

app.get('/api/parser/json', (req, res) => {
    res.json(parser.fromJson('../../file-formats/res/data.json'))
})

app.get('/api/parser/csv', (req, res) => {
    res.send('To be implemented...')
})

app.get('/api/parser/xml', (req, res) => {
    res.send('To be implemented...')
})

app.get('/api/parser/yaml', (req, res) => {
    res.send('To be implemented...')
})

// ------------------------------------------------------------------------------------
// Server start
// ------------------------------------------------------------------------------------

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})