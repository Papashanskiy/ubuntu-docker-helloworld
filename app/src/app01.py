from flask import Flask

hello = Flask(__name__)

@hello.route('/')
def greating():
    return "<h1>Hello world!</h1>"


if __name__ == '__main__':
    hello.run(host='0.0.0.0')