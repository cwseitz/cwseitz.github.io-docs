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
