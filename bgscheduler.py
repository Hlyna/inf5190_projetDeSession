import atexit
import manage
from apscheduler.schedulers.background import BackgroundScheduler

def update():
    sched = BackgroundScheduler(deamon=True)
    sched.add_job(manage.import_files(),'cron',hour =12)
    sched.start()

    atexit.register(lambda: sched.shutdown())