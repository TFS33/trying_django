# Generated by Django 5.0.6 on 2024-06-18 09:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('difficulty', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.questions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.person')),
                ('id_person_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.answers')),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.questions')),
                ('id_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.test')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('id_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.test')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]