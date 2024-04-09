#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  charPrint (value) {
    if (arguments.length === 0) {
      value = 'x';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(value.repeat(this.height));
    }
  }
}

module.exports = Square;
