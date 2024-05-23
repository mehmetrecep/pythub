# tests/test_data_frame_loader.py
import unittest
import pandas as pd
import data_frame_loader
import os

class TestDataFrameLoader(unittest.TestCase):
    def setUp(self):
        # Create a sample CSV file for testing
        self.sample_csv_path = 'sample.csv'
        data = {
            'A': [1, 2, 3, 4],
            'B': [5, 6, 7, 8],
            'C': ['a', 'b', 'c', 'd']
        }
        df = pd.DataFrame(data)
        df.to_csv(self.sample_csv_path, index=False)

    def tearDown(self):
        # Remove the sample CSV file after tests
        if os.path.exists(self.sample_csv_path):
            os.remove(self.sample_csv_path)

    def test_read_csv(self):
        df = data_frame_loader.DataFrameLoader.read_csv(self.sample_csv_path)
        self.assertEqual(df.shape, (4, 3))
        self.assertListEqual(df.columns.tolist(), ['A', 'B', 'C'])
        self.assertListEqual(df['A'].tolist(), [1, 2, 3, 4])
