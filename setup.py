from setuptools import setup

setup(
    name = "pynist",
    version = "0.1",
    author = "Christopher Poole",
    author_email = "mail@christopherpoole.net",
    description = "Grab NIST physics data as numpy arrays",
    keywords = "NIST, physics data",
    url = "http://github.com/christopherpoole/pynist",
    packages = ["nist"],    
    package_data = {'' : ['*.yaml']},
    long_description=open("README.markdown").read(),
)
