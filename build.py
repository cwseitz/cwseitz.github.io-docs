import os
import markdown
import nbformat
from nbconvert import HTMLExporter
from document import HTMLDocument

navi = """  <nav class="menu">
                <ul class="menu__inner">
                  <li><a href="posts">Drafts</a></li>
                  <li><a href="mirage">Mirage</a></li>
                  <li><a href="photos">Photography</a></li>
                </ul>
            </nav>"""

logo = """
            <div class="logo">
                    <span class="logo__mark">></span>
                    <span class="logo__text">cd ~</span>
                    <span class="logo__cursor"
                    style="background-color:#008080;animation-duration:0.75s;">
                    </span>
            </div>"""

content = """
            <div class="content">
                <main aria-role="main">
                  <style type="text/css">
                  .bgimg {
                      background-image: url('static/landing');
                      height: 500px;
                      width: 900px;
                  }
                  .hstyle {
                      line-height: 500px;
                  }
                  </style>

                <div class="bgimg">
                    <h1 class="hstyle"></h1>
                </div>

                <div>
                    <p>I just wondered how things were put together - Claude Shannon</p>
                </div>

            </main>
        </div>"""


index = HTMLDocument()
index.set_style('assets/main.css')
index.add_header(logo, navi)
index.add_content(content)
index.add_mathjax()
index.add_scripts()
index.write('index.html')

#Build posts
md_files = os.listdir('md')
for file in md_files:
    rootname = file.split('.')[0]
    dir = f'posts/{rootname}'
    if not os.path.exists(dir):
        os.mkdir(dir)

    post = markdown.markdown(open('md/' + file).read())

    post = f"""
                    <div style="margin: 0 auto; width: 50%;">
                    {post}
                    </div>
                 """


    this_post = HTMLDocument()
    this_post.set_style('../../assets/main.css')
    this_post.add_header(logo, navi)
    this_post.add_content(post)
    this_post.add_mathjax()
    this_post.write(f'posts/{rootname}/index.html')
