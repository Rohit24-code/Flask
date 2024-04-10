from flask import Flask, render_template , request


app = Flask(__name__)

@app.route("/")
def index():
    print(request.args)
    # if "name" in request.args:
    #     name=request.args["name"]
    # else : name="world"


    # In place of writing all this we can do
    name=request.args.get("name","world")
    return render_template("index.html",name=name)