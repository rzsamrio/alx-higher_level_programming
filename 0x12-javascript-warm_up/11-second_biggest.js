#!/usr/bin/node

let max = 0; let smax = 0;

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const num = Number(process.argv[i]);
    if (max < num) {
      smax = max;
      max = num;
      continue;
    }
    if (smax < num) {
      smax = num;
    }
  }
  console.log(smax);
}
