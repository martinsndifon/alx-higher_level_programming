#!/usr/bin/node
// writes a string to a file

const request = require('request');
const process = require('process');

const id = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
