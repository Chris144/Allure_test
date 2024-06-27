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
        # Checking if index is less than data and returning the value at the given index
        data_values = ReadFile.read_file(
            "../test_data/DDT.xlsx")
        if index <= len(data_values):
            return data_values[index]
        else:
            return None
