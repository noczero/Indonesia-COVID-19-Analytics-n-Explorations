import subprocess as cmd
from covid19 import Covid19
import schedule
import time
from datetime import datetime


def run_automation():
    # invoke pull for recent files on master
    do_git_pull_cmd()

    # process plot
    indo_covid19 = Covid19(data_url)
    indo_covid19.generate_plot()

    # push new files
    do_git_push_cmd()


def do_git_pull_cmd():
    print("Get newest repository...")
    cmd.run("git pull origin master", check=True, shell=True)


def do_git_push_cmd():
    try:
        print("Add images")
        cmd.run("git add ../notebooks/images", check=True, shell=True)
        dt_now = datetime.now()
        msg = "Update-on-{}/{}/{}".format(dt_now.day, dt_now.month, dt_now.year)
        cmd.run("git commit -m {}".format(msg), check=True, shell=True)
        cmd.run("git push origin master", check=True, shell=True)
        print("Push successfully... ")
    except:
        print("Something wrong...")


if __name__ == '__main__':
    print("Start Schedule")
    format = 'csv'  # export format
    sheet_gid = '2052139453'  # get from browser url when sheet clicked
    data_url = 'https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/export?format={}&gid={}'.format(
        format, sheet_gid)
    update_time = "19:30"
    schedule.every().day.at(update_time).do(run_automation)

    #run_automation()

    while True:
        schedule.run_pending()
        time.sleep(1)
