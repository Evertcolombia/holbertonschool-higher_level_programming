#!/usr/bin/node

const request = require('request');
const filmsUrl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
let count = 0;

request(filmsUrl, (error, response, body) => {
  if (error) return console.log('error', error);
  const data = JSON.parse(body).characters;
  const characters = {};

  for (const x in data) {
    request(data[x], (error, response, body) => {
      if (error) return console.log('error', error);
      characters[x] = JSON.parse(body).name;
      count++;

      if (count === data.length) {
        for (const v in characters) {
          console.log(characters[v]);
        }
      }
    });
  }
});
