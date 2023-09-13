#!/usr/bin/node

/* Define a Square class with constructor that takes 1 argument: size */

class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
