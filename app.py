import ui
from dbqueries import *


def list_mentors():
    head = ['First Name', 'Last Name']
    table = list_name_of_mentors()
    ui.print_table(table, head)


def list_mentor_by_city():
    inputs = ui.get_inputs(['Please specify the city: '])
    city_name = inputs[0]
    head = ['Nick Name']
    table = get_mentor_by_city(city_name)
    ui.print_table(table, head)


def get_info():
    inputs = ui.get_inputs(['Please specify the first name: '])
    first_name = inputs[0]
    head = ['Full Name', 'Phone Number']
    table = get_applicant_info(first_name)
    for item in table:
        info_list = [[item[0] + ' ' + item[1], item[2]]]
    ui.print_table(info_list, head)