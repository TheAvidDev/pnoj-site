# Generated by Django 3.0.1 on 2020-01-05 03:40

from django.conf import settings
from django.db import migrations, models
import judge.models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0008_auto_20200105_0220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='maintainers',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='owner',
        ),
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.ManyToManyField(related_name='problems_authored', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problem',
            name='is_partial',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_file',
            field=models.FileField(unique=True, upload_to=judge.models.problem_file_path),
        ),
    ]