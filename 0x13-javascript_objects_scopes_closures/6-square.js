#!/usr/bin/node
const oldSquare = require('./5-square');

module.exports = class Square extends oldSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str = str + c;
        }
        console.log(str);
      }
    }
  }
};
