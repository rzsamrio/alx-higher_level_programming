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
}
module.exports = Rectangle;
