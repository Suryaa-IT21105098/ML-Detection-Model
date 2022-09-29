# For receiving POST request

from flask import Flask, jsonify, request
import requests
from file_checker import main
from time import sleep

# Initiating the Node
app = Flask(__name__)


@app.route('/check', methods=['POST'])
def check():
    if request.files.get('file', 0):
        f = request.files['file']
#         print(f)
        f.save('malwares/tempFile')
    elif request.form.get('link', 0):
        l = request.form['link']
#         print(l)
    else:
        response = {'Invalid Response': 'Bad request'}
        return jsonify(response), 400
    
    legitimate = main('malwares/tempFile')
    response = {
        'legitimate': bool(legitimate)
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run()
