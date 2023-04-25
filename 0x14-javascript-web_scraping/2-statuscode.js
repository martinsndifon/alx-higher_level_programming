#!/usr/bin/node
// writes a string to a file

const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) throw error;
  if (response.statusCode === 200) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
