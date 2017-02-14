#!/usr/bin/env python

from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)

reqs = [str(ir.req) for ir in install_reqs]

setup_args = {
    'name': 'cups_mqtt_bridge',
    'version': '0.0.1',
    'url': 'https://github.com/hanseartic/cups-mqtt-bridge',
    'packages': ['cmb'],
    'install_requires': reqs
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args)
