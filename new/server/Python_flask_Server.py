from flask import Flask, request, jsonify
import utility
import numpy as np
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)


@app.route('/predict_heating_load', methods=['POST','GET'])
def predict_heating_load():
    print("hi there!")
    relative_compactness = float(request.form['relative_compactness'])
    wall_area = float(request.form['wall_area'])
    roof_area = float(request.form['roof_area'])
    overall_height = float(request.form['overall_height'])
    orientation= int(request.form['orientation'])
    glazing_area= float(request.form['glazing_area'])
    glazing_area_distribution= int(request.form['glazing_area_distribution'])



    # Get the estimated heating load
    estimated_heating_load = utility.get_estimated_heating_load(relative_compactness, wall_area, roof_area, overall_height, orientation, glazing_area,glazing_area_distribution)

    # Convert any float32 values to regular floats
    if isinstance(estimated_heating_load, np.float32):
        estimated_heating_load = round(float(estimated_heating_load),2)
    # Create the JSON response
    response = jsonify({
        'estimated_heating_load': estimated_heating_load
    })

    #response = jsonify({
    #    'estimated_heating_load': utility.get_estimated_heating_load(relative_compactness, wall_area, roof_area, overall_height,orientation, glazing_area, glazing_area_distribution)
    #})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_cooling_load', methods=['POST','GET'])
def predict_cooling_load():
    
    relative_compactness = float(request.form['relative_compactness'])
    wall_area = float(request.form['wall_area'])
    roof_area = float(request.form['roof_area'])
    overall_height = float(request.form['overall_height'])
    orientation= int(request.form['orientation'])
    glazing_area= float(request.form['glazing_area'])
    glazing_area_distribution= int(request.form['glazing_area_distribution'])

    estimated_cooling_load = utility.get_estimated_cooling_load(relative_compactness, wall_area, roof_area, overall_height,orientation, glazing_area, glazing_area_distribution)

    if isinstance(estimated_cooling_load, np.float32):
        estimated_cooling_load = round(float(estimated_cooling_load), 2)
    # Create the JSON response
    response = jsonify({
        'estimated_cooling_load': estimated_cooling_load
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/hello')
def hello():
    return "Hi!"

if __name__ == "__main__":
    print("Starting Python Flask Server For Room Energy Efficiency Prediction...")
    utility.load_saved_models()
    app.run(debug=True)


