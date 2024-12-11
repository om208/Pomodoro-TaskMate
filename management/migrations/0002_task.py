# Generated by Django 5.1.4 on 2024-12-11 08:00

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('initial_deadline', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=6)),
                ('estimated_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('remainder_sound', models.CharField(default='/reminder-sound/Task/bell1', max_length=255)),
                ('status', models.CharField(choices=[('working', 'Working'), ('done', 'Done'), ('pending', 'Pending')], default='pending', max_length=8)),
                ('Reminder_duration', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(1)])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]