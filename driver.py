# Sample driver file
from joblib import dump, load
import pandas as pd
from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import datasets
import pickle
from graph_generation import graph_generator
import numpy as np
from sklearn.model_selection import train_test_split

class FinalModel():
    
    def outliers_removal2(self, feature,feature_name,dataset):
        q25, q75 = np.percentile(feature, 25), np.percentile(feature, 75)
        feat_iqr = q75 - q25
    
        feat_cut_off = feat_iqr * 1.5
        feat_lower, feat_upper = q25 - feat_cut_off, q75 + feat_cut_off

        outliers = [x for x in feature if x < feat_lower or x > feat_upper]
        #print(feature_name + ' outliers:{}'.format(outliers))
        dataset = dataset.drop(dataset[(dataset[feature_name] > feat_upper) | (dataset[feature_name] < feat_lower)].index)
        return dataset

    def predict(self, dataset):
        stars_type = ['Red Dwarf','Brown Dwarf','White Dwarf','Main Sequence','Super Giants','Hyper Giants']
        stars_data['Class'] =  stars_data['Type'].replace(stars_data['Type'].unique(),stars_type)
        stars_data['Color'].loc[stars_data['Color'] =='Blue-white'] = 'Blue-White'
        stars_data['Color'].loc[stars_data['Color'] =='Blue White'] = 'Blue-White'
        stars_data['Color'].loc[stars_data['Color'] =='Blue white'] = 'Blue-White'
        stars_data['Color'].loc[stars_data['Color'] =='yellow-white'] = 'White-Yellow'
        stars_data['Color'].loc[stars_data['Color'] =='Yellowish White'] = 'White-Yellow'
        stars_data['Color'].loc[stars_data['Color'] =='white'] = 'White'
        stars_data['Color'].loc[stars_data['Color'] =='yellowish'] = 'Yellowish'
        data_cleaned = self.outliers_removal2(stars_data['L'],'L', dataset)
        num_feat = stars_data.drop(['Color','Spectral_Class','Type','Class'], axis = 1)
        cat_feat = stars_data.drop(['Temperature','L','R','A_M','Type','Class'], axis = 1)
        data_dummy = pd.get_dummies(cat_feat)
        scaler = MinMaxScaler()
        data_scaled = scaler.fit_transform(num_feat)
        data_scaled = pd.DataFrame(data_scaled, columns = num_feat.columns)
        data_complete = data_scaled.join(data_dummy)
        labels = stars_data['Class']

        # Splitting the data

        Xtrain,X_test,ytrain,y_test = train_test_split(data_complete,labels,
                                                    test_size = 0.1,
                                                    stratify = labels,
                                                    shuffle = True)


        X_train,X_val,y_train,y_val = train_test_split(Xtrain,ytrain,
                                                    test_size = 0.1,
                                                    stratify = ytrain,
                                                    shuffle = True)
        l_reg = LogisticRegression(random_state = 42)
        log_model = l_reg.fit(X_train,y_train)
        pred = log_model.predict(data_complete)
        stars_data['Class'] = pred
        stars_data.to_csv("Star_data_with_predictions.csv")

print("ML Algorithm: Begin")

stars_data = pd.read_csv('Stars.csv')
FinalModel3 = load('Star_Predict.joblib')
FinalModel3 = FinalModel3.predict(stars_data)

print("ML Algorithm: End")
print("Graph Generation: Begin")

graphs = graph_generator('Star_data_with_predictions.csv')
graphs.generate_histograms()
graphs.graph_values()

print("Graph Generation: End")