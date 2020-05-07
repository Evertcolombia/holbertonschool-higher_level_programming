#!/usr/bin/node

function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  console.log(result);
}

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  add(process.argv[2], process.argv[3]);
}
