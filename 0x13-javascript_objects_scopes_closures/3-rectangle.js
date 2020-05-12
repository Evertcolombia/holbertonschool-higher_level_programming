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

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
