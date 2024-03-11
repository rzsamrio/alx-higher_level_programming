#!/usr/bin/node
if (process.argv.length < 3) { // No arguments
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
