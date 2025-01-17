from setuptools import setup

setup(
    name='flask-lambda-python36',
    version='0.1.1',
    description=('Python3.6+ module to make Flask compatible with AWS Lambda'),
    keywords='flask aws amazon lambda',
    author='Andrew Griffiths',
    author_email='mail@andrewgriffithsonline.com',
    url='https://github.com/techjacker/flask-lambda',
    license='Apache License, Version 2.0',
    py_modules=['flask_lambda'],
    install_requires=['Flask>=0.10'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
    ]
)
