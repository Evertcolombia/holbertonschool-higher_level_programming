#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) return console.log('error', error);
  const data = JSON.parse(body);
  const results = Object();

  for (const x in data) {
    if (data[x].completed) {
      const userId = data[x].userId;
      const isInResults = results.hasOwnProperty(userId);
      if (isInResults) {
        results[userId] += 1;
      } else {
        results[userId] = 1;
      }
    }
  }
  console.log(results);
});
