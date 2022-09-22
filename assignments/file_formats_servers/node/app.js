import express from 'express'
import swaggerUI from 'swagger-ui-express'
import swaggerJSDoc from 'swagger-jsdoc'

const app = express()
const port = process.env.PORT || 8080

// ------------------------------------------------------------------------------------
// API Documentation
// ------------------------------------------------------------------------------------

const options = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'File Formats API',
            version: '0.0.1',
        },
    },
    apis: ['./routes/*.js'],
}

const swaggerSpec = swaggerJSDoc(options);

app.use('/api/docs', swaggerUI.serve, swaggerUI.setup(swaggerSpec))

// ------------------------------------------------------------------------------------
// API Routes
// ------------------------------------------------------------------------------------



// ------------------------------------------------------------------------------------
// Server start
// ------------------------------------------------------------------------------------

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})