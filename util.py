import markdown

def md_to_post(file):

    html = markdown.markdown(open('md/' + file).read(), extensions=['fenced_code'])



    html = f"""<div style="margin: 0 auto; width: 850px;
                border: 1px solid black; padding: 50px;
                margin-top: 100px; text-align: left;
                font-size: 14px">
                {html}
                </div>
                 """

    return html
