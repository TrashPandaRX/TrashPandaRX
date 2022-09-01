# this module is to be used in conjunction with one of the "mare.bot"s and "profile_builders" of the xseries
import pandas as pd
import numpy as np
import xarray as xr
import os

class automator:

    # IMPORTANT each kwargs should be a separate xr.dataarray or xr.dataset.dataarray
    def __init__(self, **kwargs):
        self.proflies = []

        # will need data from the largest profile like:
        # number of indicies, number of columns, 
        largest_profile_params = {
            'name': str,
            'indicies' : 0,
            'columns' : 0,
            'data' : pd.DataFrame()
        }
        print("\n\n->***REVEALING KWARGS***<-\n\n")
        print(kwargs.keys())

        # adjusted at 10:57am so that its more based on pandas atm
        # why the fuck is this shit still name kwargs...
        for profile_type, actual_profile in zip(kwargs.keys(),kwargs.values()):
            self.proflies.append(actual_profile)
            print("outside if comparator")
            if len(actual_profile) > largest_profile_params['indicies']:
                print("inside if comparator")
                print(profile_type)
                print(actual_profile)
                largest_profile_params['name'] = profile_type

                # last debugged sept 1 at 10:13am
                # cant use .shape.x or shape.y because they are tuples and actual profile has these coded under the dimensions.
                # that is to say...instead of doing .shape.x do .shape[0] and .shape[1] for .y
                # also dropped the len() because the new change to the code already yields ints
                largest_profile_params['indicies'] = actual_profile.shape[0] # number of indicies in this dataarray --> # formely had actual_profile.shape.x but that didnt work because i was treating the dict as a dataframe. instead of it holding the dataframes
                largest_profile_params['columns'] = actual_profile.shape[1] # number of columns in this dataarray
                largest_profile_params['data'] = actual_profile
        '''
        for profile_type in kwargs:
            self.proflies.append(profile_type)
            if len(profile_type) > largest_profile_params['indicies']:
                print(profile_type)
                largest_profile_params['name'] = profile_type.name
                largest_profile_params['indicies'] = len(profile_type.dim_0) # number of indicies in this dataarray
                largest_profile_params['columns'] = len(profile_type.dim_1) # number of columns in this dataarray
                largest_profile_params['data'] = profile_type
        '''


    
        self.profile_standard = largest_profile_params

    # forcefully upscale all other dataarrays dimensions up to the dimensions of the 'largest profile'
    # then return the freshly rescaled results
    def scale_profiles_to_largest(self, ):
        # alright so xarray.Dataarray is being a little **** so
        # im going to just have to take the old dataarray
        # and create a new one based off of it...
        dataset = xr.Dataset()
        updated_arrays = {
            'default' : self.profile_standard['data']
        }

        for profile_type in self.proflies:
            print(type(profile_type))
            # skip if this profile is the same as the one being used as the golden standard
            if profile_type.name is self.profile_standard['name']:
                print('found the biggie!')
                continue
            else:
                # reforge the profile_type with the dimensions of the profile_standard
                # while retaining the data and adding new indicies to match the standard.
                
                # remember index and columns need list-like values which is why arange is good
                upgraded_array = pd.DataFrame(profile_type, index = np.arange(self.profile_standard['indicies']), columns = np.arange(self.profile_standard['columns']))
                print(upgraded_array)
                


                #updated_arrays[''] = upgraded_array

            # does this look at each key value pair or is it just the key? or just the value?
            # TODO
            '''
            for array in updated_arrays:
                dataset[] = array
            
            return dataset
            '''

# testing setup
if __name__ == '__main__':
    profile_builder_dir = os.getcwd()
    name_of_folder_containing_profile_data = "test folder"
    profile_data_path = os.path.join(profile_builder_dir, name_of_folder_containing_profile_data)
    
    csv_profiles = ['gaming', 'dating', 'default', 'mental']
    dictionary_of_profiles = dict()

    for file, name  in zip(os.listdir(profile_data_path), csv_profiles):
        print(file)
        dictionary_of_profiles[name] = pd.read_csv(f"{profile_data_path}/{file}", index_col=[0])

    for key,value in zip(dictionary_of_profiles.keys(), dictionary_of_profiles.values()):
        print(f"{key} : {value}")

    dictionary_of_profiles['default']

    # testing
    # i think i fucked up with how i passed the dictionary into the constructor for KWARGS to be used...
    # maybe i should be using key value pairs to bring the dictionary elements in
    # instead of a full fucking dictionary.
    initializer = automator(**dictionary_of_profiles)   # THIS WAS WRONG



    '''
    # initializer = automator(kwargs = dictionary_of_profiles)   # THIS WAS WRONG
    # basically what i had before was a KEY named kwargs, that contained the dictionary, 'dictionary_of_profiles'
    # which meant that kwargs whenever i referred to it later on, was literally just the string-key to the dictionary-value
    # example for my dumb ass:
    def sample_kwarg(**kwargs):
        print(kwargs)
        print(type(kwargs))

    sample_kwarg(kwargs = sample_dict)  

    # returns the following
    {'kwargs': {'name': 'rory', 'age': 22, 'height': 162, 'weight': 140}}
    <class 'dict'>
    '''          