from conenct import *


def list_name_of_mentors():
    """
    returns the 2 name columns of the mentors table.
    :return: first_name, last_name
    """
    cursor = connect_to_db()
    cursor.execute("""SELECT first_name, last_name FROM mentors ORDER BY first_name ASC;""")
    rows = cursor.fetchall()
    return rows


def get_mentor_by_city(city):
    """
    returns the nick_name-s of all mentors working at a specific city.
    :param city: city name
    :return: nick_name
    """
    pass


def get_full_name(first_name):
    """
    returns the full_name-s and phone_number-s of an applicant by their first_name
    :param first_name: the first name of an applicant
    :return: full_name, phone_number
    """
    pass