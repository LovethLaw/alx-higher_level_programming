#!/usr/bin/node
const cmdLineArgv = process.argv[2];

if (cmdLineArgv === undefined) {
  console.log('No argument');
} else {
  console.log(cmdLineArgv);
}
