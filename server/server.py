from flask import Flask,request,jsonify
import util


app=Flask(__name__)

@app.route('/predict_crop',methods=['POST','GET'])
def predict_crop():
    state=request.form.get('State')
    rainfall=int(request.form.get('Rainfall'))
    season=request.form.get('Season')
    soil=request.form.get('Soil')

    response =jsonify({'predict_crop':util.predict_crop(state,rainfall,season,soil) })
    response.headers.add('Access-control-Allow-Origin', '*')
    return response

@app.route('/get_state_names')
def get_state_names():
    response=jsonify({
        'state':util.get_state_names()
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

@app.route('/get_soil_names')
def get_soil_names():
    response=jsonify({
        'soil':util.get_soil_names()
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response

@app.route('/predict_rop',methods=['POST','GET'])
def predict_rop():
    state="Andhra Pradesh"
    rainfall=4568
    season="Rabi"
    soil="Black"

    response =jsonify({'predict_crop':util.predict_crop(state,rainfall,season,soil) })
    response.headers.add('Access-control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    print("predict_crop done......")
    app.run()


