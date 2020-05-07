#!/usr/bin/node

const arLength = process.argv.length;

if (arLength < 3) {
  console.log('No argument');
} else if (arLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
