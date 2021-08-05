# BibTexFormatter

BibTeXFormatter is a simple Python script/package for the formatting of BibTeX (.bib) files.
It heavily relies upon the `bibtexparser` library.

# Usage

Functions from the package can be used outside the script:

```python
from bibtexformatter.formatter import formatBib

formatBib("bibtex.bib", output_path="bibtex-formatted.bib", ood="drdc-web")
```

If the script is run, it will ask the user for each of the parameters to be passed into the `formatBib()` function.

```
Please input the path to your .bib file, or 'exit':bibtex.bib
Please input the path you would like the output file to be:bibtex-formatted.bib
Please select an order of formatting. One of ['drdc-web'].
```

# Installation
As of now the package has to be downloaded manually. \
Users can do this with: \
`python setup.py install`

# License
No license (just a simple wrapper, most credit goes to the developers of the `bibtexparser` library).