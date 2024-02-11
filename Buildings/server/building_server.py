from flask import Flask,request,jsonify
import util
app= Flask(__name__)

@app.route('/get_facility_type', methods= ['GET'])
def get_facility_type():
    response = jsonify({
        'facility_type': util.get_facility_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_site_eui', methods=['GET', 'POST'])
def predict_site_eui():

    year_factor= float(request.form['year_factor'])
    facility_type= request.form['facility_type']
    floor_area= float(request.form['floor_area'])
    elevation= float(request.form['elevation'])
    avg_temp= float(request.form['avg_temp'])
    cooling_degree_days= float(request.form['cooling_degree_days'])
    heating_degree_days=float(request.form['heating_degree_days'])
    precipitation_inches=float(request.form['precipitation_inches'])


    response = jsonify({
        'site-eui': util.get_estimated_site_eui(facility_type,year_factor,floor_area,elevation,avg_temp,cooling_degree_days,heating_degree_days,precipitation_inches)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()