import pickle

# create dictionary containing all your data
data = {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}
# save data in pickle format
with open('my_data.pickle', 'w') as f:
    pickle.dump(data, f)

# open data from file
with open('my_data.pickle', 'rb') as f:
    new_data_variable = pickle.load(f)

# now new_data_variable is equal to the dict {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}
