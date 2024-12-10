const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Email configuration
const transporter = nodemailer.createTransport({
    service: 'gmail', // Or use your preferred service
    auth: {
        user: 'your-email@gmail.com',
        pass: 'your-email-password',
    },
});

// Endpoint to send email
app.post('/send-email', (req, res) => {
    const { csvData } = req.body;

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: 'recipient-email@gmail.com',
        subject: 'Daily SAC Report',
        text: 'Please find the attached report.',
        attachments: [
            {
                filename: 'SAC_Report.csv',
                content: csvData,
            },
        ],
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            return res.status(500).send({ success: false, error });
        }
        res.send({ success: true });
    });
});

app.listen(3000, () => console.log('Server is running on port 3000'));
