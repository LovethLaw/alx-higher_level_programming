#!/usr/bin/node
const res = require('request');

res.get(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
