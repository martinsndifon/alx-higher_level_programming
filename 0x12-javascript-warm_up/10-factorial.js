#!/usr/bin/env node

const args = process.argv;
const num = +args[2];

if (!args[2]) {
  console.log(1);
  return;
}

function factorial (n) {
  if (n < 0) {
    return (-1);
  }

  if (n === 0) {
    return (1);
  }

  return (n * factorial(n - 1));
}
console.log(factorial(num));
