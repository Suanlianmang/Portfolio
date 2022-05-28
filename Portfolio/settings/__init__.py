from .keys import *
from .development import *


if keys.DEBUG == 'False':
    from .production import *

SECRET_KEY = keys.SECRET_KEY