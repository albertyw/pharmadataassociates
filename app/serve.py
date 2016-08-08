import os

from flask import Flask, render_template, got_request_exception, redirect, url_for


import dotenv
root_path = os.path.dirname(os.path.realpath(__file__)) + '/../'
dotenv.read_dotenv(os.path.join(root_path, '.env'))
from getenv import env


app = Flask(__name__)
app.debug = env('DEBUG') == 'true'


if env('ENV') == 'production':
    import rollbar
    import rollbar.contrib.flask

    @app.before_first_request
    def init_rollbar():
        """init rollbar module"""
        rollbar.init(
            env('ROLLBAR_SERVER_TOKEN'),
            # environment name
            env('ENV'),
            # server root directory, makes tracebacks prettier
            root=os.path.dirname(os.path.realpath(__file__)),
            # flask already sets up logging
            allow_logging_basic_config=False)

        # send exceptions from `app` to rollbar, using flask's signal system.
        got_request_exception.connect(
            rollbar.contrib.flask.report_exception, app)


@app.context_processor
def inject_envs():
    envs = {}
    envs['ROLLBAR_CLIENT_TOKEN'] = env('ROLLBAR_CLIENT_TOKEN')
    envs['SEGMENT_TOKEN'] = env('SEGMENT_TOKEN')
    envs['ENV'] = env('ENV')
    return {'ENV': envs}


@app.route("/")
def index():
    return render_template("index.htm")


@app.route("/home")
def home():
    return redirect(url_for("index"))


@app.route("/AboutUs")
def about_us():
    return render_template("about_us.htm")


@app.route("/Capabilities")
def capabilities():
    return render_template("capabilities.htm")


@app.route("/Careers")
def careers():
    return render_template("careers.htm")


@app.route("/CaseStudies")
def case_studies():
    return render_template("case_studies.htm")


@app.route("/Contact")
def contact():
    return render_template("contact.htm")


@app.route("/Experience")
def experience():
    return render_template("experience.htm")


@app.route("/References")
def references():
    return render_template("references.htm")


@app.route("/Technology")
def technology():
    return render_template("technology.htm")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
