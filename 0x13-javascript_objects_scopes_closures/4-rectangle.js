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

  rotate () {
    this.width = this.width ^ this.height;
    this.height = this.width ^ this.height;
    this.width = this.width ^ this.height;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
