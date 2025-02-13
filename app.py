import oyaml as yaml
from flask import Flask
from flask import render_template
from flask import send_from_directory
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    # website_data = yaml.load(open('_config.yaml', encoding='UTF8'))

    return render_template('_index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=False, port=8080)
