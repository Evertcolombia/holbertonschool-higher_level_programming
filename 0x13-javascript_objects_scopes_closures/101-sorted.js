#!/usr/bin/node

const dict = require('./101-data').dict;
const values = Object.values(dict);
const keys = Object.keys(dict);
const newDict = {};

values.map(value => {
  newDict[value] = keys.filter(key => dict[key] === value);
});

console.log(newDict);
