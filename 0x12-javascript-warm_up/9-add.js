#!/usr/bin/node

const args = process.argv;

a = +args[2];
b = +args[3];

add(a , b);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
