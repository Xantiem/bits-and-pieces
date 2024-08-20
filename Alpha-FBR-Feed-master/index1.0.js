// Version: 1.0
// Last Updated: 28/11/18
// Created by Simon6468


/*
Created for the Alpha discord room:  https://discordapp.com/channels/517308464326901761
Display the in-game news feed on Fortnite Battle Royale
*/

// Known Bugs:

/*
- Delay when displaying some of the news articles
- Pings user with each feed
*/

console.log('Alpha FBR Feed running'); // Log that the bot has started

var httpRequest = require('https'); // HTTPS module for sending requests
var fs = require('fs'); // Module to read and write files
const Discord = require('discord.js'); // Module for interaction with Discord API

var request = httpRequest.request('https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game',

  function(res) {

    var json_chunks = []; // Store chunks of json file from buffer

    res.on('data', function(data) {

      json_chunks.push(data); // Push chunks to be stored

    });

    res.on('end', function() {

      var json = JSON.parse(Buffer.concat(json_chunks)); // Parse and join buffer chunks together

      var len; // number of articles

      const client = new Discord.Client(); // Create Discord client

      client.on('message', msg => {

          if (msg.content === '!help') { // If the user types !help (universal command)
            msg.reply('Type "!fbr news" to get the latest Fortnite news'); // Help section
          }

          else if (msg.content === '!fbr news') { // If the user types !fbr news

            for (len = 0; len < json['battleroyalenews']['news']['messages'].length; len ++ ) { // Determine the length of the news feed (3)
              // All messages formatted in bold using ** **
              msg.reply('**' + json['battleroyalenews']['news']['messages'][len]['title'] + '**'); // Reply with the news title
              msg.reply(json['battleroyalenews']['news']['messages'][len]['image']); // Reply with the news image
              msg.reply('**' + json['battleroyalenews']['news']['messages'][len]['body'] + '**'); // Reply with the news content
            }
          }
        });
      fs.readFile('token.txt', 'utf8', function(error, content) {  // Note:  No error checking for no file
        client.login(content); // Discord token (found in token.txt)
      });
    });
  });

request.end();  // Close the request to the Fortnite API
