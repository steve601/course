from flask import Flask,request,render_template
from source.logger import logging
from source.main_project.pipeline.predict_pipeline import PredicPipeline,UserData

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('course.html')

@app.route('/predict',methods=['POST'])
def do_prediction():
    user_inputs = UserData(
        coursecategory=request.form.get('cat'),
        timespentoncourse=request.form.get('time'),
        numberofvideoswatched=request.form.get('vid'),
        numberofquizzestaken=request.form.get('quiz'),
        quizscores=request.form.get('score'),
        completionrate=request.form.get('rate'),
        devicetype=request.form.get('rate')
    )
    
    user_df = user_inputs.get_data_as_df()
    logging.info('Doing prediction')
    
    pred_pipe = PredicPipeline()
    prediction = pred_pipe.predict(user_df)
    
    msg = 'Course completed!!' if prediction == 1 else 'Course not completed'
    
    return render_template('course.html',text = msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0")