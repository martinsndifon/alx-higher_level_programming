#!/usr/bin/node

const args = process.argv;
const fs = require('fs');

const str1 = fs.readFileSync(args[2], 'utf8');

const str2 = fs.readFileSync(args[3], 'utf8');

const str3 = str1 + str2;

fs.writeFile(args[4], str3, (err) => {
  if (err) throw err;
});
