#!/usr/bin/node

const args = process.argv;
const len = process.argv.length;

if (len === 2 || isNaN(args[2])) {
  console.log('Missing size');
} else {
  const num = +args[2];

  for (let i = 0; i < num; i++) {
    let str = '';
    for (let j = 0; j < num; j++) {
      str = str + 'X';
    }
    console.log(str);
  }
}
