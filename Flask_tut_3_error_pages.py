from flask import Flask, render_template
app = Flask(__name__)

# FILTERS - Few Main Filters - jinja2
# * safe 
#    - say need to pass text to html page, its tricky because hackers
#    can put some weired code in to inject some code, so flask will strip out that code, not to do that
#    we use safe to append our code.
# * capitalize
# * lower
# * upper
# * title
#   - First letter of every word is capitalized.
# * trim
#   - This will remove trailing spaces at the end.
# * striptags
#   - It will strip any html tags completely, wont ignore will remove them.

@app.route('/')
def index():
    first_name = "Sonu"
    stuff_title = "personal introduction for webpage"
    stuff_safe = "This is <strong> Bold </strong> text!"
    stuff_strip = "This is <strong> Strong </strong> text!"
    fav_pizza = ["pepperoni","cheese","mushroom",41]
    return render_template('indextut.html', 
                           first_name=first_name,
                           stuff_title=stuff_title,
                           stuff_safe=stuff_safe,
                           stuff_strip=stuff_strip,
                           fav_pizza=fav_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# create custom error pages

# Invalid URL - error 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error - error 500

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)