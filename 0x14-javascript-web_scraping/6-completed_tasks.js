#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
const url = link + id
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  const name = characters.map(
    lnk => new Promise((resolve, reject) => {
      request(lnk, (err, response, body) => {
        if (err) {
          reject(err);
        }
        const info = JSON.parse(body);
        resolve(info.name);
      });
    }));
  Promise.all(name)
    .then(names => console.log(names.join('\n')))
    .catch(x => console.log(err));
});#!/usr/bin/node
