from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pandas as pd
import json
from resources.preprocessing import preprocessing, get_input
from resources.fuzzy import fuzzification, inference, defuzzification

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
  return jsonify({"message": "kelayakan-pinjaman"})

@app.route('/dataset')
@cross_origin()
def dataset():
  ds = pd.read_csv("dataset/dataset.csv")
  ds = ds.to_json(orient='records')
  ds = json.loads(ds)
  return jsonify({"dataset": ds})

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
  data = request.get_json()
  pendapatan, usia, tanggungan, pengeluaran, aset = get_input(data)
  rules = preprocessing(pd.read_csv("dataset/dataset.csv"))

  fuzzification_values = fuzzification(pendapatan, usia, tanggungan, pengeluaran, aset)
  z, a = inference(fuzzification_values, rules)
  result = round(defuzzification(z, a), 2)

  return jsonify({"result": result})

if __name__ == '__main__':
  app.run()