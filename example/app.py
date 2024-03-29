from flask import Flask, render_template
from flask_wtf import FlaskForm
from jinja_wtforms import WtformExtension


app = Flask(__name__)
app.jinja_env.form_base_cls = FlaskForm
app.jinja_env.add_extension(WtformExtension)
app.config['SECRET_KEY'] = 'secret'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = app.jinja_env.forms['index.html'].form()
    fail = app.jinja_env.forms['index.html'].fail()
    if form.validate_on_submit():
        return render_template('success.html', data=form.data)
    return render_template('index.html', form=form, fail=fail)
