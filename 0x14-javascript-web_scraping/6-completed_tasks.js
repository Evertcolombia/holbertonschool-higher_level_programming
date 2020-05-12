#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

function doTask (data, results) {
  for (const x in data) {
    if (data[x].completed) {
      const userId = data[x].userId;
      if (results.hasOwnProperty(userId)) {
        results[userId] += 1;
      } else {
        results[userId] = 1;
      }
    }
  }
  return results;
}

request(url, (error, response, body) => {
  if (error) return console.log('error', error);
  const data = JSON.parse(body);
  let results = Object();
  results = doTask(data, results);
  console.log(results);
});
