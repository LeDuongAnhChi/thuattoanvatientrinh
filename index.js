const express = require('express')
const app = express()
var bodyParser = require('body-parser')
const { spawn } = require('child_process');
const port = 3000

// set the view engine to ejs
app.set('view engine', 'ejs');
app.set("views", "./views");
// create application/json parser
var jsonParser = bodyParser.json()
 
// create application/x-www-form-urlencoded parser
var urlencodedParser = bodyParser.urlencoded({ extended: false })


app.get('/search',(req,res)=>{
    console.log(req.query)
})
app.get('/', (req, res) => {
  res.render("index1")
})
app.post('/python', urlencodedParser,(req, res) => {
    console.log(req.body.lname)
    
    const childPython = spawn('python', ['kata.py',req.body.fname,req.body.lname]);
childPython.stdout.on('data', (data) => {
    // var temp = JSON.parse(data.toString());
    res.render("index",{data:data})
    // console.log(data.toString());
  });
  childPython.stderr.on('data', (data) => {
        
    console.error(data.toString());
  });
  childPython.on('exit', (code) => {
    console.log(`Child exited with code ${code}`);
  });
  
  })
// app.get('/vui',(req,res)=>{
//     res.render("index",{name:"chan123"});
// })
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})