import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.style as style
import seaborn as sns

from matplotlib.dates import DateFormatter
# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
from typing import Tuple, Dict

register_matplotlib_converters()

date_form = DateFormatter("%d-%b-%y")

style.use('seaborn-poster')  # sets the size of the charts
style.use('seaborn-whitegrid')
sns.set_context('poster')


def load_data(url: str) -> pd.DataFrame:
    return pd.read_csv(url)


def preprocessing(df_raw: pd.DataFrame) -> dict:
    categories = ['Kasus Harian', 'Kasus Aktif', 'Sembuh', 'Sembuh Harian', 'Meninggal Dunia',
                  'Meninggal Dunia Harian']
    df_clean = df_raw.iloc[:, :-2]  # remove 2 last columns

    # We dont care about meninggal Luar Jakarta categories and others remaining, so we find its index
    index_no_need = df_clean[df_clean['Bali'].str.match('Luar Jakarta', na=False)].index.values[0]
    df_clean = df_clean.iloc[:index_no_need, :]

    # take rows that total kasus is not NaN
    df_clean = df_clean[df_clean['Total Kasus'].notna()]

    # reset index after filter some rows
    df_clean.reset_index(drop=True, inplace=True)

    # find indexes of categories key
    index_categories = {}
    for category in categories:
        # find index of each category on 'Total Kasus' column, na = False (not remove NA values).
        index_categories[category] = df_clean[df_clean['Total Kasus'].str.match(category, na=False)].index.values[0]

    # get total kasus from 0 to kasus harian, and remove rows that has all values as NaN.
    df_total_cases = df_clean.iloc[:index_categories['Kasus Harian'], :]

    # as categories is in the list, better use loop
    df_categories = {}
    idx_categories_list = list(index_categories.values())  # convert values to list
    for i in range(len(idx_categories_list)):
        if i < len(idx_categories_list) - 1:
            # filter rows based on range
            df_categories[categories[i]] = df_clean.iloc[idx_categories_list[i] + 1:idx_categories_list[i + 1], :]
        else:
            # as it last, last rows is index_no_need
            df_categories[categories[i]] = df_clean.iloc[idx_categories_list[i] + 1:index_no_need, :]

    # added df_total_kasus to df_categories
    df_categories['Total Case'] = df_total_cases

    # process next preprocessing for each category
    for category, df_category in df_categories.items():
        print("Preprocessing")
        print("Category : {}".format(category))
        # fill NaN to zero string
        df_category = df_category.fillna('0')

        # rename Total Kasus to time
        df_category = df_category.rename(columns={"Total Kasus": "Time"})

        # parse time from string to datetime format pandas with year
        parse_time_list = parse_time(df_category)
        df_category.loc[:, 'Time'] = parse_time_list

        # set time as index
        df_category = df_category.set_index('Time')

        # remove comma
        df_category = df_category.apply(lambda x: x.str.replace(',', ''))

        # convert columns to numeric
        df_category = df_category.apply(pd.to_numeric)

        # set ddf_category
        df_categories[category] = df_category

        # print(df_categories[category].info())

    return df_categories


# function for parsing time
def parse_time(df_category: pd.DataFrame) -> list:
    time_list = []
    start_year = 2020
    for index, row in df_category.iterrows():
        # print(row['Time'])
        time_str = row['Time']

        # check new year, if 31-Dec than add year
        if '1 Jan' == time_str or '1-Jan' == time_str:
            start_year += 1

        # concat
        time_str = time_str + ' ' + str(start_year)

        # check format

        if '-' in time_str:
            time_dt = datetime.strptime(time_str, '%d-%b %Y')
            time_list.append(time_dt)
        else:
            time_dt = datetime.strptime(time_str, '%d %b %Y')
            time_list.append(time_dt)

        # print(time_dt)
    return time_list


