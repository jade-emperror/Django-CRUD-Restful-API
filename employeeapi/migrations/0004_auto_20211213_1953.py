# Generated by Django 3.1.5 on 2021-12-13 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employeeapi', '0003_employee_uname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='uname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]