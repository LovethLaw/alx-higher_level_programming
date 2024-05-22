#!/usr/bin/node

const res = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
res.get(url, (err, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const jsonBody = JSON.parse(body.body);
  console.log(jsonBody.title);
});
