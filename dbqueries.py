from connenct import *


def list_name_of_mentors():
    """
    returns the 2 name columns of the mentors table.
    :return: first_name, last_name
    """
    cursor = connect_to_db()
    cursor.execute("""SELECT first_name, last_name FROM mentors ORDER BY first_name ASC;""")
    rows = cursor.fetchall()
    return rows


def get_mentors_by_city(city):
    """
    returns the nick_name-s of all mentors working at a specific city.
    :param city: name of city
    :return: nick_name
    """
    cursor = connect_to_db()
    cursor.execute("""SELECT nick_name FROM mentors WHERE city = '{}';""".format(str.capitalize(city)))
    rows = cursor.fetchall()
    return rows


def get_applicant_info(first_name):
    """
    returns the full_name-s and phone_number-s of an applicant by their first_name
    :param first_name: first name of an applicant
    :return: full_name, phone_number
    """
    cursor = connect_to_db()
    cursor.execute("""SELECT first_name, last_name, phone_number
    FROM applicants WHERE first_name = '{}';""".format(first_name))
    rows = cursor.fetchall()
    return rows


def get_applicant_info_by_email(email):
    """
    returns the full_name-s and phone_number-s of an applicant by their university.
    :param email: name of university
    :return: full_name, phone_number
    """
    cursor = connect_to_db()
    cursor.execute("""SELECT first_name, last_name, phone_number
    FROM applicants WHERE email LIKE '%{}%';""".format(str.lower(email)))
    rows = cursor.fetchall()
    return rows
