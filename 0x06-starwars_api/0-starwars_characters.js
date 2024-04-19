#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    
    for (const character of characters) {
      try {
        const characterBody = await getCharacter(character);
        console.log(characterBody.name);
      } catch (error) {
        console.error(error);
      }
    }
  }
});

async function getCharacter(character) {
  return new Promise((resolve, reject) => {
    request(character, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        if (response.statusCode === 200) {
          const characterBody = JSON.parse(body);
          resolve(characterBody);
        } else {
          reject(new Error('Request failed with status code: ' + response.statusCode));
        }
      }
    });
  });
}
