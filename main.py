from caesar import rotate_string
from flask import Flask,request
app = Flask(__name__)

app.config['DEBUG'] = True

form = """
        <html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
                    <!--create your form here--> 
                    <form action="/" method="POST">
                            <label>Rotate by:
                            <input type="text" name="rot" value="0"/>
                            </label>
                            <textarea name="text">{0}</textarea>
                            <input type="submit" value="Submit"/>

                    </form>   
                    </body>
            </html>
        """
@app.route("/")
def index():
    return form.format("")
    

@app.route("/", methods=['POST'])
def encrypt():
    rotate_by = int(request.form["rot"])
    text_area = request.form["text"]
    cypher = rotate_string(text_area,rotate_by)
    return form.format(cypher)
    


app.run()
