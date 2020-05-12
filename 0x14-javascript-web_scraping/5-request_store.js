#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2].concat('/').concat(process.argv[3]);

function write (filename, string) {
  fs.writeFile(filename, string, 'utf8', (err, data) => {
    if (err) return console.log(err);
  });
}
function doRequest () {
  request(url, (error, response, body) => {
    if (error) return console.log('error', error);
    write(process.argv[3], body);
  });
}

doRequest();
