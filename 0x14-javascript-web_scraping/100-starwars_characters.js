#!/usr/bin/node

const request = require('request');
const filmsUrl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(filmsUrl, (error, response, body) => {
  if (error) return console.log('error', error);
  const data = JSON.parse(body).characters;

  for (const x in data) {
    request(data[x], (error, response, body) => {
      if (error) return console.log('error', error);
      const character = JSON.parse(body).name;
      console.log(character);
    });
  }
});
