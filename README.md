# Mail'em
Mail'em is a simple web application that provides email scheduling and analytics services. The application is built using Angular, Nebular, Flask, Python, TypeScript, SQLite, CSS, and HTML.

The application has two types of users: Admin and Normal users. Admin users can log in and see analytics of emails, i.e. the number of scheduled, sent, and opened emails. Normal users can sign up, log in, and schedule emails to be sent at particular times.

The database used is SQLite, which is easy to set up and use.

## Features
- User management (sign up)
- Authentication (login and logout)
- Email management
  - Schedule emails
  - Send emails
- Analytics (Admin api)
  - Check for the emails that are scheduled, sent and opened.

## Local Deployment

- ### Developed with :
  - Angular CLI: 15.2.2
     - https://www.npmjs.com/package/@angular/cli/v/15.2.2
  - Node 18.15.02
     - https://nodejs.org/download/release/v18.15.0/
  - npm 9.5.0
     - https://www.npmjs.com/package/npm/v/9.5.0
  - Python 3.9.1
     - https://www.python.org/downloads/release/python-391/
     
 - ### Steps to deploy :
      - Make sure everything mentioned above is already installed and setup. 
          - You can have different version than mine, but there is no guarantee project will work or not.
      - Clone the project on local machine
      - Open Terminal or Command Prompt
    - Frontend :
      - Go to project root
      - `cd frontend`
      - `npm install`
      - `ng build`
   - Backend :
      - Go to project root
      - `python -m pip install virtualenv`
      - `python -m venv venv`
      - `source venv/bin/activate` for Unix/macOS or `.\venv\Scripts\activate` for Windows
      - `pip install -r requirements.txt`
      - `python run.py`
      - It will run a server on `http://127.0.0.1:<port>` or `http://localhost:<port>`
        - Port mentioned in run.py. Other configurations present in config.py
        - Database used is SQLite which will automatically get setup on deployment
      - `python run_mail_scheduler.py`

## How To Use 
  - This app requires to add your email and password for email account in config.py file to be able to send the mails
    - Where?
      - In config.py root folder replace 
        - `MAIL_USERNAME = 'company.email.id'` with `MAIL_USERNAME = '<your-email-id>'`
        - `MAIL_PASSWORD = 'company.email.password'` with `MAIL_PASSWORD = 'your-email-password'`
    - For gmail users
      - Gmail doesn't allow to use the credentials directly due to security concern
      - You will need to get and use the app password, below are the steps
        - First turn on two factor authenticaion in the gmail account
        - Second go to https://myaccount.google.com/apppasswords and get the app password
      - Once you get the app password, just put that instead of your password in required configuration property
  - This app, when launched for the first time, creates an admin user with credentials :
     - username : `admin@admin.admin`
     - password : `admin`
   - With these credentials admin panel is accessible, from where you can check the analytics
   - For user panel, you can just signup and use those credentials to login
    - In user account when you schedule the mail, the mail will send after 8:00 am IST next day.