# plot
def save_plot(df_categories: dict):
    for category, df_category in df_categories.items():
        print("Generating {} plot...".format(category))
        for province in df_category.columns:
            fig, ax = plt.subplots()

            if 'Harian' in category:
                # ax.bar(df_category.index,df_category[province], label=category)
                # sns.barplot( x = df_category.index, y= province, data = df_category)
                ax.bar(df_category.index, df_category[province], color='tab:red', label=category)

            else:
                ax.plot(df_category.index, df_category[province], color='tab:red', label=category)

            skip = max(len(df_category.index) // 10, 1)  # 10 date tick marks
            plt.xticks(df_category.index[::skip])

            ax.set_title('Kasus Covid-19 di {}'.format(province))
            ax.set_xlabel('Waktu')
            ax.set_ylabel('Orang')
            ax.legend(loc='upper right')

            # change date fromat
            ax.xaxis.set_major_formatter(date_form)

            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('../images/{}_{}.png'.format(category, province), dpi=100)
            plt.close()

        print("Generating {} plot successfully.".format(category))


def save_plot_all_province(df_categories: dict):
    LINE_STYLES = ['solid', 'dashed', 'dashdot', 'dotted']
    NUM_STYLES = len(LINE_STYLES)
    NUM_COLORS = 34

    cm = plt.get_cmap('gist_rainbow')
    clrs = sns.color_palette('husl', n_colors=NUM_COLORS)  # a list of RGB tuples

    for category, df_category in df_categories.items():
        print("Generating join {} plot...".format(category))
        if 'Harian' not in category:
            fig = plt.figure(figsize=(12, 10))
            ax = plt.subplot(111)
            i = 0
            for province in df_category.columns:
                lines = ax.plot(df_category.index, df_category[province], label=province)
                lines[0].set_color(clrs[i])
                lines[0].set_linestyle(LINE_STYLES[i % NUM_STYLES])
                i += 1

            plt.title('{} di Semua Provinsi'.format(category))
            skip = max(len(df_category.index) // 10, 1)  # 10 date tick marks
            plt.xticks(df_category.index[::skip])
            plt.xlabel("Waktu")
            plt.ylabel("Orang")
            plt.xticks(rotation=45)

            # Shrink current axis's height by 10% on the bottom
            box = ax.get_position()
            ax.set_position([box.x0, box.y0 + box.height * 0.5,
                             box.width, box.height * 1])

            # Put a legend below current axis
            ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.35),
                      fancybox=True, shadow=True, ncol=5)

            # date formatter
            ax.xaxis.set_major_formatter(date_form)

            plt.subplots_adjust()
            plt.savefig('../images/{}_Semua_Provinsi.png'.format(category), dpi=100, bbox_inches='tight')
            plt.close()
        else:
            # bar
            fig = plt.figure(figsize=(12, 10))
            ax = plt.subplot(111)
            i = 0
            for province in df_category.columns:
                lines = ax.bar(df_category.index, df_category[province], label=province)
                lines[0].set_color(clrs[i])
                lines[0].set_linestyle(LINE_STYLES[i % NUM_STYLES])
                i += 1

            plt.title('{} di Semua Provinsi'.format(category))
            skip = max(len(df_category.index) // 10, 1)  # 10 date tick marks
            plt.xticks(df_category.index[::skip])
            plt.xlabel("Waktu")
            plt.ylabel("Orang")
            plt.xticks(rotation=45)

            # Shrink current axis's height by 10% on the bottom
            box = ax.get_position()
            ax.set_position([box.x0, box.y0 + box.height * 0.5,
                             box.width, box.height * 1])

            # Put a legend below current axis
            ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.35),
                      fancybox=True, shadow=True, ncol=5)

            # date formatter
            ax.xaxis.set_major_formatter(date_form)

            plt.subplots_adjust()
            plt.savefig('../images/{}_Semua_Provinsi.png'.format(category), dpi=100, bbox_inches='tight')
            plt.close()

        print("Generating join {} plot successfully.".format(category))


def save_plot_monthly(df_categories: dict):
    for category, df_category in df_categories.items():
        if 'Harian' in category:  # Filter just harian
            print("Generating {} plot in month...".format(category))
            df_monthly_avg = df_category.resample('M').mean()  # get average

            for province in df_category.columns:
                fig, ax = plt.subplots()
                df_monthly_avg[province].plot(kind='bar', title='Rata-Rata {} di {}'.format(category, province), ax=ax,
                                              color='tab:red').set(xlabel='Waktu', ylabel='Orang')
                ax.set_xticklabels(map(line_format, df_monthly_avg[province].index))
                plt.tight_layout()
                ax.figure.savefig('../images/{} Rata-Rata di {}'.format(category, province), dpi=100)
                plt.close()

            print("Generating {} plot in month successfully.".format(category))


