# Generated by Django 3.0.1 on 2020-01-05 19:29

from django.conf import settings
from django.db import migrations, models
import judge.models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0009_auto_20200105_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='problems_authored', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='problem',
            name='category',
            field=models.ManyToManyField(blank=True, to='judge.ProblemCategory'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_type',
            field=models.ManyToManyField(blank=True, to='judge.ProblemType'),
        ),
        migrations.AlterField(
            model_name='problemcategory',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='problemtype',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='submission',
            name='memory',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='points',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='scoreable',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='scored',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='source',
            field=models.FileField(upload_to=judge.models.submission_file_path),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(blank=True, choices=[('AC', 'Accepted'), ('WA', 'Wrong Answer'), ('TLE', 'Time Limit Exceeded'), ('MLE', 'Memory Limit Exceeded'), ('OLE', 'Output Limit Exceeded'), ('IR', 'Invalid Return'), ('IE', 'Internal Error'), ('AB', 'Aborted'), ('G', 'Grading')], max_length=4),
        ),
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='submissionbatchresult',
            name='status',
            field=models.CharField(choices=[('AC', 'Accepted'), ('WA', 'Wrong Answer'), ('TLE', 'Time Limit Exceeded'), ('MLE', 'Memory Limit Exceeded'), ('OLE', 'Output Limit Exceeded'), ('IR', 'Invalid Return'), ('IE', 'Internal Error'), ('AB', 'Aborted'), ('G', 'Grading')], max_length=4),
        ),
        migrations.AlterField(
            model_name='submissiontestcaseresult',
            name='status',
            field=models.CharField(choices=[('AC', 'Accepted'), ('WA', 'Wrong Answer'), ('TLE', 'Time Limit Exceeded'), ('MLE', 'Memory Limit Exceeded'), ('OLE', 'Output Limit Exceeded'), ('IR', 'Invalid Return'), ('IE', 'Internal Error'), ('AB', 'Aborted'), ('G', 'Grading')], max_length=4),
        ),
    ]
