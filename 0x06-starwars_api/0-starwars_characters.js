#!/usr/bin/node

const request = require('request');

async function fetchData (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function main () {
  const movieNumber = parseInt(process.argv[2]);
  const movieUrl = 'https://swapi-api.alx-tools.com/api/films';
  const data = await fetchData(movieUrl);

  const movie = data.results[movieNumber - 1];

  for (const character of movie.characters) {
    const person = await fetchData(character);
    console.log(person.name);
  }
}

main();
