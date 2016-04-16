/*Load the Twit and Fs packages*/
var Twit = require('twit');
var fs = require('fs');

var JsFile;

var tweets;

/*Access the Twitter API*/
var T = new Twit ({
    consumer_key: '2iYILmQvHq1wCfaepfBPP6HUJ',
    consumer_secret: 'F9zQZknsFx12vq1r4rMXvpo5xvifGWuXzX3NXe1tRzO0S4K4ym',
    access_token: '715700662324097024-wkwOAsag1tOgA1CVZGpHCNbSDrjpstu',
    access_token_secret: 'RJ8FvdF4pVJ3xWJhRNNjoskPIOIQLdpqqC4sVZTXdj4Rq'

})

/*Set the search parameters: search for words women AND (abortion OR slut OR queer OR sexism), search for
geotagged Tweets within the United States, retrieve 100 tweets
 */

var parameters = {
    q: 'women abortion OR slut OR queer OR sexism -RT',
    count: 100,
    include_entities: true,
    geocode:'39.8,-95.583068847656,2500km'

};

/*
Use the Twit package to search the tweets according to the parameters
and pass it to the function gotData
 */
T.get('search/tweets', parameters, gotData);

/*
Create function gotData to assign the returned JSON file from the
Twitter API search/statuses method and pass JSON file to generateFile function
 */
function gotData(err, data, response){
    tweets = data.statuses
    console.log(tweets)
    generateFile(tweets);
}

/*
Create generateFile function and stringify the objects in the
JSON file, then write to the Tweets_Geolocation.json file
 */

function generateFile(){
    var str = JSON.stringify(tweets)
    fs.writeFile("Tweets_Geolocation.json", str, function(err) {
        if(err) {
            return console.log(err);
        }

        console.log("The file was saved!");
    });

}





