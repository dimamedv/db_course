from django.apps import AppConfig

from bd_course import settings
from services.backup import create_backup


class ClubMembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'club_members'

    def ready(self):
        create_backup(
            settings.DATABASES['default']['NAME'],
            settings.DATABASES['default']['USER'],
            settings.BACKUP_DIR,
        )
