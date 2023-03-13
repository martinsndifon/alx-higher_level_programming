#!/usr/bin/env node

const process = require('node:process');

let args = process.argv;

if (args.length === 2) {
	console.log('Not a number');
} else {
	if (isNaN(args[2])) {
		console.log('Not a number');
	} else {
		let num = parseInt(args[2]);
		console.log(`My number: ${num}`);
	}
}
