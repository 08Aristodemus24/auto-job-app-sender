const node_mailer = require('nodemailer');
const { google } = require('googleapis');
const response = require('dotenv').config({path: './.env'});

// for reading the message template text files
const fs = require('fs');
const { parse } = require('csv-parse');


const CLIENT_ID = process.env['CLIENT_ID'];
const CLIENT_SECRET = process.env['CLIENT_SECRET'];
const REDIRECT_URI = process.env['REDIRECT_URI'];

// to be able to send emails programmatically
const REFRESH_TOKEN = process.env['REFRESH_TOKEN'];

// senders email
const EMAIL = process.env['SENDER_EMAIL'];

// set oauth2client
const oauth2client = new google.auth.OAuth2(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI);
oauth2client.setCredentials({refresh_token: REFRESH_TOKEN});



// define send mail function
const send_mail = async (email_adds) => {
    try{
        // retrieve access token first
        const access_token = await oauth2client.getAccessToken();
        // use this if accses token has expired only then can we use getAccessToken again to retrieve the newly generated access token
        // oauth2client.refreshAccessToken();
        
        console.log(access_token);

        // create transport to be able to send payload/content to email addresses
        const transport = node_mailer.createTransport({
            service: 'gmail',
            auth: {
                type: 'OAuth2',
                user: EMAIL,
                clientId: CLIENT_ID,
                clientSecret: CLIENT_SECRET,
                accessToken: access_token['token']
            }
        });

        // place loop here to build mail options
        const mail_options = {
            from: `Larry Miguel R. Cueva <${EMAIL}>`,
            to: email_adds,
            subject: 'test',
            test: 'this is the body of content',
            html: 'this is the body of content',
            attachments: [
                {
                    file: 'Cueva, Larry Miguel.pdf',
                    path: './documents/Cueva, Larry Miguel.pdf',
                    contentType: 'application/pdf'
                }
            ]
        };

        const result = await transport.sendMail(mail_options);
        return result;
    }catch(error){
        console.log(error)
    }
}



// here the this method from fs reads the .csv file
// in which here indicates that the reader should parse the file at line 2
// since we know that at line 1 is where the headers of the .csv file are
const read_csv_rw = () => {
    // initialize csv array
    const company_list = [];

    // since createReadStream is asynchronous we will have to wait and 
    // until it has executed fully, only then can company_list have values
    return new Promise((resolve) => {
        fs.createReadStream('./documents/company_list.csv')
        .pipe(parse({delimiter: ",", from_line: 2}))
        .on("data", (data) => {
            company_list.push(data);
        })
        .on("end", () => {
            console.log('successfully parsed .csv file resolving promise');
            resolve(company_list);
        })
        .on("error", (error) => console.log(`error ${error} has occured`));
    })
}

// this function is like the above however reads the .csv file column wise
const read_csv_cw = () => {
    // initialize csv array
    const company_list = [];

    // since createReadStream is asynchronous we will have to wait and 
    // until it has executed fully, only then can company_list have values
    return new Promise((resolve) => {
        fs.createReadStream('./documents/company_list.csv')
        .pipe(parse({delimiter: ",", from_line: 2}))
        .on("data", (data) => {
            company_list.push(data);
        })
        .on("end", () => {
            console.log('successfully parsed .csv file resolving promise');
            resolve(company_list);
        })
        .on("error", (error) => console.log(`error ${error} has occured`));
    })
}

const extract_data = async () => {
    const data = await read_csv();
    console.table(data);
}

extract_data();

// call async send_mail
// send_mail(['MichaelCueva5701@gmail.com']).then(result => console.log(`email ${result} successfully sent`)).catch(err => console.log(`error ${err} has occured`));
