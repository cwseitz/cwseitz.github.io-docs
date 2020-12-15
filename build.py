import os
from document import HTMLDocument
from util import md_to_post

navi = open('partials/navi.html').read()
logo = open('partials/logo.html').read()
body = open('partials/body.html').read()

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
md_files = os.listdir('md')
for file in md_files:
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

    var = f"""
                <a href="{rootname}/">{rootname}</a>
            """

    posts.add_content(var)


posts.write('posts/index.html')
