#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);

let i = 0;
console.log(list.map(function (n) {
  n = n * i;
  i++;
  return n;
}));
