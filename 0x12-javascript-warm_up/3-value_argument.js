#!/usr/bin/node
if (process.argv[2] === undefined) { // No arguments
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
