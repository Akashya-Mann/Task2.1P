const express = require('express');
const bodyParser = require('body-parser');
const sgMail = require('@sendgrid/mail');

const app = express();
const PORT = process.env.PORT || 3000;

sgMail.setApiKey('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');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html');
});

app.post('/subscribe', (req, res) => {
  const email = req.body.email;

  const msg = {
    to: email,
    from: 'akmcanda@gmail.com',
    subject: 'Welcome NEW CUSTOMER to DEV@Deakin!!',
    text: 'Thanks you for subscribing to DEV@Deakin',
    html: '<strong>Thank you for subscribing to DEV@Deakin</strong>',
  };

  sgMail.send(msg);
  console.log('Email sent');
  res.send('<h2>Thank you!!! Ive sent u a email pls check</h2>');
});

app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
