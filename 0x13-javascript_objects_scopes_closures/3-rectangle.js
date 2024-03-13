#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return null;
    } else if (w === undefined || h === undefined) {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let res = 'X';
      for (let j = 1; j < this.width; j++) {
        res += 'X';
      }
      console.log(res);
    }
  }
}
module.exports = Rectangle;
