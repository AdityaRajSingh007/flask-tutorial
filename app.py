from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses = ['python', 
               'flask', 
               'fastAPI']
    student = {'name' : 'Aditya', 
               'course' : 'flask'}
    return render_template("index.html", courses = courses, student=student)

if __name__ == '__main__': 
    app.run(debug=True)