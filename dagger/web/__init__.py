from flask import Flask

app = Flask(__name__)

from dagger.web import routes
