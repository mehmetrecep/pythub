import pandas as pd


class CSVReader:
    @staticmethod
    def read_csv(file_path, delimiter=',', na_values=None, dtype=None):
        """
        Reads a CSV file and returns a pandas DataFrame.

        Parameters:
        - file_path (str): The path to the CSV file.
        - delimiter (str): The delimiter used in the CSV file (default is comma).
        - na_values (list or str): Additional strings to recognize as NA/NaN (default is None).
        - dtype (dict): Data type for data or columns (default is None).

        Returns:
        - DataFrame: A pandas DataFrame containing the data from the CSV file.
        """
        return pd.read_csv(file_path, delimiter=delimiter, na_values=na_values, dtype=dtype)
