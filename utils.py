from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np

def get_data_from_file(inputFile):
	data = pd.read_csv(inputFile, delimiter='|', header=0)
	data = data.interpolate()
	data = data.fillna(method ='ffill')
	data = data.fillna(data.mean())
	data = data.fillna(0)

	return data


def prepare_test_data_random_forest(data):
	features = d_to_features2(data)
	return features

# def prepare_input_for_random_forest(all_training_data, is_training=False):
	
# 	all_data_features = []
# 	all_labels = []
# 	for idx, training_data in enumerate(all_training_data):
# 		num_row = training_data.shape[0]
# 		for i in range(num_row):
# 			# features_map =  d_to_features(training_data, i, mean_values=None, std_values=None, min_values=None, max_values=None)
# 			if  is_training:
# 				label = training_data.loc[i, 'SepsisLabel']
# 			else: 
# 				label = 0
# 			# features_values = features_map.values()
# 			# all_data_features.append(features_values)
# 			all_data_features.append(d_to_features2(training_data, i, mean_values=None, std_values=None, min_values=None, max_values=None))
# 			all_labels.append(label)
# 		#if idx%100==0:
# 		#	print("Finished ", idx)
# 	return all_data_features, all_labels


def d_to_features2(training_data):
	l = training_data.shape[0]
	data = training_data[l-1]
	
	if l > 0:
		prev_data = training_data[l-2]
	else:
		prev_data = data
	if l > 1:
		prev2_data = training_data[l-3]
	else:
		prev2_data = prev_data
	if l> 2:
		prev3_data = training_data[l-4]
	else:
		prev3_data = prev2_data

	if l > 3:
		prev4_data = training_data[l-5]
	else:
		prev4_data = prev3_data

	if l > 4:
		prev5_data = training_data[l-6]
	else:
		prev5_data = prev4_data
	features = []
	features.extend(data.tolist())
	features.extend(prev_data.tolist())
	features.extend(prev2_data.tolist())
	features.extend(prev3_data.tolist())
	features.extend(prev4_data.tolist())
	features.extend(prev5_data.tolist())
	return features


def impute_missing_data(data):
	df = pd.DataFrame(data=data)
	df = df.interpolate()
	df = df.fillna(method ='ffill')
	df = df.fillna(df.mean())
	df = df.fillna(0)

	return df.values