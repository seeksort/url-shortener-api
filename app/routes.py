from app import urlapp
from flask import jsonify, request
import re

def send_err():
    error = {
        'error': 'Wrong url format, make sure you have a valid protocol and real site.'
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


def db_find_url(url):
    pass

def shorten_url(url):
    pass

'''
============ Routes ============
'''
@urlapp.errorhandler(404)
def bad_url(error):
    print(error)
    return send_err()

@urlapp.route('/')
def root():
    print('root')
    return "Welcome to url shortener!"

# Note: in "http://" it gets confused after the "//" so it returns two variables
@urlapp.route('/new/<url_protocol>//<url_parts>')
def handle_url(url_protocol, url_parts):
    validated = validate_url(url_protocol, url_parts)
    if validated == False:
        return send_err()
    else:
        print('validated!')
        # new_url = shorten_url(url_protocol)
        json = {
            'validated': True
            # 'original_url': url_protocol,
            # 'short_url': new_url
            }
        return jsonify(json)
