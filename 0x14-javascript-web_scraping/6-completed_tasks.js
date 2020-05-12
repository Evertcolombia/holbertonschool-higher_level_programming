#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) return console.log('error', error);
  const data = JSON.parse(body);
  const results = Object();

  for (const x in data) {
    if (data[x].completed) {
      if (results.hasOwnProperty(data[x].userId)) {
        results[data[x].userId] += 1;
      } else {
        results[data[x].userId] = 1;
      }
    }
  }
  console.log(results);
});
