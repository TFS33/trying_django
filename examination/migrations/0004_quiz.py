# Generated by Django 5.0.6 on 2024-06-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0003_rename_answers_answer_rename_questions_question_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
