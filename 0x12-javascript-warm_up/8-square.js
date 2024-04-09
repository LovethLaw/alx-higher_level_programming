#!/usr/bin/node
const cmdLineArgv = process.argv[2];
const converted = Number(cmdLineArgv);

if (cmdLineArgv === undefined || isNaN(converted)) {
  console.log('Missing size');
} else {
  let i, j;
  let result = '';
  for (i = 0; i < converted; i++) {
    for (j = 0; j < converted; j++) {
      result += 'X';
    }
    console.log(result);
    result = '';
  }
}
