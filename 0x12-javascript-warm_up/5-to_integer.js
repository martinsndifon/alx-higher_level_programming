#!/usr/bin/node

const process = require('node:process');

const args = process.argv;

if (args.length === 2) {
  console.log('Not a number');
} else {
  if (isNaN(args[2])) {
    console.log('Not a number');
  } else {
    const num = parseInt(args[2]);
    console.log(`My number: ${num}`);
  }
}
