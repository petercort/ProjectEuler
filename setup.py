from setuptools import setup

setup(
    name='ProjectEuler',
    packages=['ProjectEuler'],
    include_package_data=True,
    install_requires=[
        'flask',
        'click',
		'gunicorn',
		'itsdangerous',
		'Jinja2',
		'MarkupSafe',
		'Werkzeug'
    ],
)