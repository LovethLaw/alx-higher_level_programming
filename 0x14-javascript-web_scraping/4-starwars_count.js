#!/usr/bin/node
const res = require('request');
const movieId = process.argv[3];
const url = process.argv[2] + '/' + movieId;
const characterId = 18;

res.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const characterUrl = JSON.parse(body).characters.filter(x => x.includes(characterId))[0];

  res.get(characterUrl, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }

    const filmLength = JSON.parse(body).films.length;
    console.log(filmLength);
  });
});
