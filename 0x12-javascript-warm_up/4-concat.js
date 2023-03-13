#!/usr/bin/env node

const process = require('node:process');

let args = process.argv;

console.log(`${args[2]} is ${args[3]}`);
