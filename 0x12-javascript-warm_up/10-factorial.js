#!/usr/bin/node

function factorial (num) {
  if (!num) {
    console.log(1);
    return (0);
  }
  else{
    return (num * factorial(num - 1));
  }
}

factorial(process.argv[2]);
