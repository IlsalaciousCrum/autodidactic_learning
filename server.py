from flask import Flask, render_template, jsonify

from programs.runtime import runtime_flashcards, flashcard_ajax

import os

from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = os.environ['APP_SECRET_KEY']

app.jinja_env.undefined = StrictUndefined

 # ___________________________________


@app.route('/hello')
def say_hello():
    """The landing page for this series of learning exercises"""

    html = "<html><body>This is where I work on learning</body></html>"
    return html


@app.route('/runtime')
def runtime():
    """Flashcards for learning runtime"""

    flashcard = runtime_flashcards()

    return render_template("runtime.html", flashcard=flashcard)


@app.route('/runtime.json')
def refresh_runtime():
    """Returns a new flashcard"""

    flashcard = flashcard_ajax()

    return jsonify(flashcard)

#  ____________________________________

if __name__ == "__main__":

    DEBUG = "NO_DEBUG" not in os.environ

    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
