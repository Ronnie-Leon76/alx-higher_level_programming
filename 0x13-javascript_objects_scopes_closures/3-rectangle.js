#!/usr/bin/node

/* Define a Rectangle class with constructor that takes 2 arguments w and h */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
}
module.exports = Rectangle;
