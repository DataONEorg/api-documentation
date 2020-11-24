# Architecture Docs

![Build Pages](https://github.com/DataONEorg/api-documentation/workflows/Build%20Pages/badge.svg)

API and Architecture documentation for DataONE.

This is a [Sphinx](https://www.sphinx-doc.org/en/master/index.html) 
project that provides documentation for the DataONE
Coordinating Node and Member Node (i.e. repository) service interfaces. 
Various design documents are included for additional information.

The current released version of the documentation is available at:

  https://purl.dataone.org/architecture

Or:

  https://dataoneorg.github.io/api-documentation/


## Contributing

These documents are built automatically after the GitHub repository is updated
with a push to master. See the [GitHub Action work flow](https://github.com/DataONEorg/api-documentation/blob/master/.github/workflows/gh-pages.yml) for more details

Minor edits can be made through the GitHub editor interface or through
the usual clone / fork, edit, commit, and push / pull-request process.

Most of the source documents are composed in [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html). 

The APIs are documented with mock Python methods documented using 
Google docstring formatting. After editing and commiting changes to 
those files, the changes will be reflected in the API docs through the
various sphinx `auto*` directives. 

## Building

This project uses [Poetry](https://python-poetry.org/docs/) for dependency management. 

```
git clone https://github.com/DataONEorg/api-documentation.git
cd api-documentation
poetry install
make html
```

The generated HTML will be available at `build/html/index.html`

Live generation and reload is also available:

```
make livehtml
```

A local web server will make the pages available at http://localhost:8000/ and edits to the source will be automatically rendered in the browser.

