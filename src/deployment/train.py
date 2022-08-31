import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, r2_score 
from sklearn.preprocessing import PolynomialFeatures

import mlflow
from mlflow.models.signature import infer_signature

mlflow.set_experiment("Usina")

mlflow.start_run()

df = pd.read_csv('C:/Users/ewert/Desktop/Usina_termoeletrica_regressor/data/ccppa.csv')

sns.pairplot(df, diag_kind='hist')
plt.savefig('mlruns/pairplot.png')
mlflow.log_artifact('mlruns/pairplot.png')
plt.close()

sns.heatmap(df.corr(), annot=True)
plt.savefig('mlruns/heatmap.png')
mlflow.log_artifact('mlruns/heatmap.png')
plt.close()

X = df.drop(['PE'], axis=1)
y = df['PE']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)



pipeline = Pipeline(
    steps = [  
        ('imputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
        ('polynomial', PolynomialFeatures(degree=4)),
        ('linear_regressor', LinearRegression())
    ]
)


pipeline.fit(X_train, y_train)


y_pred_test = pipeline.predict(X_test)


mse = mean_squared_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)

mlflow.log_metric('MSE test', mse)
mlflow.log_metric('R2 test', r2)


y_pred_train = pipeline.predict(X_train)

r2 = r2_score(y_train, y_pred_train)
mse = mean_squared_error(y_train, y_pred_train)

mlflow.log_metric('MSE train', mse)
mlflow.log_metric('R2 train', r2)

params = pipeline.named_steps['linear_regressor'].get_params()

mlflow.log_params(params)

signature = infer_signature(X_test, y_pred_test)

mlflow.sklearn.log_model(pipeline, 'model_pipeline', signature=signature)

mlflow.end_run()

# mlflow.search_runs()

# last_run = dict(mlflow.search_runs().sort_values(by='start_time', ascending=False).iloc[0])

# artifact_uri = last_run['artifact_uri']

# model = mlflow.sklearn.load_model(artifact_uri+'/model_pipeline')

# model.predict(X_test)


