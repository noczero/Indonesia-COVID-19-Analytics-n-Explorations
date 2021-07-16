import subprocess as cmd
from src.covid19 import Covid19
from src.kmeans_model import KMEANS_Covid
import schedule
import time
from datetime import datetime

FILE_EXTENSION = 'csv'  # export format
SHEET_GID = '2052139453'  # get from browser url when sheet clicked
DATA_URL = 'https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/export?format={}&gid={}'.format(
    FILE_EXTENSION, SHEET_GID)
UPDATE_TIME = '20:30'


def run_automation():
    # invoke pull for recent files on master
    do_git_pull_cmd()

    # generate plot
    indo_covid19 = Covid19(DATA_URL)
    indo_covid19.generate_plot()
    indo_covid19.generate_aggregation_plot()
    indo_covid19.generate_monthly_plot()
    indo_covid19.generate_weekday_plot()

    # generate csv
    indo_covid19.generate_csv()

    # k-Means
    kmeans_covid = KMEANS_Covid()
    print("Daily Clustering")
    kmeans_covid.model_daily_cured_death_rate(n_clusters=5)
    print("Weekly Clustering")
    kmeans_covid.model_weekly_active_newactivecapita_average(n_clusters=3)
    print("Weekly Clustering No-Norm")
    kmeans_covid.model_weekly_active_newactive_average_no_norm(n_clusters=2)

    # push new files
    do_git_push_cmd()


def do_git_pull_cmd():
    print("Get newest repository...")
    cmd.run("git pull origin master", check=True, shell=True)


def do_git_push_cmd():
    try:
        print("Add generated files to staging area.")
        cmd.run("git add images", check=True, shell=True)
        cmd.run("git add data", check=True, shell=True)

        print("Commit...")
        dt_now = datetime.now()
        msg = "Update-on-{}/{}/{}".format(dt_now.day, dt_now.month, dt_now.year)
        cmd.run("git commit -m {}".format(msg), check=True, shell=True)

        cmd.run("git push origin master", check=True, shell=True)
        print("Push successfully... ")
    except:
        cmd.run("git push origin master", check=True, shell=True)
        print("Something wrong...")


def main():
    print("Start Scheduling...")

    schedule.every().day.at(UPDATE_TIME).do(run_automation)

    run_automation()

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
