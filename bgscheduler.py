import atexit
import manage
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(deamon=True)
sched.add_job(manage.import_data(),'cron',hour =0)
sched.start()

atexit.register(lambda: sched.shutdown())