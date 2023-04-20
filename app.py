from flask import Flask, render_template

app = Flask(__name__)


# defining home page
@app.route('/')
def home():
    return render_template('home.html')


# defining direction page
@app.route('/direction')
def direction():
    return render_template('direction.html')

# defining 3dview page
@app.route('/view_3d')
def view_3d():
    return render_template('view_3d.html')

# defining dummy3d view page
@app.route('/dummy_3d')
def dummy_3d():
    return render_template('dummy_3d.html')

# defining street view page
@app.route('/street_view')
def street_view():
    return render_template('street_view.html')

# defining driving page
@app.route('/driving')
def driving():
	return render_template('driving.html')

# defining indoor room page
@app.route('/indoor')
def indoor():
	return render_template('indoor.html')

# defining indoor room page
@app.route('/car')
def car():
	return render_template('car.html')

# defining map direction
@app.route('/map_dir')
def map_dir():
    return render_template('map_dir.html')

# defing search
@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)




