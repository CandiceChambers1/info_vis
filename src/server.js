// server.js
const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
const port = 3000;
app.use(express.static('public'));
// Parse JSON bodies
app.use(bodyParser.json());

// Handle POST requests to /process endpoint
app.post('/process', (req, res) => {
    const inputData = req.body.text;
//    console.log(inputData)
    // Spawn a Python process
    const pythonProcess = spawn('python', ['noun_extracter.py', inputData]);

    let outputData = '';

    // Capture stdout data from Python process
    pythonProcess.stdout.on('data', (data) => {
        outputData += data.toString();
        outputData += '\n\n';

    });
    console.log(outputData)

    // When Python process ends
    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
        // Send output back to client
        res.send({ output: outputData });

    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
