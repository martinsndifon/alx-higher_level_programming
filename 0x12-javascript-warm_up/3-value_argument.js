#!/usr/bin/env node

const process = require('node:process');

let args = process.argv;

if (args.length === 2) {
	console.log('No argument');
} else {
	console.log(args[2]);
}
