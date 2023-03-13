#!/usr/bin/node

const args = process.argv;
const len = process.argv.length;
const arr = [];

for (let i = 2; i < len; i++) {
  arr.push(args[i]);
}

if (len === 2) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  arr.sort(compareFn);
  console.log(+arr[1]);
}

function compareFn (a, b) {
  return b - a;
}
