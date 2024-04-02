import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            #model_path=os.path.join("artifacts","model.pkl")
            #preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path = "artifacts\model.pkl"
            preprocessor_path = 'artifacts\proprocessor.pkl'
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(  self,
        Age: str,
        TypeofContact: str,
        CityTier:float,
        Occupation: int,
        Gender: int,
        NumberOfPersonVisiting: int,
        PreferredPropertyStar: int,
        MaritalStatus: float,
        NumberOfTrips: float,
        Passport: float,
        NumberOfChildrenVisiting: float,
        Designation: float,
        MonthlyIncome: float
        ):

        self.Age = Age

        self.TypeofContact = TypeofContact

        self.CityTier = CityTier

        self.Occupation = Occupation

        self.Gender = Gender
        
        self.NumberOfPersonVisiting = NumberOfPersonVisiting

        self.PreferredPropertyStar = PreferredPropertyStar

        self.MaritalStatus = MaritalStatus
        
        self.NumberOfTrips = NumberOfTrips

        self.Passport = Passport

        self.NumberOfChildrenVisiting = NumberOfChildrenVisiting

        self.Designation = Designation

        self.MonthlyIncome = MonthlyIncome


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.Age],
                "TypeofContact": [self.TypeofContact],
                "CityTier": [self.CityTier],
                "Occupation": [self.Occupation],
                "Gender": [self.Gender],
                "NumberOfPersonVisiting": [self.NumberOfPersonVisiting],
                "PreferredPropertyStar": [self.PreferredPropertyStar],
                "MaritalStatus": [self.MaritalStatus],
                "NumberOfTrips": [self.NumberOfTrips],
                "Passport": [self.Passport],
                "NumberOfChildrenVisiting": [self.NumberOfChildrenVisiting],
                "Designation": [self.Designation],
                "MonthlyIncome": [self.MonthlyIncome]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)