from flask import Flask, request, jsonify
import utility
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/predict_heating_load', methods=['POST','GET'])
def predict_heating_load():
    
    relative_compactness = float(request.form['relative_compactness'])
    wall_area = float(request.form['wall_area'])
    roof_area = float(request.form['roof_area'])
    overall_height = float(request.form['overall_height'])
    orientation= int(request.form['orientation'])
    glazing_area= float(request.form['glazing_area'])
    glazing_area_distribution= int(request.form['glazing_area_distribution'])

    heating_load_array = utility.get_estimated_heating_load(relative_compactness, wall_area, roof_area, overall_height,orientation, glazing_area, glazing_area_distribution)

    # Convert the NumPy array to a list of standard Python floats
    heating_load_list = heating_load_array.tolist()

    # Create a response using jsonify with the converted list
    response = jsonify({'Heating_Load': heating_load_list})

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

    cooling_load_array = utility.get_estimated_heating_load(relative_compactness, wall_area, roof_area, overall_height,orientation, glazing_area, glazing_area_distribution)

    # Convert the NumPy array to a list of standard Python floats
    cooling_load_list = cooling_load_array.tolist()

    # Create a response using jsonify with the converted list
    response = jsonify({'Cooling_Load': cooling_load_list})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/hello')
def hello():
    return "Hi!"

if __name__ == "__main__":
    print("Starting Python Flask Server For Room Energy Efficiency Prediction...")
    utility.load_saved_models()
    app.run(debug=True)


