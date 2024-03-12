#!/usr/bin/node

const n = Number(process.argv[2]);
console.log(factorial(n));

function factorial (num) {
  if (isNaN(num)) {
    return (1);
  }

  if (num === 0) {
    return (1);
  }

  return (num * factorial(num - 1));
}
