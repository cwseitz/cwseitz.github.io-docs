import os
import subprocess
from os.path import basename, splitext
from glob import glob
from util import *

PATH_TO_DOCS = './docs/'
PATH_TO_DOCS_TABLE = 'docs/docs.xlsx'

def build_site():

    #Read HTML partials
    navi = open('partials/navigation.html').read()
    land = open('partials/landing.html').read()

    #Build index page
    index = HTMLDocument()
    index.set_style('assets/main.css')
    index.add_header(navi)
    index.add_content(land)
    index.write('index.html')

    #Build document listing page
    documents = HTMLDocument()
    documents.set_style('../assets/main.css')
    documents.add_header(navi)
    documents.add_content(excel_to_html(PATH_TO_DOCS_TABLE))
    documents.write(PATH_TO_DOCS + 'index.html')

    #Build document pages
    docs = os.listdir(PATH_TO_DOCS)
    docs = [x for x in docs if '.' not in x]

    for fldr in docs:

        this_doc = HTMLDocument()
        this_doc.set_style('../../assets/main.css')
        this_doc.add_header(navi)

        html = get_doc_content(PATH_TO_DOCS + fldr)
        if html is not None:
            this_doc.add_content(html)
            new_file =  PATH_TO_DOCS + '%s/index.html' % fldr
            this_doc.write(new_file)
        
def get_doc_content(fldr):

    """This function only supports inserting pdf currently"""

    files = os.listdir(fldr)
    html = None
    for file in files:
        filetype = os.path.splitext(file)[1]
        if filetype == '.pdf':
            html = f'<div style="margin-top: 5%;"><object width=100% height=800px data="{file}" type="application/pdf"></object></div>'
    return html

if __name__ == "__main__":
    build_site()

