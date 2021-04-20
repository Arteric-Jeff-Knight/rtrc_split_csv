import io
from typing import Callable
import pandas as pd


class RtrcSplitCsv:
    """A helper to split an incoming csv file into a DataFrame with data and configs in a dict.

    """

    defaults = {}

    data = None

    def __init(self, the_csv=None, defaults=None, config_name: str = 'config'):

        if the_csv is not None:
            self.data, self.defaults = self.split_data_and_configs(the_csv, defaults, config_name)

    @staticmethod
    def split_data_and_configs(df, defaults=None, config_name: str = 'config', validator: Callable = None):

        if defaults is None or type(defaults) == dict:
            defaults = {}

        # Get everything with 'config' (or custom config_name) in first column
        configs = df[df[0] == config_name]
        # Build a dictionary from the key in the second column with values from the third
        defaults.update(dict(zip(configs[1], configs[2])))

        if validator is not None:
            defaults = validator(defaults)

        # Everything else that isn't a config, is data
        data = df[df[0] != config_name].reset_index(drop=True)
        # Assume that the first row is the column names now that configs are gone
        data.columns = data.iloc[0]
        # Drop the row with the column names
        data.drop(df.index[0], inplace=True)
        # Reset the index, so zero works below
        data = data.reset_index(drop=True)

        return data, defaults

    @staticmethod
    def split_from_csv(the_csv, defaults=None, config_name: str = 'config', validator: Callable = None):
        df = pd.read_csv(the_csv, header=None)

        return RtrcSplitCsv.split_data_and_configs(df, defaults, config_name, validator)

    @staticmethod
    def split_from_colab_upload(uploaded, defaults=None, config_name: str = 'config', validator: Callable = None):
        filename = list(uploaded.keys())[0]
        df = pd.read_csv(io.BytesIO(uploaded[filename]), header=None)

        return RtrcSplitCsv.split_data_and_configs(df, defaults, config_name, validator)
