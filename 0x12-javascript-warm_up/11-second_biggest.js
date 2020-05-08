#!/usr/bin/node

const length = process.argv.length;

if (length < 3) {
  console.log(0);
} else if (length === 3) {
  console.log(0);
} else {
  let sor = [];
  for (let i = 2; i < length; i++) {
    sor.push(parseInt(process.argv[i]));
  }

  sor = sor.sort((a, b) => {
    return (a - b);
  });

  const len = sor.length;
  console.log(sor[len - 2]);
}
