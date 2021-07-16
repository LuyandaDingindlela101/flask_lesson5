from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def shopping_list():
    return render_template('shopping_list.html')


@app.route("/showitems", methods=['POST'])
def show_items():
    product_details = {
        "name": request.form['name'],
        "item_id": request.form['item id'],
        "quantity": request.form['quantity'],
        "price": request.form['price']
    }

    return render_template("show_items.html", product_details=product_details)


# @app.route('/login', methods=['POST'])
# def login():
#     uname = request.form['username']
#     password = request.form['userpass']
#     if uname == "luyanda" and password == "1234":
#         return f"Welcome {uname}, the status code is: {request.method}"
#     else:
#         return f"Error in logging in, status code: {request.method}"


if __name__ == "__main__":
    app.run(debug=True)