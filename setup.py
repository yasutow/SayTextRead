from setuptools import setup, find_packages

setup(
    name='SayTextRead',
    version='0.0.1',
    license='MIT',
    description='This python program produces the estimated time to finish reading a set of .txt files written in Japanese language.',
    install_requires=["pyttsx3"],
    author='yasutow',
    author_email='yasuto@g.ecc.u-tokyo.ac.jp',
    url='https://github.com/yasutow',
    packages=['SayTextRead']
    )
