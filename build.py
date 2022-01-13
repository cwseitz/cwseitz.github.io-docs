import os
import subprocess
from os.path import basename, splitext
from glob import glob
from util import *

PATH_TO_DOCS = './docs/'
PATH_TO_DOCS_TABLE = 'docs/docs.csv'

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

    #Build project listing page
    projects = ['iplm/', 'fdl/', 'info/', 'hdss/', 'bio/']

    for project in projects:

        doc_page = HTMLDocument()
        doc_page.set_style('../../assets/main.css')
        doc_page.add_script('../../assets/table.js')
        doc_page.add_header(navi)
        doc_page.add_content(csv_to_html('docs/' + project + 'docs.csv'))
        doc_page.write(PATH_TO_DOCS + project + '/index.html')

        #Build document pages
        docs = os.listdir(PATH_TO_DOCS + project)
        docs = [x for x in docs if '.' not in x]

        for doc in docs:

            this_doc = HTMLDocument()
            this_doc.set_style('../../../../assets/main.css')
            this_doc.add_header(navi)

            DOC_PATH = PATH_TO_DOCS + project + doc + '/' + doc
            html = get_doc_content(DOC_PATH)

            if html is not None:
                this_doc.add_content(html)
                new_file =  PATH_TO_DOCS + project + doc + '/%s/index.html' % doc
                this_doc.write(new_file)


    # #Build photos page
    # photos = HTMLDocument()
    # photos.set_style('../assets/main.css')
    # photos.add_header(navi)
    # photos.add_content(regi)
    # photos.write('./photos/index.html')


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
