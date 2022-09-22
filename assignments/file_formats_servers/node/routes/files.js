import { Router } from 'express'
import { fromJson } from '../models/parser.js'

const router = Router();

/**
 * @openapi
 * /api/parser/txt:
 *   get:
 *     summary: To be implemented.. 
 */
router.get('/api/parser/txt', (req, res) => {
    res.send('To be implemented...')
})

/**
 * @openapi
 * /api/parser/json:
 *   get:
 *     summary: Returns a list of songs from a txt file.
 *     description: Returns a list of songs from a json file, in json format.
 *     responses:
 *       200:
 *         description: Returns a list of songs.
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   title:
 *                     type: string
 *                     description: The song name.
 *                     example: Feel This Moment
 *                   genre:
 *                     type: string
 *                     description: The song's genre.
 *                     example: Dance pop
 *                   artists:
 *                     type: array
 *                     description: List of artists.
 *                     items:
 *                       type: string
 *                       description: artist 1
 *                       example: Pitbull 
 */
router.get('/api/parser/json', (req, res) => {
    res.json(fromJson('../../file_formats/res/data.json'))
})

/**
 * @openapi
 * /api/parser/csv:
 *   get:
 *     summary: To be implemented.. 
 */
router.get('/api/parser/csv', (req, res) => {
    res.send('To be implemented...')
})

/**
 * @openapi
 * /api/parser/xml:
 *   get:
 *     summary: To be implemented.. 
 */
router.get('/api/parser/xml', (req, res) => {
    res.send('To be implemented...')
})

/**
 * @openapi
 * /api/parser/yaml:
 *   get:
 *     summary: To be implemented.. 
 */
router.get('/api/parser/yaml', (req, res) => {
    res.send('To be implemented...')
})

export default router