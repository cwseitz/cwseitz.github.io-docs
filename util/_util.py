import markdown
import pandas as pd

def csv_to_html(csv):

        posts = pd.read_csv(csv)
        posts = posts.fillna('')
        cols = posts.columns

        for col in cols:
                posts[col] = posts[col].apply(lambda x: '<a href="{0}/index.html">{0}</a>'.format(x))

        html = posts.to_html(justify='left', index=False, escape=False)
        html = html.replace('border="1"','border="0"')

        return html

def md_to_post(file):

    html = markdown.markdown(open('raw/' + file).read(), extensions=['fenced_code'])



    html = f"""<div style="margin: 0 auto; width: 850px;
                border: 1px solid black; padding: 50px;
                margin-top: 100px; text-align: left;
                font-size: 14px">
                {html}
                </div>
                 """

    return html
