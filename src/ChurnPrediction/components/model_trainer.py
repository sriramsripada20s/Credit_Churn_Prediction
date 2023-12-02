import pandas as pd
import os
from src.ChurnPrediction import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.ChurnPrediction.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        #convert your target variable to a 1D array using the ravel()
        train_y = train_data[self.config.target_column].values.ravel()
        test_y = test_data[self.config.target_column].values.ravel()

        

        rf = RandomForestClassifier(max_depth=self.config.max_depth, min_samples_leaf=self.config.min_samples_leaf, n_estimators = self.config.n_estimators, random_state=42)
        rf.fit(train_x, train_y)

        joblib.dump(rf, os.path.join(self.config.root_dir, self.config.model_name))