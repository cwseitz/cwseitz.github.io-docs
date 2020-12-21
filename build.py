import os
import pandas as pd
from glob import glob
from document import HTMLDocument
from util import md_to_post

def build_posts_html():
	
	posts = pd.read_csv('posts.csv')
	posts = posts.fillna('')
	cols = posts.columns

	for col in cols:
		posts[col] = posts[col].apply(lambda x: '<a href="{0}/index.html">{0}</a>'.format(x))
	
	html = posts.to_html(justify='left', index=False, escape=False)
	html = html.replace('border="1"','border="0"')


	return html



navi = open('partials/navi.html').read()
logo = open('partials/logo.html').read()
body = open('partials/body.html').read()
post_style = open('partials/post_style.html').read()

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
posts.add_content(build_posts_html())
posts.write('posts/index.html')
