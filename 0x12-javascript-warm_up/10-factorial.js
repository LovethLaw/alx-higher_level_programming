#!/usr/bin/node
const num = Number(process.argv[2]);

function fact (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 1 || n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}
const result = fact(num);
console.log(result);
