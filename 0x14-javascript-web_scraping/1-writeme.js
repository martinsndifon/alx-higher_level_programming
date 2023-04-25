#!/usr/bin/node
// writes a string to a file

const fs = require('fs');
const process = require('process');

const path = process.argv[2];
const string = process.argv[3];
fs.writeFile(path, string, 'utf8', (err) => {
  if (err) console.log(err);
});
