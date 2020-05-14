#!/usr/bin/node

const base64 = require('base-64');
const request = require('request');
const utf8 = require('utf8');

const bearerToken = `${process.argv[2]}:${process.argv[3]}`;
const BToken = base64.encode(utf8.encode(bearerToken));

async function doRequest (options) {
  return new Promise((resolve, reject) => {
    request(options, (err, res) => {
      err ? reject(err) : resolve(res);
    });
  });
}

async function getTweets (string, accessToken) {
  const options = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    method: 'GET',
    auth: {
      bearer: accessToken
    },
    qs: { q: string, result_type: 'recent', count: 5 }
  };

  const res = await doRequest(options);
  return JSON.parse(res.body);
}

async function bearer () {
  const options = {
    url: 'https://api.twitter.com/oauth2/token',
    method: 'POST',
    Authorization: `Basic ${BToken}`,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    auth: {
      user: process.argv[2],
      pass: process.argv[3]
    },
    form: {
      grant_type: 'client_credentials'
    }
  };

  const res = await doRequest(options);
  return JSON.parse(res.body).access_token;
}

function showTweets (data) {
  const elem = data.statuses;
  for (const x in elem) {
    const st = `[${elem[x].id}] ${elem[x].text} by ${elem[x].user.name}`;
    console.log(st);
  }
}

(async () => {
  let accessT = '';
  const stSearch = process.argv[4];

  try {
    accessT = await bearer();
    try {
      const tweets = await getTweets(stSearch, accessT);
      showTweets(tweets);
    } catch (e) {
      return console.error(e);
    }
  } catch (e) {
    return console.error(`Could not generate a Bearer token. Please check that your credentials are correct and that the Filtered Stream preview is enabled in your Labs dashboard. (${e})`);
  }
})();
