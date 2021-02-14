import pandas as pd
from datetime import datetime


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
