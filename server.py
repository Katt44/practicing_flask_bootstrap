from flask import Flask, request, session, redirect
import jinja2

app = Flask(__name__)
app.secret_key = 'this-should-be-something-unguessable'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def homepge():
    """Return homepage"""
    return render_template("homepage.html")




if __name__ == '__main__':
    app.run(debug=True)