const express = require('express');

const app = express();
const countStudents = require('./3-read_file_async');

app.get('/', (req, res) => {
  res.type('text');
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  res.type('text');
  const path = process.argv[2];
  let output = '';
  const originalLog = console.log;
  console.log = (msg) => { output += `${msg}\n`; };
  try {
    await countStudents(path);
    output = output.trimEnd();
    res.send(`This is the list of our students\n${output}`);
    return;
  } catch (err) {
    console.log = originalLog;
    res.send('This is the list of our students\nCannot load the database');
    return;
  } finally {
    console.log = originalLog;
  }
});
app.listen(1245);
module.exports = app;
