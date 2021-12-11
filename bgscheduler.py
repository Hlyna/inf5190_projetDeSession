import atexit
from manage import import_files
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(deamon=True)
sched.add_job(import_files,'cron', hour =12 ,minute='17', timezone='America/Newyork')
sched.start()

atexit.register(lambda: sched.shutdown())