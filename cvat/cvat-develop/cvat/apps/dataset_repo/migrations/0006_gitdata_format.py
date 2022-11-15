# Generated by Django 3.1.13 on 2021-10-26 10:10

from django.db import migrations, models


def update_default_format_field(apps, schema_editor):
    GitData = apps.get_model('dataset_repo', 'GitData')
    for git_data in GitData.objects.all():
        if not git_data.format:
            git_data.format = 'CVAT for images 1.1' if git_data.task.mode == 'annotation' else 'CVAT for video 1.1'
            git_data.save()
class Migration(migrations.Migration):

    dependencies = [
        ('dataset_repo', '0005_auto_20201019_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitdata',
            name='format',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.RunPython(update_default_format_field),
    ]
