from flask import Flask,render_template,redirect,request
from src.pipelines.predict_pipeline import  *

application=Flask(__name__)

@application.route("/")
def home_page():
    return render_template("index.html")

@application.route("/predict",methods=["GET", "POST"])
def predict_pipeline():
    if request.method == "GET":
        return render_template("index.html")
    else:
        data=custom_data(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_As_dataframe()
        print(pred_df)
        print("Before Prediction")

        predict_pipelin=pipeline_1()
        print("Mid Prediction")
        results=predict_pipelin.predict_pipeling(pred_df)
        print("after Prediction")
        return render_template('index.html',results=results[0])




if __name__=="__main__":
    application.run(debug=True)