from flask import Flask, render_template
import sqlite3
import base64
from wtforms import SelectField
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2e1f5442ad15d0bde5f839f34c944b99'

# SQL operators
conn = sqlite3.connect('week10.db')
c = conn.cursor()
query = c.execute("SELECT * FROM Lab10")
rows = c.fetchall()

studentsList = []
for row in rows:
    studentsList.append([row[4], row[2], row[3], str(base64.b64decode(row[1]))[2:-1]])

selectList = [("", "Select a Student")]
for name in studentsList:
    selectList.append((name[3], name[0]))


class StudentForm(FlaskForm):
    formValue = SelectField("Select Student", choices=selectList)


@app.route('/')
def init():
    return render_template("default.html", the_title="My Title")


@app.route('/findStudent')
def findStudent():
    form = StudentForm()
    return render_template('findStudent.html', studentsForm=form, the_title="Find Student")


@app.route('/displayAll')
def displayAll():

    return render_template('displayAll.html', studentsList=studentsList, the_title="Display All")


if __name__ == '__main__':
    app.run(debug=True)