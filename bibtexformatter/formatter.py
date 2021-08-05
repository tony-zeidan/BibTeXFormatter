import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import homogenize_latex_encoding

orders = {
    "drdc-web": ["title", "author", "editor", "institution", "address", "year", "month", "publisher", "booktitle",
                 "journal", "volume", "number", "pages", "keywords", "isbn", "issn", "doi",
                 "eprint", "url", "abstract", "note", "issue_date", "accessdate"]
}

default_order = "drdc-web"


def parseFile(filepath: str) -> BibDatabase:
    """Wrapper for parsing .bib file.

    :param filepath: The input filepath to parse
    :type filepath: str
    :return: The parsed bib database
    :rtype: BibDatabase
    """
    with open(filepath) as bibtex_file:
        return bibtexparser.load(bibtex_file, parser=BibTexParser(
            customization=homogenize_latex_encoding,
            interpolate_strings=False,
            ignore_nonstandard_types=False,
            homogenize_fields=True,
            common_strings=False
        ))


def formatBib(filepath: str, output_path: str = None, ood: str = None):
    """Formats a .bib file.

    :param filepath: The input filepath (.bib file)
    :type filepath: str
    :param output_path: The output filepath (default=same as input path)
    :type output_path: str
    :param ood: The order of display to use (default='drdc-web')
    :type ood: str
    """
    if output_path is None:
        output_path = filepath

    db = parseFile(filepath)

    writer = BibTexWriter(write_common_strings=False)
    writer.indent = '\t'
    writer.comma_first = False
    writer.align_values = True
    try:
        writer.display_order = list(orders[ood])
    except KeyError:
        writer.display_order = list(orders[default_order])

    with open(output_path, "w") as output_file:
        output_file.write(writer.write(db))


def _executeFormat():
    """Executes the main script stub.
    """
    input_path = input("Please input the path to your .bib file, or 'exit':")
    if input_path.lower() == 'exit':
        return
    output_path = input("Please input the path you would like the output file to be:")
    if output_path.lower() == 'exit':
        return
    ood = input(f"Please select an order of formatting. One of {list(orders.keys())}:").lower()
    if ood == 'exit':
        return
    formatBib(input_path, output_path=(output_path or None), ood=(ood or None))


if __name__ == '__main__':
    _executeFormat()
