#!/usr/bin/node

const argNum = process.argv[2];

if (!argNum) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argNum; i++) {
    console.log('C is fun');
  }
}
