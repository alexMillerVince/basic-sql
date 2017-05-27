import ui
from random import randint
from dbqueries import *


def generate_applicant_code():
    application_codes = get_custom_attributes('applicants', 'application_code')
    while True:
        new_application_code = randint(10000, 99999)
        for item in application_codes:
            if item != new_application_code:
                return new_application_code


def list_mentors():
    head = ['First Name', 'Last Name']
    table = list_name_of_mentors()
    ui.print_table(table, head)


def get_nickname_by_city():
    inputs = ui.get_inputs(['Please specify the city: '])
    city_name = inputs[0]
    head = ['Nick Name']
    table = get_mentors_by_city(city_name)
    ui.print_table(table, head)


def get_info():
    inputs = ui.get_inputs(['Please specify the first name: '])
    first_name = inputs[0]
    head = ['Full Name', 'Phone Number']
    table = get_applicant_info(first_name)
    info_list = list()
    for item in table:
        info_list = [[item[0] + ' ' + item[1], item[2]]]
    ui.print_table(info_list, head)


def get_info_by_email():
    inputs = ui.get_inputs(['Please specify the email: '])
    email = inputs[0]
    head = ['Full Name', 'Phone Number']
    table = get_applicant_info_by_email(email)
    info_list = list()
    for item in table:
        info_list = [[item[0] + ' ' + item[1], item[2]]]
    ui.print_table(info_list, head)


def add_applicant():
    ui.print_message('Give the applicant attributes (first name, last name , phone number, email)')
    inputs = ui.get_inputs([': '])
    inputs.append(generate_applicant_code())
    head = ['id','First Name', 'Last Name', 'Phone Number', 'Email', 'Application Code']
    table = add_new_applicant(inputs)
    ui.print_table(table, head)


def add_given_applicant():
    try:
        applicant_info = ['Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823]
        head = ['id', 'First Name', 'Last Name', 'Phone Number', 'Email', 'Application Code']
        table = add_new_applicant(applicant_info)
        ui.print_table(table, head)
    except psycopg2.IntegrityError:
        ui.print_error_message('An applicant with this application code already exists.')


def update_give_applicant():
    head = ['Phone Number']
    table = update_applicant_phone_number(['Jemima', 'Foreman'], '003670/223-7459')
    ui.print_table(table, head)


def remove_given_applicant():
    ui.print_message(remove_applicant('@mauriseu.net'))
