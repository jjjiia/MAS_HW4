from flask import Flask
app = Flask(__name__)
from flask import Markup
from flask import request


@app.route('/')
def hello_world():
    return Markup('<strong>Hello %s!</strong>')


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'



if __name__ == '__main__':
    app.run()
	##app.run(host='0.0.0.0')