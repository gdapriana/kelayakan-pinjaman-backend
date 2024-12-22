import json

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from resources.fuzzy import defuzzification, fuzzification, inference
from resources.member import get_member
from resources.preprocessing import get_input, preprocessing

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
@cross_origin()
def home():
    return jsonify({"message": "kelayakan-pinjaman"})


@app.route("/dataset")
@cross_origin()
def dataset():
    row = request.args.get("row")

    try:
        if row is None:
            row = 10
        row = int(row)
    except ValueError:
        return jsonify({"message": "wrong input"})

    ds = pd.read_csv("dataset/dataset2.csv")
    take_many = ds.head(row)
    true_label = len(ds[ds["Kelayakan"] == "layak"])
    false_label = len(ds[ds["Kelayakan"] == "tidak layak"])
    take_many = take_many.to_json(orient="records")
    total = len(ds)
    take_many = json.loads(take_many)
    return jsonify(
        {
            "dataset": take_many,
            "total": total,
            "true_label": true_label,
            "false_label": false_label,
        }
    )


@app.route("/member")
@cross_origin()
def member():
    meber = get_member()
    return jsonify({"member": meber})


@app.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    data = request.get_json()
    pendapatan, usia, tanggungan, pengeluaran, aset, durasi_peminjaman = get_input(data)
    rules = preprocessing(pd.read_csv("dataset/dataset2.csv"))

    fuzzification_values = fuzzification(
        pendapatan, usia, tanggungan, pengeluaran, aset, durasi_peminjaman
    )
    z, a = inference(fuzzification_values, rules)
    result = round(defuzzification(z, a), 2)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run()
