#!/usr/bin/node
// writes a string to a file

const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const newurl = JSON.parse(body).results[0].characters[15];
    request(`${newurl}`, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        const films = JSON.parse(body).films;
        console.log(films.length);
      }
    });
  }
});
