from setuptools import find_packages, setup

NAME = "Cloudmesh Eve"
DESCRIPTION = "A REST service for cloudmesh"
AUTHOR = "Gregor von Laszewski, I524"
AUTHOR_EMAIL = "laszewski@gmail.com"
URL = "https://github.com/cloudmesh/eve"
LONG_DESCRIPTION = """
Cloudmesh Eve
==============

Development environment for cloudmesh to define simple REST services

"""

setup \
(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    version="1.0.0",
    license="Apache 2.0",
    url=URL,
    packages=find_packages(),
    #package_data={
    #    "cloudmesh.data": [
    #        "templates/cloudmesh/data.txt",
    #    ]
    #},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "eve",
        "pygments",
        "detox",
    ],
    # test_suite="runtests.runtests",
    tests_require=[
        "flake8",
        "coverage",
    ],
    zip_safe=False,
)
