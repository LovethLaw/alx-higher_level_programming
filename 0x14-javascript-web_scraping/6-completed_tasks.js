#!/usr/bin/node

const res = require('request');
const url = process.argv[2];

res.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);

  const obj = {};

  tasks.forEach(element => {
    if (!(element.userId in obj)) {
      obj[element.userId] = 0;
    }
  });

  tasks.forEach(element => {
    if (element.completed === true) {
      obj[element.userId] += 1;
    }
  });
  console.log(obj);
});
