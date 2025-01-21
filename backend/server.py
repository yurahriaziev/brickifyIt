from config import app
from flask import jsonify, request

import os

@app.route('/server-test', methods=['POST'])
def server_test():
    return jsonify({'message':'Server OK'})

if __name__ == "__main__":
    app.run(debug=True)