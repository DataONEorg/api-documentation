# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = $(CURDIR)/build
GRAPHVIZ      = /usr/bin/dot
JAVA          = /usr/bin/java
XSLTPROC      = /usr/bin/xsltproc
PYTHON        = /usr/bin/python
PLANTUMLCONF  = $(CURDIR)/tools/docutils/plantuml.conf
PLANTUML      = $(JAVA) -jar "$(CURDIR)/tools/docutils/plantuml.jar" -config "$(PLANTUMLCONF)"
DOCGENERATOR  = $(PYTHON) "$(CURDIR)/tools/ihwd/ihwd.py"
METHODXLS     = MethodCrossReference.xls
ZIPHTML       = architecture.zip
SCHEMADIR     = source/D1_SCHEMA_v1
XSD2RST       = source/tools/xsd2rst
#SCHEMADIR     = /Users/vieglais/Workspaces/DataONE_trunk/d1_schemas

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d "$(BUILDDIR)/doctrees" $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes linkcheck doctest pdf

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  generate  to generate doc files from spreadsheet and schema"
	@echo "  plantuml  to make PlantUML diagrams"
	@echo "  html      to make standalone HTML files"
	@echo "  all       Run generate, plantuml, and html to make standalone HTML files"
	@echo "  epub      to make ePub document"
	@echo "  dirhtml   to make HTML files named index.html in directories"
	@echo "  pickle    to make pickle files"
	@echo "  json      to make JSON files"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  qthelp    to make HTML files and a qthelp project"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  changes   to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"
	@echo "  doctest   to run all doctests embedded in the documentation (if enabled)"
	@echo "  pdf       to make PDF files"

clean:
	-rm -rf "$(BUILDDIR)"

all: generate plantuml html

generate: generate_types generate_methods

generate_methods: $(METHODXLS)
	$(DOCGENERATOR) -s "$(CURDIR)/$(METHODXLS)" -d "$(CURDIR)/source/apis/generated"

generate_types: 
	$(XSLTPROC) --path ".:$(SCHEMADIR):$(XSD2RST)" dataoneTypes2rst.xsl dataoneTypes.xsd > "$(CURDIR)/source/apis/Types.txt"

plantuml: plantuml_source plantuml_usecase plantuml_types

plantuml_source:
	GRAPHVIZ_DOT=$(GRAPHVIZ) $(PLANTUML) "$(CURDIR)/source" "$(CURDIR)/source/design"

plantuml_usecase:
	GRAPHVIZ_DOT=$(GRAPHVIZ) $(PLANTUML) "$(CURDIR)/source/design/UseCases"

plantuml_types:
	GRAPHVIZ_DOT=$(GRAPHVIZ) $(PLANTUML) "$(CURDIR)/source/apis"

html: 
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) "$(BUILDDIR)/html"
	#zip -r $(BUILDDIR)/$(ZIPHTML) $(BUILDDIR)/html
	#mv $(BUILDDIR)/$(ZIPHTML) $(BUILDDIR)/html/
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) "$(BUILDDIR)/dirhtml"
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) "$(BUILDDIR)/pickle"
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) "$(BUILDDIR)/json"
	@echo
	@echo "Build finished; now you can process the JSON files."

pdf:
	$(SPHINXBUILD) -b pdf $(ALLSPHINXOPTS) "$(BUILDDIR)/pdf"
	@echo
	@echo "Build finished. The PDF files are in $(BUILDDIR)/pdf."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) "$(BUILDDIR)/htmlhelp"
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) "$(BUILDDIR)/qthelp"
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/DataONEArchitecture.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/DataONEArchitecture.qhc"

latex: 
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) "$(BUILDDIR)/latex"
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) "$(BUILDDIR)/changes"
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) "$(BUILDDIR)/linkcheck"
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) "$(BUILDDIR)/doctest"
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) "$(BUILDDIR)/epub"
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

