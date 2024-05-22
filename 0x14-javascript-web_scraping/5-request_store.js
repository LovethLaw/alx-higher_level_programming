#!/usr/bin/node
const res = require('request');
const fs = require('fs');

const url = process.argv[2];
const resPath = process.argv[3];

res.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(resPath, body, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
