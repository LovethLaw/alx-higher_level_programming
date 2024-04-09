#!/usr/bin/node
const cmdLineArgv = process.argv[2];
const converted = Number(cmdLineArgv);

if (isNaN(converted)) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 1; i <= converted; i++) {
    console.log('C is fun');
  }
}
