# Generated by Django 5.0.6 on 2024-06-18 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_questions_test_alter_person_birth_date_answers_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Results',
            new_name='Result',
        ),
        migrations.RenameModel(
            old_name='TestQuestions',
            new_name='TestQuestion',
        ),
    ]
