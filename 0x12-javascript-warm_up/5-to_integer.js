#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Not a Number');
} else {
  console.log(Number(process.argv[2]));
}
