from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from service.Announcer import MessageAnnouncer

db = SQLAlchemy()
sched = BackgroundScheduler()
announcer = MessageAnnouncer()