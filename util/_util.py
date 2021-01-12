import pandas as pd

def excel_to_html(file):

    posts = pd.read_excel(file)
    posts = posts.fillna('')
    cols = posts.columns

    #for col in cols:
    #    posts[col] = posts[col].apply(lambda x: '<a href="{0}/index.html">{0}</a>'.format(x))

    html = posts.to_html(justify='left', index=False, escape=False)
    html = html.replace('border="1"','border="0"')

    return html
