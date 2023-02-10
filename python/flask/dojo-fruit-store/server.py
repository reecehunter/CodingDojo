from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    data = {
        "first_name": request.form["first_name"],
        "strawberries": request.form["strawberry"],
        "raspberries": request.form["raspberry"],
        "apples": request.form["apple"],
    }
    count = int(data["strawberries"]) + int(data["raspberries"]) + int(data["apples"])
    print(f"Charging {data['first_name']} for {count}")
    return render_template("checkout.html", data=data)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)