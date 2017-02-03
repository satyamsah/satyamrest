#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import yaml
from cerberus import Validator

schema_text = '''
name:
  type: string
age:
  type: integer
  min: 10
'''

schema = yaml.load(schema_text)
document = {'name': 'Gregor von Laszewski', 'age': 3}
v = Validator()
print(v.validate(document, schema))
print(v.errors)
