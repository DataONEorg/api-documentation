# Architecture Docs

![Build Pages](https://github.com/DataONEorg/api-documentation/workflows/Build%20Pages/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/dataone-architecture-documentation/badge/?version=latest)](https://dataone-architecture-documentation.readthedocs.io/en/latest/?badge=latest)

API and Architecture documentation for DataONE.

This is a [Sphinx](https://www.sphinx-doc.org/en/master/index.html) 
project that provides documentation for the DataONE
Coordinating Node and Member Node (i.e. repository) service interfaces. 
Various design documents are included for additional information.

The current released version of the documentation is available at:

  https://purl.dataone.org/architecture

The draft version built from GitHub sources is available at:

  https://dataone-architecture-documentation.readthedocs.io/en/latest/


## Contributing

These documents are built automatically after the GitHub repository is updated
with a commit.

Minor edits can be made through the GitHub editor interface or through
the usual clone / fork, edit, commit, and push / pull-request process.

Most of the source documents are composed in [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html). 

The APIs are documented with mock Python methods documented using 
Google docstring formatting. After editing and commiting changes to 
those files, the changes will be reflected in the API docs through the
various sphinx `auto*` directives. 

## Building

1. Ensure that the various requirements are installed:

* [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
* [recommonmark](https://recommonmark.readthedocs.io/en/latest/)
* [plantweb](https://plantweb.readthedocs.io/)
* [sqltable](https://github.com/datadavev/docutils_sqltable) *Note:* this module is to be deprecated.

2. Clone or fork the repository

3. Change to the folder of the checked-out project

4. Run `make clean html` to generate HTML documentation

