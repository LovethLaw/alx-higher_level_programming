#!/usr/bin/node
const cmdLineArgv = process.argv[2];
const converted = Number(cmdLineArgv);
if (isNaN(converted)) {
  console.log('Not a number');
} else if (typeof converted === 'number') {
  console.log(`My number: ${converted}`);
}
