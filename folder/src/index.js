const express = require('express')
require('./db/mongoose')
const logger = require('morgan')
const  fs =require('fs')
const app = express()
app.use(logger('common', {
    stream: fs.createWriteStream('./access.log', {flags: 'a'})
}))
app.use(logger('dev'));
const taskRouter = require('./routers/task')
const port = process.env.PORT || 2019
app.use(express.json())
app.use(taskRouter)
app.listen(port,()=>{
    console.log('server on port %s',port)

}) 

