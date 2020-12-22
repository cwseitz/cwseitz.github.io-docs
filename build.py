import os
import pandas as pd
from glob import glob
from util import *


navi = open('partials/navi.html').read()
logo = open('partials/logo.html').read()
body = open('partials/body.html').read()
post_style = open('partials/post_style.html').read()
proj_style = open('partials/proj_style.html').read()

#Build index page
index = HTMLDocument()
index.set_style('assets/main.css')
index.add_header(logo, navi)
index.add_content(body)
index.write('index.html')

#Initialize post listing page
posts = HTMLDocument()
posts.set_style('../assets/main.css')
posts.add_header(logo, navi)

#Build posts
files = glob('raw/*.md')
for file in files:
    file = os.path.basename(file)
    rootname = file.split('.')[0]
    dir = f'posts/{rootname}'
    if not os.path.exists(dir):
        os.mkdir(dir)

    post = md_to_post(file)
    this_post = HTMLDocument()
    this_post.set_style('../../assets/main.css')
    this_post.add_header(logo, navi)
    this_post.add_content(post)
    this_post.add_scripts()
    this_post.write(f'posts/{rootname}/index.html')


posts.head = post_style
posts.add_content(csv_to_html('util/posts.csv'))
posts.write('posts/index.html')


#Build project page 
projects = HTMLDocument()
projects.set_style('../assets/main.css')
projects.add_header(logo, navi)
projects.head = proj_style
projects.add_content(csv_to_html('util/projects.csv'))
projects.write('projects/index.html')
