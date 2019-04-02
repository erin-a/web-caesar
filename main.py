from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

def form():
    <!DOCTYPE html>

    <html>
        <head>
            <stlye>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    ,argom: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </stlye>
        </head>
        <body>"""
            #create form here
            """
        </body>
        </html>


@app.route("/")
def index():
    return "Hello World"



app.run()