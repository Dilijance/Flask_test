# Flask Fundamentals

## Setup
    create .env file for auto run your code:
        ** inside .env **
        FLASK_APP="Name_of_file.py"
        FLASK_ENV="development"
        FLASK_DEBUG=1

    To run your programm call in powershell:
        Using .env:
            flask run

        Without .env:
            flask --app sample --debug run

    Create run.py as shortcut for activating application

```python
from Your_folder import app

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)
```
    Then initialize in .env:
        FLASK_APP="run.py"


## Front-end

* Templates folder is a default path for flask for getting .html files
* (Store your .html files in this folder)

### HTML
    ??
    
### CSS
    ??


## Back-end

### __ __init__ __.py
    Connection between whole application
    Through which run.py can get access to
```python
```

### forms.py
    Making slots for user inputs and validate input for the future storing in database

    EXAMPLE OF REGISTRATION MODEL
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from cafe.models import User

class RegisterForm(FlaskForm):
    # Check input for already existing User
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist! Please try a different username')
        
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different Email')

    # Creating a new One
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

```
### models.py
    Get data from forms.py and contain all data in database which was created by __ init __.py
```python

```

### routes.py
    Main purpose of routes.py is to connect Front-end and Back-end together and redirect user through sites