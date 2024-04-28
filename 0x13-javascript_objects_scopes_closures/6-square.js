#!/usr/bin/node
const SquareAlpha = require('./5-square');

class Square extends SquareAlpha {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let out = c;
      for (let j = 1; j < this.size; j++) {
        out += c;
      }
      console.log(out);
    }
  }
}

module.exports = Square;
