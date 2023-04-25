#!/usr/bin/node
// writes a string to a file

const request = require('request');
const process = require('process');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  let data = JSON.parse(body).results;
  data = data.filter(({ characters }) => characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  console.log(data.length);
});
