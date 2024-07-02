import sys
import pandas as pd
from source.commons import load_object
from source.exception import UserException
from source.logger import logging

class PredicPipeline:
    def __init__(self):
        pass
    
    logging.info('Preprocessing user input and making predictions')
    def predict(self,features):
        model_path = 'elements\model.pkl'
        scaler_path = 'elements\scaler.pkl'
        # loaeding objects
        model = load_object(model_path)
        scaler = load_object(scaler_path)
        data_scaled = scaler.transform(features)
        prediction = model.predict(data_scaled)
        
        return prediction
logging.info('This class is responsible for mapping all the inputs from html to flask')
class UserData:
    def __init__(self,
                 coursecategory,timespentoncourse,numberofvideoswatched,
                 numberofquizzestaken,quizscores,completionrate,devicetype):
        self.cat = coursecategory
        self.time = timespentoncourse
        self.vid = numberofvideoswatched
        self.quiz = numberofquizzestaken
        self.score = quizscores
        self.rate = completionrate
        self.device = devicetype
        
    # let's write a function that returns the user input as a numpy array
    def get_data_as_df(self):
        try:
            user_data = {
                "coursecategory":[self.cat],
                "timespentoncourse":[self.time],
                "numberofvideoswatched":[self.vid],
                "numberofquizzestaken":[self.quiz],
                "quizscores":[self.score],
                "completionrate":[self.rate],
                "devicetype":[self.device]
            }
            return pd.DataFrame(user_data)
        except Exception as e:
            raise UserException(e,sys)
        