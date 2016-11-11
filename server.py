from Flask import Flask

import os

app = Flask(__name__)

app.secret_key = os.environ['APP_SECRET_KEY']

 # ___________________________________


@app.route('/hello')
def say_hello():
    html = "<html><body>This is where I work on learning</body></html>"
    return html


#  ____________________________________

if __name__ == "__main__":

    app.debug = True

    DEBUG = "NO_DEBUG" not in os.environ

    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT)
