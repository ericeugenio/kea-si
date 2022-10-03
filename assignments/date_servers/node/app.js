import express from 'express'

const app = express()
const port = process.env.PORT || 8080

// ------------------------------------------------------------------------------------
// API Routes
// ------------------------------------------------------------------------------------

app.get('/timestamp', (req, res) => {
    const event = new Date()
    res.send(event.toISOString())
})

app.get('/timestamp-from-api', async (req, res) => {
    const response = await fetch('http://127.0.0.1:8000/timestamp')
    const timestamp = await response.json()
    res.send(timestamp)
})

// ------------------------------------------------------------------------------------
// Server start
// ------------------------------------------------------------------------------------

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})