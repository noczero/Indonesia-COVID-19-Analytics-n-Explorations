from utils import preprocessing, load_data
import pandas as pd


class Covid19:
    def __init__(self, url):
        self.data_url = url

        # load data
        raw_data = load_data(self.data_url)

        # preprocessing data
        self.clean_data = preprocessing(raw_data)

    def get_new_active_case(self) -> pd.DataFrame:
        return self.clean_data['Kasus Harian']

    def get_still_active_case(self) -> pd.DataFrame:
        return self.clean_data['Kasus Aktif']

    def get_total_confirmed_case(self) -> pd.DataFrame:
        return self.clean_data['Total Case']

    def get_total_cured_case(self) -> pd.DataFrame:
        return self.clean_data['Sembuh']

    def get_new_cured_case(self) -> pd.DataFrame:
        return self.clean_data['Sembuh Harian']

    def get_total_dead_case(self) -> pd.DataFrame:
        return self.clean_data['Meninggal Dunia']

    def get_new_dead_case(self) -> pd.DataFrame:
        return self.clean_data['Meninggal Dunia Harian']


if __name__ == '__main__':
    # testing

    format = 'csv'  # export format
    sheet_gid = '2052139453'  # get from browser url when sheet clicked
    data_url = 'https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/export?format={}&gid={}'.format(
        format, sheet_gid)

    indo_covid19 = Covid19(data_url)
    list_cases = indo_covid19.clean_data

    print("\nStill Active")
    print(indo_covid19.get_still_active_case())
