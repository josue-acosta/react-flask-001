# React-Flask App Boilerplate

## Install dependancies
Run `yarn install` in the root directory folder ( `react-flask-001` )


## Saticfy the `app.config.from_object("api.configuration.DevelopmentConfig")` requirement
``` python
# api/configuration.py
class BaseConfig(object):
    """Base config class"""
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = "my new base config variable"

class ProductionConfig(BaseConfig):
    """Production config class"""
    DEBUG = False
    ENV = "production"
    NEW_CONFIG_VARIABLE = "my new production config variable"

class StagingConfig(BaseConfig):
    """Staging config class"""
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """Development config class"""
    DEBUG = True
    TESTING = True
    ENV = "development"
    NEW_CONFIG_VARIABLE = "my new development config variable"
```


## Start the servers
React app: `yarn start`

Flask app: `yarn start-api`