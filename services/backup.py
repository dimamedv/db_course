import os
import subprocess
from datetime import datetime

import yadisk
from django_cron import Schedule, CronJobBase

from bd_course.settings import DATABASES, BACKUP_DIR, env

y = yadisk.YaDisk(
    id=env("YADISK_ID"),
    secret=env("YADISK_SECRET"),
    token=env("YADISK_TOKEN")
)

if y.check_token():
    print("Disk token is valid")
else:
    print("Disk token is invalid")


def create_backup(db_name, db_user, backup_dir):
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"db_backup_{date_str}.sql")

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Команда для создания бэкапа PostgreSQL
    command = f"pg_dump -U {db_user} {db_name} -f {backup_file}"

    # Выполнение команды и логирование ошибок
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Ошибка при создании бэкапа: {stderr.decode()}")
    else:
        print(f"Бэкап успешно создан: {backup_file}")
        if not y.exists("course_backups"):
            y.mkdir("/course_backups")
        y.upload(f"{backup_file}", f"/course_backups/{os.path.basename(backup_file)}")


class DatabaseBackupCronJob(CronJobBase):
    RUN_EVERY_MINS = 60 * 24  # запуск каждые 24 часа
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'database_backup_cron_job'

    def do(self):
        create_backup(
            DATABASES['default']['NAME'],
            DATABASES['default']['USER'],
            BACKUP_DIR,
        )
