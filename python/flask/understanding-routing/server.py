from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/") # The "@" decorator associates this route with the function immediately following

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:message>")
def say(message):
    return message

@app.route("/repeat/<string:message>/<int:amount>")
def repeat(message, amount):
    return message * amount

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# python -m pipenv <command to use>