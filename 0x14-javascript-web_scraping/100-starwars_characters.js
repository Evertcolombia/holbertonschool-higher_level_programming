#!/usr/bin/node

const request = require('request');
const filmsUrl = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

console.log(filmsUrl)
function doRequest (url) {
  setTimeout(() => {	
    request(url, (error, response, body) => {
      if (error) return console.log('error', error);
      const data = JSON.parse(body);
      console.log(data);
      return data;
    });
  }, 3000);
}


let data = doRequest(filmsUrl);
console.log(data)
