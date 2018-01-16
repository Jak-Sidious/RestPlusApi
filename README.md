[![Build Status](https://travis-ci.org/Jak-Sidious/RestPlusApi.svg?branch=Crud-Functionality-2)](https://travis-ci.org/Jak-Sidious/RestPlusApi)

[![Coverage Status](https://coveralls.io/repos/github/Jak-Sidious/FlaskAPI/badge.svg?branch=master)](https://coveralls.io/github/Jak-Sidious/FlaskAPI?branch=master)

[![Maintainability](https://api.codeclimate.com/v1/badges/c7422200c78aacd4c9eb/maintainability)](https://codeclimate.com/github/Jak-Sidious/RestPlusApi/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/c7422200c78aacd4c9eb/test_coverage)](https://codeclimate.com/github/Jak-Sidious/RestPlusApi/test_coverage)

# Project Title

This is an API for a Recipies Service using Flask. Users can register an account, loginin and from there perform certain functionality on the recipies

## Setup

To use this application ensure that you have python 3.6+ clone the repository to your local machine and execute the following commands

1. Clone the repository

   ```
   https://github.com/Jak-Sidious/RestPlusApi.git
   ```

2. Enter the project directory
   ```
   cd RestPlusApi
   ```
3. Create a virtual environment
   ```
   virtualenv venv
   ```
4. Activate the virtual environment
   ```
   source venv/bin/activate
   ```
5. Then install all the required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Install postgres if you don't already have it. Preferably Postgres 10.1.

7. Create the Databases

   #### For the test Database

   ```
   createdb testing_db
   ```

   #### For the development Database

   ```
   createdb yummy_db2
   ```

8. Run Migrations using these commands, in that order:

   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```

9. To test the application, run the command:

   ```
   pytest --cov-report term --cov=app
   ```

10. To start the server, run the command:

```
export FLASK_CONFIG=development
python manage.py runserver
```