# Jinja-WTForms

Extract WTForms classes from jinja templates

## Installation

    pip install jinja-wtforms

## Setup

```py
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
env.add_extension('jinja_wtforms.WtformExtension')
```

## Defining forms in templates

Defining forms is almost like using a pre-defined form but with added information
on the type of the field.

To do so, you'll need to call a method named after the type of the field on each
field. So if you want to define a "firstname" field as a text field, you can
do `form.firstname.text()`.

Let's define a signup form:

    <form action="" method="post">
        {{ form.csrf_token() }}
        <p><label>First name</label> {{ form.firstname.text() }}</p>
        <p><label>Last name</label> {{ form.lastname.text() }}</p>
        <p><label>Email</label> {{ form.email.email() }}</p>
        <p><label>Password</label> {{ form.password.password() }}</p>
    </form>

The optional parameters of the field definition functions are:

 - *label*: the field's label (can also be define as the first argument)
 - *description*: the field's description
 - *placeholder*: the field's placeholder
 - *required*: boolean, default false
 - *optional*: boolean, default false
 - *range*: a tuple of (min, max), value should be a number in the range
 - *length*: a tuple of (min, max), value should be of string of length in the range
 - *validators*: a list of validator names from `wtforms.validators`

Available field types and their actual class:

 - *checkbox*: `wtforms.fields.BooleanField`
 - *decimal*: `wtforms.fields.DecimalField`
 - *date*: `wtforms.fields.DateField`
 - *datetime*: `wtforms.fields.DateTimeField`
 - *float*: `wtforms.fields.FloatField`
 - *int*: `wtforms.fields.IntegerField`
 - *radio*: `wtforms.fields.RadioField`
 - *select*: `wtforms.fields.SelectField`
 - *selectmulti*: `wtforms.fields.SelectMultipleField`
 - *text*: `wtforms.fields.StringField`
 - *textarea*: `wtforms.fields.TextAreaField`
 - *password*: `wtforms.fields.PasswordField`
 - *upload*: `wtforms.fields.FileField`
 - *hidden*: `wtforms.fields.HiddenField`
 - *datetimelocal*: `wtforms.fields.DateTimeLocalField`
 - *decimalrange*: `wtforms.fields.DecimalRangeField`
 - *email*: `wtforms.fields.EmailField`
 - *intrange*: `wtforms.fields.IntegerRangeField`
 - *search*: `wtforms.fields.SearchField`
 - *tel*: `wtforms.fields.TelField`
 - *url*: `wtforms.fields.URLField`

## Extracting forms

Use the form registry available through the `forms` property of the environment:

```py
form_class = env.forms["form.html"].form # where form.html is the template filename containing the form definition
form = form_class()
```