def save_plot_weekday(df_categories: dict):
    days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    for category, df_category in df_categories.items():
        if 'Harian' in category:  # Filter just harian
            print("Generating {} plot in weekday...".format(category))
            df_weekly_avg = df_category.copy()
            df_weekly_avg['Day'] = df_category.index.weekday  # get weekday, 0 : monday, 1 : tuesday , .... , 6 : Sunday
            df_weekly_avg = df_weekly_avg.groupby('Day').mean()

            for province in df_category.columns:
                fig, ax = plt.subplots()
                df_weekly_avg[province].plot(kind='bar',
                                             title='Rata-Rata {} dalam Hari di {}'.format(category, province), ax=ax,
                                             color='tab:red').set(xlabel='Waktu', ylabel='Orang')
                ax.set_xticklabels(days)
                plt.tight_layout()
                ax.figure.savefig('../images/{} Rata-Rata dalam Hari di {}'.format(category, province), dpi=100)
                plt.close()

            print("Generating {} plot in weekday successfully.".format(category))


def save_cases_to_csv(df_categories: dict):
    for category, df_category in df_categories.items():
        filename = "../data/{}_post_processing.csv".format(category)
        df_category.to_csv(filename)
        print("Generating for {} CSV file successfully".format(category))


def line_format(label):
    """
    Convert time label to the format of pandas line plot
    """
    month = label.month_name()[:3]
    if month == 'Jan':
        month += f'\n{label.year}'
    return month


def load_data_population():
    # get population information
    df_populations = pd.read_excel('../data/Jumlah_Penduduk_Indonesia_2020.xlsx')
    #df_populations.info()

    df_populations['2020'] = df_populations['2020'] * 1000  # multiple to thousand

    # mapping
    df_populations['Provinsi'] = df_populations['Provinsi'].apply(lambda name: province_name_to_abr(name))

    # set index
    df_populations = df_populations.set_index('Provinsi')

    # rename column
    df_populations = df_populations.rename(columns={'2020': 'population'})

    return df_populations


def province_name_to_abr(province_name: str) -> str:
    # Bengkulu,DIY,Jakarta,Jambi,Jabar,Jateng,Jatim,Kalbar,Kaltim,Kalteng,Kalsel,Kaltara,Kep Riau,NTB,Sumsel,Sumbar,Sulut,Sumut,Sultra,Sulsel,Sulteng,Lampung,Riau,Malut,Maluku,Papbar,Papua,Sulbar,NTT,Gorontalo
    provinces_map = {
        'SUMATERA UTARA': 'Sumut',
        'KEP. BANGKA BELITUNG': 'Babel',
        'SUMATERA BARAT': 'Sumbar',
        'SUMATERA SELATAN': 'Sumsel',
        'KEP. BANGKA BELITUNG': 'Babel',
        'KEP. RIAU': 'Kep Riau',
        'DKI JAKARTA': 'Jakarta',
        'JAWA BARAT': 'Jabar',
        'JAWA TENGAH': 'Jateng',
        'DI YOGYAKARTA': 'DIY',
        'JAWA TIMUR': 'Jatim',
        'NUSA TENGGARA BARAT': 'NTB',
        'NUSA TENGGARA TIMUR': 'NTT',
        'KALIMANTAN BARAT': 'Kalbar',
        'KALIMANTAN TENGAH': 'Kalteng',
        'KALIMANTAN SELATAN': 'Kalsel',
        'KALIMANTAN TIMUR': 'Kaltim',
        'KALIMANTAN UTARA': 'Kaltara',
        'SULAWESI UTARA': 'Sulut',
        'SULAWESI TENGAH': 'Sulteng',
        'SULAWESI SELATAN': 'Sulsel',
        'SULAWESI TENGGARA': 'Sultra',
        'SULAWESI BARAT': 'Sulbar',
        'MALUKU UTARA': 'Malut',
        'PAPUA BARAT': 'Papbar'
    }

    try:
        return provinces_map[province_name]
    except:
        return province_name.capitalize()


