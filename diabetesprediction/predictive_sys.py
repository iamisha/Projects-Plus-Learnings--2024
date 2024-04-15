import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('/home/isha/Documents/PythonProject2024/diabetesprediction/diabetes_model.sav', 'rb'))

# predicting system output
input_data = (3,78,50,32,88,31,0.248,26)

# changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('the person is not diabetic')
else:
  print('the person is diabetic')