
profile = {
    'schema': {
        'firstname': {
            'type': 'string'
        },
        'Lastname': {
            'type': 'string'
        },
        'e-mail': {
            'type': 'string'
        },
        'username': {
            'type': 'string'
        }
    }
}

cluster = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'label': {
            'type': 'string'
        },
        'provider': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'endpoint': {
            'type': 'dict',
            'schema': {
                'url': {
                    'type': 'string'
                },
                'passwd': {
                    'type': 'string'
                }
            }
        }
    }
}

computer = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'label': {
            'type': 'string'
        },
        'ip': {
            'type': 'string'
        },
        'memoryGB': {
            'type': 'integer'
        }
    }
}



eve_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_DBNAME': 'testing',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'BANDWIDTH_SAVER': False,
    'DOMAIN': {
        'profile': profile,
        'cluster': cluster,
        'computer': computer,
    },
}
