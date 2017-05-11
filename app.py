import ui
from dbqueries import *

def list_mentors():
    head = ['First Name', 'Last Name']
    table = list_name_of_mentors()
    ui.print_table(table, head)