from app import urlapp, db
from flask import jsonify, request, redirect, render_template
from app.models import UrlMap
import re

wrong_url_err = {
    'error': 'Wrong url format, make sure you have a valid protocol and real site.'
    }

bad_short_url_err = {
    'error': 'This url is not in the database.'
    }

def send_err(error):
    return jsonify(error), 404

def validate_url(url_protocol, url_parts):
    # url should have http:// or http://
    if (url_protocol != 'http:') and (url_protocol != 'https:'):
        return False
    # url should have at least one "dot"
    else:
        regex = re.compile(r'(\.).')
        match = re.search(regex, url_parts)
        if match:
            return True
        else:
            return False

def find_url(url_search):
    return db.session.query(UrlMap).filter(url_search).first()

def shorten_url(url):
    # lookup last in db
    last_url = UrlMap.query.order_by(UrlMap.id.desc()).first()
    # add +1 to url id if exist in db, start at 1000 if not
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
    return send_err(wrong_url_err)

@urlapp.route('/')
def root():
    return render_template('index.html')

@urlapp.route('/<short_url>/')
def handle_short_url(short_url):
    url_search = UrlMap.short_url_id == short_url
    url_in_db = find_url(url_search)
    if url_in_db == None:
        return send_err(bad_short_url_err)
    else:
        return redirect(url_in_db.original_url, 301)

# Note: in "http://" it gets confused after the "//" so it returns two variables
@urlapp.route('/new/<url_protocol>//<url_parts>/')
def handle_url(url_protocol, url_parts):
    validated = validate_url(url_protocol, url_parts)
    if validated == False:
        return send_err(wrong_url_err)
    else:
        full_url = url_protocol + '//' + url_parts
        url_search = UrlMap.url_no_protocol == url_parts
        url_in_db = find_url(url_search)
        if url_in_db == None:
            # create new url & add to db
            short_url = shorten_url(url_parts)
            url = UrlMap(original_url=full_url, url_no_protocol=url_parts, short_url_id=short_url)
            db.session.add(url)
            db.session.commit()
            # compose url to return w/ new shortened_url
            json = {
                'original_url': full_url,
                'short_url': str(request.url_root) + str(short_url)
                }
        else:
            json = {
                'original_url': full_url,
                'short_url': str(request.url_root) + str(url_in_db.short_url_id)
                }
        return jsonify(json)
