#!/usr/bin/node

function factorial (num) {
  if (!process.argv[2]) {
    return (1);
  }
  else{
    let num = process.argv[2]
    return (num * factorial(num))
  }
}
