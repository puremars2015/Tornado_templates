#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        #print('method/function [set_default_headers] of class [BaseHandler] of Python code in [BaseHandler.py] is called.') # DEBUG 
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        #self.set_header('Access-Control-Allow-Headers', 'x-requested-with, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
        #self.set_header('Access-Control-Allow-Headers', 'authorization,Authorization,Content-Type,Access-Control-Allow-Origin,Access-Control-Allow-Headers,X-Requested-By,Access-Control-Allow-Methods')
        self.set_header('Access-Control-Allow-Methods', '*')
        #self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', '*')
        #self.set_header('Content-type', 'application/json; charset=UTF-8')

    # HTTP method 'OPTIONS'
    def options(self):
        print('HTTP method [OPTION] is called.') # DEBUG 
        # For CORS(cross origin resource sharing), we have to implement HTTP method 'OPTIONS' to handle pre-flight request of browsers. 
        self.set_default_headers()
        self.set_status(204) # We set HTTP status code to 204. HTTP status code 204 'No Content success' means a request has succeeded, but that the client doesn't need to navigate away from its current page. This is for pre-flight request of browsers, which is a browsers' behavior to enhance safety during CORS. 
        self.finish()
