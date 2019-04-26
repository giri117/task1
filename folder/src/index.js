const express = require('express') //require means import module
require('./db/mongoose')
const app = express()//express ia a class. in this step we have created a object
const taskRouter = require('./routers/task')
const port = process.env.PORT || 2019
app.use(express.json())// methods inside the express class
app.use(taskRouter)
app.listen(port,()=>{
    console.log('server on port %s',port)

}) 

