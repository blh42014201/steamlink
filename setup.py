#!/usr/bin/env python3
"""SteamLink setup script."""
import os
from setuptools import setup, find_packages
from steamlink.const import (__version__, PROJECT_PACKAGE_NAME,
								PROJECT_LICENSE, PROJECT_URL,
								PROJECT_EMAIL, PROJECT_DESCRIPTION,
								PROJECT_LONG_DESCRIPTION, 
								PROJECT_CLASSIFIERS, GITHUB_URL,
								PROJECT_AUTHOR)

HERE = os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_URL = ('{}/archive/'
				'{}.tar.gz'.format(GITHUB_URL, __version__))

PACKAGES = find_packages(exclude=['tests', 'tests.*'])
REQUIRES = [
	'PyYAML>=3.11,<4',
	'aiohttp>=3.0.0',
	'aiomqtt>=0.1.0',
	'python-socketio>=1.8.4',
	'paho-mqtt>=1.3.1,<2',
	'hbmqtt==0.8.0',
	'jinja2==2.10',
	'aiohttp-jinja2>=1.0.0',
	'tinydb>=3.9.0',
	'tinydb-smartcache>=1.0.2',
	'zeroconf>=0.20.0',
	'msgpack>=0.5.6'
]

setup(
	name=PROJECT_PACKAGE_NAME,
	version=__version__,
	license=PROJECT_LICENSE,
	url=PROJECT_URL,
	download_url=DOWNLOAD_URL,
	author=PROJECT_AUTHOR,
	author_email=PROJECT_EMAIL,
	description=PROJECT_DESCRIPTION,
	long_description=PROJECT_LONG_DESCRIPTION,
	packages=PACKAGES,
	include_package_data=True,
	zip_safe=False,
	platforms='any',
	install_requires=REQUIRES,
	keywords=['iot', 'LoRa'],
	entry_points={
		'console_scripts': [
			'steamlink = steamlink.main:steamlink_command'
		],
	},
	scripts=['bin/pynode-example.py'],
	classifiers=PROJECT_CLASSIFIERS,
)
