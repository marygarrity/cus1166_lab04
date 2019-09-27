from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#This route should display a static welcome message. The message should be defined in the template index.html
def index():
    return render_template("index.html")

@app.route('/welcome/<string:student_name>') # @app.route or @route ?
#This message should display a welcome message that includes the student_name specified in the route. The route should render the template welcome.html
def welcome(student):
    return render_template("welcome.html", student=student)

class_roster = [
    ('Richard', 'A', 'Sophomore'),
    ('Kate', 'B', 'Junior'),
    ('Emma', 'A-', 'Freshmen'),
    ('Tiffany', 'B+', 'Senior'),
    ('Liz', 'C+', 'Sophomore'),
    ('Mel', 'F', 'Senior'),
    ('Jane', 'C', 'Junior'),
    ('Matt', 'B', 'Senior'),
    ('Rachel', 'A-', 'Sophomore'),
    ('John', 'B+', 'Freshman')]

@app.route('/roster/<int:grade_view>') # @app.route or @route ?
#To implement this route you need to first define a global variable that stores a list of tuples -
#name this variable class_roster . Each tuple in the list must have three elements; a
#student's name, a student's grade and a student's class standing (i.e. 'Freshman',
#'Sophomore', junior', 'Senior'). Populate this variable with student information (create at
#least 7 student entries, use dummy data).
#This route should render the template roster.html. The class_roster variable, and the
#route variable (i.e. grade_view ) should be passed as arguments to the template. The
#template must display a list of all students in the roster as follows:
#If grade_view==1 then list only the student's name, and grade.
#If grade_view==2 the list only the student's name, and it's class standing.
#if 'grade_view==0' the list all available information about a student.
#You must use the {% for %} and % if % template instructions.
def roster(grade_view):
    return render_template("roster.html", grade_view=grade_view, class_roster=class_roster)
'''
if grade_view == 0: #the list all available information about a student
    print(student_name, student_grade, student_class_standing)

if grade_view == 1: #then list only the student's name, and grade
    print(student_name, student_grade)

if grade_view == 2: #the list only the student's name, and it's class standing
    print(student_name, student_class_standing)
'''