# K-Means utils
def load_data_postprocessing() -> Tuple[Dict[str, pd.DataFrame], Dict[str, pd.DataFrame]]:
    files_categories = {
        'Kasus Harian': 'Kasus Harian_post_processing.csv',
        'Kasus Aktif': 'Kasus Aktif_post_processing.csv',
        'Sembuh Harian': 'Sembuh Harian_post_processing.csv',
        'Sembuh': 'Sembuh Harian_post_processing.csv',
        'Meninggal Dunia Harian': 'Meninggal Dunia Harian_post_processing.csv',
        'Meninggal Dunia': 'Meninggal Dunia_post_processing.csv',
        'Total Case': 'Total Case_post_processing.csv'
    }

    df_categories = {}
    df_date_time = {}
    for category in files_categories:
        # get the value
        csv_file_name = "../data/{}".format(files_categories[category])

        # load data
        df_categories[category] = pd.read_csv(csv_file_name)
        df_date_time[category] = df_categories[category].pop('Time')
        # df_categories[category].info()

    return df_categories, df_date_time


def process_daily_features(df_categories: [dict, pd.DataFrame]) -> pd.DataFrame:
    # df_features = pd.DataFrame()
    df_daily_cured_rate = df_categories['Sembuh Harian'].tail(1) / df_categories['Kasus Aktif'].tail(1)
    df_daily_death_rate = df_categories['Meninggal Dunia Harian'].tail(1) / df_categories['Kasus Aktif'].tail(
        1)

    # concat dataframe
    frames = [df_daily_cured_rate, df_daily_death_rate]
    df_features = pd.concat(frames)
    df_features = df_features.reset_index()
    del df_features['index']

    # rename columns for clearer dataframe
    df_features = df_features.rename(index={0: 'daily_cured_rate', 1: 'daily_death_rate'})

    # transpose df_features
    df_features = df_features.transpose()

    # normalization using min max scalar value-min/max-min
    df_features = (df_features - df_features.min()) / (df_features.max() - df_features.min())

    return df_features


def process_weekly_features(df_categories: [dict, pd.DataFrame], norm=True) -> pd.DataFrame:
    # merge join by index and rename
    df_weekly_features = pd.DataFrame()
    df_weekly_features['weekly_active_average'] = df_categories['Kasus Aktif'].tail(7).mean()
    df_weekly_features['weekly_confirmed_average'] = df_categories['Kasus Harian'].tail(7).mean()

    # merge
    df_populations = load_data_population()
    df_new_features = pd.merge(df_populations, df_weekly_features, how="inner", left_index=True, right_index=True)

    # add per capita columns
    df_new_features['weekly_active_capita'] = df_new_features['weekly_active_average'] / df_new_features[
        'population'] * 100
    df_new_features['weekly_confirmed_capita'] = df_new_features['weekly_confirmed_average'] / df_new_features[
        'population'] * 100
    # df_new_features.head()

    if norm:
        # df_features_norm = ( df_new_features[['weekly_active_average','weekly_confirmed_capita']] - df_new_features[['weekly_active_average','weekly_confirmed_capita']].min() ) / ( df_new_features[['weekly_active_average','weekly_confirmed_capita']].max() - df_new_features[['weekly_active_average','weekly_confirmed_capita']].min() )
        df_features_norm = (df_new_features - df_new_features.min()) / (df_new_features.max() - df_new_features.min())
        # df_features_norm
        return df_features_norm
    else:
        return df_new_features

def generate_clustering_plot(y_predicts: list, df_features_x: pd.DataFrame, df_features_y: pd.DataFrame,
                             df_features_size: pd.DataFrame, df_date_time: pd.DataFrame, plot_properties: dict):
    # set size for plot from mean of 2 columns
    size_points =  df_features_size / 10000

    # visualize
    fig = plt.figure(figsize=(14, 12))
    ax = plt.subplot(111)
    plt.scatter(df_features_x, df_features_y, c=y_predicts, s=size_points,
                alpha=0.7, cmap='plasma')
    ax.grid(True)

    # merge
    df_features = pd.merge(df_features_x, df_features_y, right_index=True, left_index=True)

    for index, rows in df_features.iterrows():
        plt.annotate(index, (rows[0], rows[1]))

    latest_dt = pd.to_datetime(df_date_time['Kasus Aktif'].tail(1))
    readable_datetime = latest_dt.dt.strftime('%A, %d-%B-%Y').values[0]
    plt.title("Zona Clustering di Indonesia\n {}".format(readable_datetime))
    plt.xlabel(plot_properties['x_label'])
    plt.ylabel(plot_properties['y_label'])
    plt.subplots_adjust()
    plt.savefig('../images/{}_Semua_Provinsi.png'.format(plot_properties['name']), dpi=100, bbox_inches='tight')
    plt.close()
