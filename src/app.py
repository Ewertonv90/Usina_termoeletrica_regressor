from flask import Flask, request
import mlflow
import pandas as pd


app = Flask(__name__)

@app.route('/predict_ccpp', methods=['POST'])

def index():
    data_json = request.get_json()
    data_json = data_json['data']
    df = pd.DataFrame.from_dict(data_json)

    mlflow.set_experiment('Usina')
    last_run = dict(mlflow.search_runs().sort_values(by='start_time', ascending=False).iloc[0])
    artifact_uri = last_run['artifact_uri']
    model = mlflow.sklearn.load_model(artifact_uri+'/model_pipeline')
    
    predictions = model.predict(df)

    return {"Power Prediciton" : predictions[0]}

if __name__ == '__main__':
 app.run(debug=True) 