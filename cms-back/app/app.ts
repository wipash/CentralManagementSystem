import express = require('express');

// Create a new express application instance
const app: express.Application = express();

let port = process.env.PORT || 3000;

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.listen(port, function () {
  console.log("Listening on " + port);
});
