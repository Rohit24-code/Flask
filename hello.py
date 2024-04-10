# First we imported the Flask class. An instance of this class will be our WSGI application.
from flask import Flask;

from markupsafe import escape;


# Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
app=Flask(__name__)

# We then use the route() decorator to tell Flask what URL should trigger our function.




@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"

# now you can run using flask --app hello run 
# you can debug it using --debug at last 




# When returning HTML (the default response type in Flask), any user-provided values rendered in the output must be escaped to protect from injection attacks. HTML templates rendered with Jinja, introduced later, will do this automatically.

# escape(), shown here, can be used manually. It is omitted in most examples for brevity, but you should always be aware of how you’re using untrusted data.


@app.route('/user/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"

