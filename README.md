# url-shortener-api

(Python, Flask) A service that will shorten a long URL and redirect to the original site when given the short URL.

I wanted to try out Flask and Python in the backend, so I decided to do a little project that still uses some HTML and a small database. 

Flask is lightweight and reminds me of Express.js. Being familiar with what I can do with Express.js really made it easier for me to look for what I wanted to do in the Flask docs.

This is one of the [Free Code Camp API projects](https://www.freecodecamp.org/challenges/url-shortener-microservice).

## To run Flask version locally

This app will run Flask in a virtualenv, using SQLite as a database. 

From root folder (assuming you already have Python and virtualenv installed):

```
virtualenv venv
. venv/bin/activate
```


Install all dependencies:

```
pip install -r requirements.txt
```


Create the database and migration, then launch the app.

```
flask db init
flask db migrate -m "create urlmaps table"
flask db upgrade
export FLASK_APP=urlapp.py
flask run
```

Then navigate to `localhost:5000` in your browser and follow the instructions onscreen.

To stop server, press `Ctrl-D` (MacOS/Linux) or `Ctrl-Z` & `Enter` (Windows). Then, stop virtualenv with `deactivate`.