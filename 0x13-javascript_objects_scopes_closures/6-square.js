#!/usr/bin/node
const SquareAlpha = require('./5-square');

class Square extends SquareAlpha {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let out = c;
      for (let j = 1; j < this.width; j++) {
        out += c;
      }
      console.log(out);
    }
  }
}

module.exports = Square;
