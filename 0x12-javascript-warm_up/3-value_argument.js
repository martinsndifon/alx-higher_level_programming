#!/usr/bin/node

const args = process.argv;
const len = process.argv.length;

if (len === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
