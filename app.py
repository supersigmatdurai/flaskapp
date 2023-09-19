from flask import Flask


app= Flask(__name__)


@app.route('/')
def home():
    return "Helllo world This is from flask"

if __name__ == '__main__':
    app.run()