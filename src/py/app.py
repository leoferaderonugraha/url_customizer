from flask import Flask
from .web import web as web_blueprint


app = Flask(__name__, template_folder='../html/')
app.secret_key = 'somesecretkeyplschange'

app.register_blueprint(web_blueprint, url_prefix='/')


if __name__ == '__main__':
    app.run()
