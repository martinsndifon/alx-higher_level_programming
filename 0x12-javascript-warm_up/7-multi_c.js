#!/usr/bin/node

const args = process.argv;
const len = process.argv.length;

if (len === 2 || isNaN(args[2])) {
  console.log('Missing number of occurences');
} else {
  const num = +args[2];
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
