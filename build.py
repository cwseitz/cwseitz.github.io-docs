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
    regi = open('partials/photos.html').read()
    subs = open('partials/subjects.html').read()

    #Build index page
    index = HTMLDocument()
    index.set_style('assets/main.css')
    index.add_header(navi)
    index.add_content(land)
    index.write('index.html')

    #Build subject page
    sub_page = HTMLDocument()
    sub_page.set_style('../assets/main.css')
    sub_page.add_header(navi)
    sub_page.add_content(subs)
    sub_page.write('docs/index.html')

    #Build document listing page
    categories = ['bio/', 'prog/', 'dlrn/', 'phys/', 'neuro/', 'info/', 'phil/', 'thesis/']

    for category in categories:

        doc_page = HTMLDocument()
        doc_page.set_style('../../assets/main.css')
        doc_page.add_script('../../assets/table.js')
        doc_page.add_header(navi)
        doc_page.add_content(excel_to_html('docs/' + category + 'docs.xlsx'))
        doc_page.write(PATH_TO_DOCS + category + '/index.html')

        #Build document pages
        docs = os.listdir(PATH_TO_DOCS + category)
        docs = [x for x in docs if '.' not in x]

        for doc in docs:

            this_doc = HTMLDocument()
            this_doc.set_style('../../../assets/main.css')
            this_doc.add_header(navi)

            html = get_doc_content(PATH_TO_DOCS + category + doc)
            if html is not None:
                this_doc.add_content(html)
                new_file =  PATH_TO_DOCS + category + '%s/index.html' % doc
                this_doc.write(new_file)


    #Build photos page
    photos = HTMLDocument()
    photos.set_style('../assets/main.css')
    photos.add_header(navi)
    photos.add_content(regi)
    photos.write('./photos/index.html')


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
