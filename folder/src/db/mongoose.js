const mongoose = require('mongoose')

mongoose.connect('mongodb://localhost:27017/task',{
    useNewUrlParser: true,
    useCreateIndex:true
})





/* const myTask = new Task({
    description:"     design monitering API    ",
    
})
myTask.save().then((my)=>{
    console.log(my)
}).catch((error)=>{
    console.log(error)
})  */