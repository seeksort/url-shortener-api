from app import urlapp
from flask import jsonify, request

@urlapp.route('/')
def root():
    return "Welcome"
