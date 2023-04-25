#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');
const process = require('process');

const path = process.argv[2];
fs.readFile(path, 'utf8', (err, data) => {
  if (err) console.log(err);
  else {
    console.log(data);
  }
});
