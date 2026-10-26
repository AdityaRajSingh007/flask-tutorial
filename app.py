from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = 'Aditya'
    course = ['Flask',
              'python',
              'FastAPI']
    city = 'Delhi'
    age = 29
    first_name = 'Aditya'
    last_name = 'Raj'
    return render_template("index.html", 
                           name=name,
                           course = course,
                           city = city,
                           age = age,
                           first_name = first_name,
                           last_name = last_name)

if __name__ == '__main__':
    app.run(debug=True)