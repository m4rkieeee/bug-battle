# Generated by Django 5.2.1 on 2025-05-23 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationStudentAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge_4.evaluationquestion')),
            ],
        ),
    ]
