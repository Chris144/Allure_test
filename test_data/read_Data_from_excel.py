import os

import pandas as pd


class ReadFile:
    @staticmethod
    def read_file(file_path):
        # Reading data from file excel
        df = pd.read_excel(file_path)
        df = pd.DataFrame(df, columns=["username_email", "password"])
        df = df.fillna('')
        return df.values.tolist()

    @staticmethod
    def get_test_data(index):
        # Get the absolute path of the test data file
        script_dir = os.path.dirname(__file__)
        data_file_path = os.path.join(script_dir, '../test_data/DDT.xlsx')
        data_values = ReadFile.read_file(data_file_path)
        if index < len(data_values):
            return data_values[index]
        else:
            return None
