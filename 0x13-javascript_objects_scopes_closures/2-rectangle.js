#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w < 1 || !w) || (h < 1 || !h)) {
      Object();
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
