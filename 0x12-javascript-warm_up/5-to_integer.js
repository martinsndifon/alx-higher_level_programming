#!/usr/bin/node

const args = process.argv;
const len = process.argv.length;

if (len === 2) {
  console.log('Not a number');
} else {
  if (isNaN(args[2])) {
    console.log('Not a number');
  } else {
    const num = parseInt(args[2]);
    console.log(`My number: ${num}`);
  }
}
