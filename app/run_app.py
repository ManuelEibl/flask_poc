from flask import Flask

from some_utils import my_helper_func

# Init App
app = Flask(__name__)

# Get a specific product
@app.route('/hello', methods=['GET'])
def get_product():

    return my_helper_func()

# Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)