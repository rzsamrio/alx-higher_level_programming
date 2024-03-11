#!/usr/bin/node
if (process.argv.length < 3) { // No arguments
  console.log('No argument');
} else if (process.argv.length < 4) { // 1 true argument
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
