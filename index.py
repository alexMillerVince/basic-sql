from flask import Flask, render_template, request
import bll

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors():
    head_title = 'Mentors'
    head = ['Mentor Name', 'School Name', 'School Country']
    data = bll.get_mentors_and_school()
    return render_template('list.html', head=head, data=data, head_title=head_title)


@app.route('/all-school')
def all_school():
    head_title = 'All School'
    head = ['Mentor Name', 'School Name', 'School Country']
    data = bll.get_mentors_and_all_school()
    return render_template('list.html', head=head, data=data, head_title=head_title)


@app.route('/mentors-by-country')
def mentors_by_countryl():
    head_title = 'Mentors by country'
    head = ['Country', 'Number Of The Mentors']
    data = bll.mentors_by_country()
    return render_template('list.html', head=head, data=data, head_title=head_title)


@app.route('/contacts')
def contacts():
    head_title = 'Contacts'
    head = ['School Name', 'Contact Mentor']
    data = bll.get_contact_mentors()
    return render_template('list.html', head=head, data=data, head_title=head_title)


@app.route('/applicants')
def applicants():
    head_title = 'Mentors by country'
    head = ['First Name', 'Application Code', 'Creation Date']
    data = bll.get_applicants()
    return render_template('list.html', head=head, data=data, head_title=head_title)


if __name__ == '__main__':
    app.run(debug=True)