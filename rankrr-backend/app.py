from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config['JSON_SORT_KEYS'] = False

# route controllers
import controllers.ranker_controller
import controllers.text_analyzer_controller

if __name__ == '__main__':
    app.run(debug=True)

