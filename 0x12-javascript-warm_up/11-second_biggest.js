#!/usr/bin/node

const length = process.argv.length;

if (length > 3) {
  let sort = [];
  for (let i = 2; i < length; i++) {
    sort.push(process.argv[i]);
  }
  sort = sort.sort();
  const len = sort.length;
  console.log(sort[len - 2]);
}
