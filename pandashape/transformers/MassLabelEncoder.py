from pandas import DataFrame, Series
import pandas as pd
from pandashape.transformers.GenericTransformer import GenericTransformer


class MassLabelEncoder(GenericTransformer):
    def __init__(self, label_encoding_breakpoint=0):
        self.label_encoding_breakpoint = label_encoding_breakpoint

    def transform(self, df):
        assert(isinstance(df, pd.DataFrame))

        newSeries = []
        for column in df.columns:
            series = df[column]
            unique_value_count = len(series.astype('category').cat.codes)

            if unique_value_count >= self.label_encoding_breakpoint:
                newSeries.append(self.__labelEncode(series))
            else:
                newSeries.append(self.__oneHotEncode(series))

        return newSeries

    def __labelEncode(self, series):
        return pd.Series(name=series.name, data=series.astype('category').cat.codes)

    def __oneHotEncode(self, series):
        return pd.get_dummies(series)
