from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from domain_app.models import User

class Command(BaseCommand):
    help = 'Grant specific permissions to a superuser'

    def handle(self, *args, **options):
        # Get the superuser
        superuser = User.objects.get(username='admin')

        # Grant specific permissions
        permission = Permission.objects.get(codename='desired_permission_codename')
        superuser.user_permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Permissions granted successfully'))
