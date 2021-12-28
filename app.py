import re
from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def Predict():
    utils.load_saved_artifacts()
    locations, area_types = utils.get_location_and_areatype_names()
    if request.method == 'POST':
        sqft = request.form['size']
        bath = request.form['bathradio']
        balcony = request.form['balconyradio']
        bhk = request.form['bhkradio']
        location = request.form['loca']
        areatype = request.form['areatype']
        availaible = request.form['availaibility']
    try:
        price = round(utils.predict_price(areatype, availaible,location,bhk, sqft, bath, balcony),2)
        params = [sqft, bath, balcony, bhk, location, areatype, availaible]
    except:
        price = False
        params = None
    return render_template('index.html', locations=locations, area_types=area_types, price=price, params=params)

if __name__ == '__main__':
    app.run(debug=True)
