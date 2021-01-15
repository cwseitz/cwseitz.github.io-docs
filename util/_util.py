import pandas as pd

def excel_to_html(file):

    posts = pd.read_excel(file)
    posts['link'] = '<a href="' + posts['filename'] + '">' + posts['title'] + '</a>'
    del posts['filename']; del posts['title']
     
    #posts = posts.reindex(sorted(posts.columns), axis=1)
    posts = posts.reindex(['link', 'subject', 'type'], axis=1)
    posts = posts.fillna('')
    cols = posts.columns

    html = posts.to_html(justify='left', index=False, escape=False)
    html = html.replace('border="1"','border="0" id="myTable"')
    html = html.replace('<th>link</th>', '<th onclick="sortTable(0)">Title</th>')
    html = html.replace('<th>subject</th>', '<th onclick="sortTable(1)">Subject</th>') 
    #html = html.replace('<th>group</th>', '<th onclick="sortTable(2)">Group</th>')
    html = html.replace('<th>type</th>', '<th onclick="sortTable(2)">Type</th>')
    
    return html
