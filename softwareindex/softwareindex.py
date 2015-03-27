from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextField, SubmitField, validators
from wtforms.validators import Required
from handlers import test_handler
from handlers import stackexchange_handler
from handlers import slideshare_handler

class BasicForm(Form):
    softwarename = TextField('Software Name', description='Software Name.')
    githubproject = TextField('GitHub Project', description='Github Project.')
    stackoverflow =  TextField('Stackoverflow Activity', description='Stackoverflow Activity.')
    submit_button = SubmitField('Submit Form') 

def create_app(configfile=None):
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = 'devkey'

    @app.route('/')
    def index():
        form = BasicForm()
        form.validate_on_submit()
        flash('critical message', 'critical')
        flash('error message', 'error')
        flash('warning message', 'warning')
        flash('info message', 'info')
        flash('debug message', 'debug')
        flash('different message', 'different')
        flash('uncategorized message')
        return render_template('index.html', form=form)

    @app.route('/about')
    def about():
       return render_template('about.html')

    @app.route('/index/test/')
    @app.route('/index/test/<software>')
    def test(software=None, score=-2):
        handler=test_handler.test_handler_handler()
        score=handler.get_score(software)
        description=handler.get_description()
        return render_template('test.html', software=software, score=score, description=description)

    @app.route('/index/stackexchange/')
    @app.route('/index/stackoverflow/')
    @app.route('/index/stackexchange/<software>')
    @app.route('/index/stackoverflow/<software>')
    def stackexchage(software=None, score=-2):
        handler=stackexchange_handler.stackoverflow_handler()
        score=handler.get_score(software)
        description=handler.get_description()
        return render_template('test.html', software=software, score=score, description=description)

    @app.route('/index/slideshare/')
    @app.route('/index/slideshare/<software>')
    def slideshare(software=None, score=-2):
        handler=slideshare_handler.slideshare_handler()
        score=handler.get_score(software)
        description=handler.get_description()
        return render_template('test.html', software=software, score=score, description=description)

    @app.route('/index/core/')
    @app.route('/index/core/<software>')
    def core(software=None, score=-2):
        handler=core_handler.core_handler()
        score=handler.get_score(software)
        description=handler.get_description()
        return render_template('test.html', software=software, score=score, description=description)

  

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
