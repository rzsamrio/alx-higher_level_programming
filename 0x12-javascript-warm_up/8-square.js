#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(size); i++) {
    let disp = 'X';
    for (let j = 1; j < Number(size); j++) {
      disp += 'X';
    }
    console.log(disp);
  }
}
