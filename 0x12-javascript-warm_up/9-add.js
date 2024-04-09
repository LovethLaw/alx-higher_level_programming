#!/usr/bin/node
const cmdLineArgv = Number(process.argv[2]);
const cmdLineArgv2 = Number(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(cmdLineArgv, cmdLineArgv2);
