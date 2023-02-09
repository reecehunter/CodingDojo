from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play/<int:amount>/<string:color>')          # The "@" decorator associates this route with the function immediately following
def play(amount, color):
    return render_template("play.html", amount=amount, color=color)  # Return the string 'Hello World!' as a response

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# python -m pipenv <command to use>