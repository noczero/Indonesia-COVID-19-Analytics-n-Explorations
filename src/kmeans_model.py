from sklearn.cluster import KMeans
import locale

#locale.setlocale(locale.LC_TIME, "id_ID")
from utils import load_data_postprocessing, process_weekly_features, process_daily_features, \
    generate_clustering_plot, load_data_population


class KMEANS_Covid:
    def __init__(self):
        self.df_categories, self.df_date_time = load_data_postprocessing()
        self.df_populations = load_data_population()

    def model_daily_cured_death_rate(self, n_clusters):
        # feature engineering
        features = process_daily_features(self.df_categories)

        # predicts class
        y_predicts = KMeans(n_clusters=n_clusters).fit_predict(features.astype('float16'))

        # generate plot
        plot_properties = {
            'name': 'K-Means-Daily',
            'x_label': 'Rate Sembuh Harian \n Normalisasi Min-Max(0-1)',
            'y_label': 'Rate Meninggal Harian \n Normalisasi Min-Max(0-1)'
        }

        generate_clustering_plot(y_predicts=y_predicts,
                                 df_features_x=features['daily_cured_rate'],
                                 df_features_y=features['daily_death_rate'],
                                 df_features_size=self.df_populations['population'],
                                 df_date_time=self.df_date_time['Total Case'],
                                 plot_properties=plot_properties)

    def model_weekly_active_newactivecapita_average(self, n_clusters):
        # feature engineering
        features = process_weekly_features(self.df_categories)

        # predicts class
        y_predicts = KMeans(n_clusters=n_clusters).fit_predict(
            features[['weekly_active_average', 'weekly_confirmed_capita']].astype('float16'))

        # generate plot
        plot_properties = {
            'name': 'K-Means_Weekly',
            'x_label': 'Rata-Rata Kasus Aktif Mingguan \n Normalisasi Min-Max(0-1)',
            'y_label': 'Rata-Rata Penambahan Kasus Per Kapita Mingguan \n Normalisasi Min-Max(0-1)'
        }

        generate_clustering_plot(y_predicts=y_predicts,
                                 df_features_x=features['weekly_active_average'],
                                 df_features_y=features['weekly_confirmed_capita'],
                                 df_features_size=features['population'],
                                 df_date_time=self.df_date_time['Total Case'],
                                 plot_properties=plot_properties)

    def model_weekly_active_newactive_average_no_norm(self, n_clusters):
        # feature engineering
        features = process_weekly_features(self.df_categories, norm=False)

        # predicts class
        y_predicts = KMeans(n_clusters=n_clusters).fit_predict(
            features[['weekly_active_average', 'weekly_confirmed_average']].astype('float16'))

        # generate plot
        plot_properties = {
            'name': 'K-Means_Weekly_no_norm',
            'x_label': 'Rata-Rata Kasus Aktif Mingguan',
            'y_label': 'Rata-Rata Penambahan Kasus Mingguan'
        }

        generate_clustering_plot(y_predicts=y_predicts,
                                 df_features_x=features['weekly_active_average'],
                                 df_features_y=features['weekly_confirmed_average'],
                                 df_features_size=features['population'],
                                 df_date_time=self.df_date_time['Total Case'],
                                 plot_properties=plot_properties)




if __name__ == '__main__':
    kmeans_covid = KMEANS_Covid()
    print("Daily Clustering")
    kmeans_covid.model_daily_cured_death_rate(n_clusters=5)
    print("Weekly Clustering")
    kmeans_covid.model_weekly_active_newactivecapita_average(n_clusters=3)
    print("Weekly Clustering No-Norm")
    kmeans_covid.model_weekly_active_newactive_average_no_norm(n_clusters=2)
    #print(kmeans_covid.df_categories)
