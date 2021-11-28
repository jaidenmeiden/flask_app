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

### Launch application
```
flask run
```

# Specification Flask

[Path Operation](https://fastapi.tiangolo.com/tutorial/path-operation-configuration/?h=path+operation)

# Tools

### [fastAPI](https://fastapi.tiangolo.com/)



