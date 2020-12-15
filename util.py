import markdown

def md_to_post(file):

    html = markdown.markdown(open('md/' + file).read(), extensions=['fenced_code'])



    html = f"""<div style="margin: 0 auto; width: 40%;
                border: 1px solid black; padding: 50px;
                margin-top: 50px; text-align: left;
                font-size: 12px">
                {html}
                </div>
                 """

    return html
