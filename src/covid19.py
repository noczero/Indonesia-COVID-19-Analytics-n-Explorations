from .utils import preprocessing, load_data, save_plot, save_plot_all_province, save_plot_monthly, save_plot_weekday, \
    save_cases_to_csv, load_data_postprocessing
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

    def generate_plot(self):
        save_plot(self.clean_data)

    def generate_aggregation_plot(self):
        save_plot_all_province(self.clean_data)

    def generate_monthly_plot(self):
        save_plot_monthly(self.clean_data)

    def generate_weekday_plot(self):
        save_plot_weekday(self.clean_data)

    def generate_csv(self):
        save_cases_to_csv(self.clean_data)


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
    # indo_covid19.generate_plot()
    indo_covid19.generate_aggregation_plot()
