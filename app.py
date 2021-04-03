import oyaml as yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    # website_data = yaml.load(open('_config.yaml', encoding='UTF8'))

    return render_template('_index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
