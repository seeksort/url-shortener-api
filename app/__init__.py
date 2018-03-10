from flask import Flask

urlapp = Flask(__name__)

from app import routes
