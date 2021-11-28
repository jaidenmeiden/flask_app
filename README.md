### Activate environment
```
python3 -m venv venv  
source venv/bin/activate
```
### Deactivate environment
```
deactivate
```
### Install tools
```
pip install flask
pip install flask-bootstrap4
pip install flask-wtf
pip install flask-testing
pip freeze
```

### Launch application

it is necessary to declare an environment variable so that flask knows where the flask instance is and thus be able to run flask run

```
export FLASK_APP=main.py
echo $FLASK_APP
```
**Only in development environment:**
```
export FLASK_DEBUG=1
echo $FLASK_DEBUG
```
**Environment:**
```
export FLASK_ENV=development
echo $FLASK_ENV
```

### Launch application
```
flask run
```

### Testing
```
flask test
```

# Flask Specification

[Flask](https://flask.palletsprojects.com/en/2.0.x/)

[Source code](https://github.com/pallets/flask/)

[Flask-Testing](https://pythonhosted.org/Flask-Testing/)

[Single-Page Applications](https://flask.palletsprojects.com/en/2.0.x/patterns/singlepageapplications/)

#### General description

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools.

#### Technician description 

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.

# Tools

### [Jinja 2](https://jinja2docs.readthedocs.io/en/stable/)

[Source code](https://github.com/pallets/jinja)

Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment.

Features:

* Sandboxed execution
* Powerful automatic HTML escaping system for XSS prevention
* Template inheritance
* Compiles down to the optimal python code just in time
* Optional ahead-of-time template compilation
* Easy to debug. Line numbers of exceptions directly point to the correct line in the template.
* Configurable syntax

### [TailwindCSS](https://tailwindcss.com/)

[Integrating TailwindCSS into Flask Apps](https://www.section.io/engineering-education/integrate-tailwindcss-into-flask/)

TailwindCSS is a utility-first CSS framework used to build frontend applications. TailwindCSS differs from other kinds of CSS frameworks as it gives the user total control over their design.

Rather than adding obscure CSS classes to your code, with TailwindCSS you use utility classes to create your components, with as much control over every single styling as you want. All without having to ever write a single line of CSS.




