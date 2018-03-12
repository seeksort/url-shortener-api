from app import urlapp, db
from flask import jsonify, request, redirect
from app.models import UrlMap
import re

def send_err():
    error = {
        'error': 'Wrong url format, make sure you have a valid protocol and real site.'
        }
    return jsonify(error)

def send_bad_short_url_err():
    error = {
        'error': 'This url is not in the database.'
        }
    return jsonify(error)

def validate_url(url_protocol, url_parts):
    # url should have http:// or http://
    if (url_protocol != 'http:') and (url_protocol != 'https:'):
        return False
    # url should have at least one "dot"
    else:
        regex = re.compile('(\.).')
        match = re.search(regex, url_parts)
        # return bool if valid/invalid
        if match:
            return True
        else:
            return False


def db_find_url(url_parts):
    return db.session.query(UrlMap).filter(UrlMap.url_no_protocol == url_parts).first()

def db_find_short_url(short_url):
    return db.session.query(UrlMap).filter(UrlMap.short_url_id == short_url).first()

def shorten_url(url):
    # lookup last in db
    last_url = UrlMap.query.order_by(UrlMap.id.desc()).first()
    print(last_url)
    # add +1 to url id if exist in db
    if last_url == None:
        short_url = 1000
    else:
        short_url = last_url.short_url_id + 1
    return short_url

'''
============ Routes ============
'''
@urlapp.errorhandler(404)
def bad_url(error):
    print(error)
    return send_err()

@urlapp.route('/')
def root():
    return "Welcome to url shortener!"

@urlapp.route('/<short_url>')
def handle_short_url(short_url):
    url_in_db = db_find_short_url(short_url)
    if url_in_db == None:
        return send_bad_short_url_err()
    else:
        return redirect(url_in_db.original_url, 302)

# Note: in "http://" it gets confused after the "//" so it returns two variables
@urlapp.route('/new/<url_protocol>//<url_parts>')
def handle_url(url_protocol, url_parts):
    validated = validate_url(url_protocol, url_parts)
    if validated == False:
        return send_err()
    else:
        print('validated!')
        full_url = url_protocol + '//' + url_parts
        # url_in_db = UrlMap.find_url(url_parts)
        url_in_db = db_find_url(url_parts)
        print('url_in_db')
        print(url_in_db)
        if url_in_db == None:
            # create new url
            short_url = shorten_url(url_parts)
            url = UrlMap(original_url=full_url, url_no_protocol=url_parts, short_url_id=short_url)
            # add url to db
            db.session.add(url)
            db.session.commit()
            # compose url to return w/ new shortened_url
            json = {
                'original_url': full_url,
                'short_url': short_url
                }
        else:
            # return existing url from db
            json = {
                'original_url': full_url,
                'short_url': str(request.url_root) + str(url_in_db.short_url_id)
                }
        return jsonify(json)
