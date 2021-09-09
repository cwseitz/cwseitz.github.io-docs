import pandas as pd

def excel_to_html(file):

    posts = pd.read_excel(file)
    posts['link'] = '<a href="' + posts['filename'] + '/' + posts['filename'] + '">' + posts['title'] + '</a>'
    del posts['filename']; del posts['title']

    #posts = posts.reindex(sorted(posts.columns), axis=1)
    posts = posts.reindex(['link', 'subject'], axis=1)
    posts = posts.fillna('')
    cols = posts.columns

    html = posts.to_html(justify='left', index=False, escape=False)
    html = html.replace('border="1"','border="0" id="myTable"')
    html = html.replace('<th>link</th>', '<th onclick="sortTable(0)">Title</th>')
    html = html.replace('<th>subject</th>', '<th onclick="sortTable(1)">Subject</th>')
    # #html = html.replace('<th>group</th>', '<th onclick="sortTable(2)">Group</th>')
    # html = html.replace('<th>type</th>', '<th onclick="sortTable(2)">Type</th>')

    return html

def generate_budget(expense_table, d0, d1, initial_amount=0):

    date_range = d1 - d0
    #ints = np.arange(np.round(expense_table['period'].min()), dtype=np.int32)

    delta = timedelta(days=1)
    amount = initial_amount

    for i in range(date_range.days):
        d0 += delta
        expenses = []

        #every day, iterate through expenses
        for index, row in expense_table.iterrows():

            #check if its an integer multiple of the period
            ls = row['dom'].split(',')
            ls = [int(x) for x in ls]

            if d0.day in ls:
                #check if it is between start and end dates
                if i >= row['start'] and i < row['end']:
                    amount += row['amount']
                    expenses.append(row['name'])

        print(d0.strftime("%Y-%m-%d"), f'Expenses: {expenses},  Balance: {amount}')

def run_budget_app():
    expense_table = pd.read_csv('budget.csv')
    initial_amount = 18750
    d0 = date(2021, 9, 26)
    d1 = date(2022, 3, 26)
    date_range = d1-d0

    print('#########################################################################')
    print(f'Generating Budget for {d0.strftime("%Y-%m-%d")} to {d1.strftime("%Y-%m-%d")} ({date_range.days} days)')
    print('#########################################################################')
    print(expense_table)
    print('\n\n\n')
    generate_budget(expense_table, d0, d1, initial_amount=initial_amount)
