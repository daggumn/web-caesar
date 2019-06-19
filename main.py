from flask import Flask, request
from caesar import rotate_string
import format


app = Flask(__name__)
app.config['DEBUG'] = True


form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
           
        </style>
    </head>
    <body>
      <html>
    <body>
        <form action = "/encrypt" method="post">
            <label for= "rotate by">Rorate by:</label>
            <input type="text" name="Rotate_by" value="0"/>
            <br><br>
            <textarea rows="10" cols="30"></textarea>
            <br><br>
            <input type= "Submit" value= "Submit Query"/>
        </form>
    </body>
</html>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/encrypt", methods=['POST'])   
def Rotate_string(): 
    encrypt = request.form['Rotate_by']
    return '<h1>Rotate_string, '+ encrypt + '<h1>'
app.run()
