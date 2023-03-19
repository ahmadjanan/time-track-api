import os

from dotenv import load_dotenv, find_dotenv


class EnvVariableNotSet(Exception):
    """Should be raised when an environment variable necessary for setting is not set"""


def required_env_var(var_name):
    var = os.environ.get(var_name)
    if var is None:
        raise EnvVariableNotSet(var_name)
    return var


load_dotenv(find_dotenv())

# DJANGO
SECRET_KEY = required_env_var("SECRET_KEY")
# DB
DB_NAME = required_env_var("DB_NAME")
