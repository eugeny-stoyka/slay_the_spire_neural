# -*- coding: utf-8 -*-
""" Сервер. """

import json
import flask
from werkzeug import serving, exceptions

class SlayTheSpireApp(flask.Flask):
    def __init__(self, threaded=True, processes=1, *args, **kwargs):
        flask.Flask.__init__(self, import_name=__name__, *args, **kwargs)
        self.config['JSON_SORT_KEYS'] = False
        self.config['JSON_AS_ASCII'] = False
