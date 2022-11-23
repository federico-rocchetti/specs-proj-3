from flask import Flask, render_template, redirect, flash, request, session
import jinja2
from melons import get_all, find_melon

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/melons')
def all_melons():
    melon_list = get_all()
    return render_template('melons.html', melon_list=melon_list)

@app.route('/melons/<melon_id>')
def melon_details(melon_id):
    melon = find_melon(melon_id)
    return render_template("individual-melon.html", melon=melon)

@app.route('/add_to_cart/<melon_id>')
def add_to_cart(melon_id):

    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']

    cart[melon_id] = cart.get(melon_id, 0) + 1
    session.modified = True

    flash(f"${melon_id} added to cart.")
    print(cart)

    return redirect('/cart')

@app.route('/cart')
def cart():
    order_total = 0
    cart_melons = []

    cart = session.get('cart', {})

    for melon_id, quantity in cart.items():
        melon = find_melon(melon_id)

        total_cost = quantity * melon.price
        order_total += total_cost

        melon.quantity = quantity
        melon.total_cost = total_cost

        cart_melons.append(melon)

    return render_template('cart.html', cart_melons=cart_melons, order_total=order_total)

@app.route('/empty-cart')
def empty_cart():
    session["cart"] = {}

    return redirect("/cart")

if __name__ == '__main__':
    app.env = "development"
    app.run(debug = True, port = 8000, host = 'localhost')
