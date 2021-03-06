#!/usr/bin/env python

NEUTRINO_HEROS_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
         'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename' : 'VXRack-Neutrino-Heros-Client.log'
        }
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG'
        }
    }
}