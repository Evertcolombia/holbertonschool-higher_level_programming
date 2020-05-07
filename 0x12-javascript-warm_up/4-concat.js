#!/usr/bin/node

const prLength = process.argv.length;
const unde = 'undefined';

if (prLength < 3) {
  console.log(`${unde} is ${unde}`);
} else if (prLength === 3) {
  console.log(`${process.argv[2]} is ${unde}`);
} else {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
}
