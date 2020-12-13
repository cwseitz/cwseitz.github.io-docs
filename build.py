from document import HTMLDocument

header = """<header class="header">
                <span class="header__inner">
                    <a href="/" style="text-decoration: none;">
                    <div class="logo">
                            <span class="logo__mark">></span>
                            <span class="logo__text">cd ~</span>
                            <span class="logo__cursor" style="background-color:#008080;animation-duration:0.75s;">
                            </span>
                    </div>
                    </a>

                    <span class="header__right">

            <nav class="menu">
                <ul class="menu__inner">
                  <li><a href="/posts">Drafts</a></li>
                  <li><a href="/mirage">Mirage</a></li>
                  <li><a href="/photos">Photography</a></li>
                </ul>
            </nav>

                            <span class="menu-trigger">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                    <path d="M0 0h24v24H0z" fill="none"/>
                                    <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>
                                </svg>
                            </span>


                        <span class="theme-toggle unselectable"><svg class="theme-toggler" width="24" height="24" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M22 41C32.4934 41 41 32.4934 41 22C41 11.5066 32.4934 3 22
              3C11.5066 3 3 11.5066 3 22C3 32.4934 11.5066 41 22 41ZM7 22C7
              13.7157 13.7157 7 22 7V37C13.7157 37 7 30.2843 7 22Z"/>
            </svg>
            </span>
            </span>
            </span>
            </header>"""

content = """            <div class="content">

    <main aria-role="main">

      <style type="text/css">
      .bgimg {
          background-image: url('../../img');
          height: 500px;
          width: 900px;
      }
      .hstyle {
          line-height: 500px;
      }
      </style>

        <div>

        </div>
        <div class="bgimg">
            <h1 class="hstyle"></h1>
        </div>
        <div>
                <p>I just wondered how things were put together - Claude Shannon</p>
        </div>

    </main>

            </div>"""

document = HTMLDocument()
document.set_style('assets/main.css')
document.add_mathjax()
document.add_scripts()
document.add_header(header)
document.add_content(content)
document.write('index.html')
