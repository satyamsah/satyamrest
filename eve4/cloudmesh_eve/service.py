#!/usr/bin/env python

from eve import Eve

from settings import eve_settings 

app = Eve(settings=eve_settings)

if __name__ == '__main__':
    app.run()
