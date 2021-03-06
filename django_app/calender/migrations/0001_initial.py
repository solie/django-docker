# Generated by Django 3.0.8 on 2020-07-16 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('display_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=32)),
                ('zoom_meeting_id', models.CharField(blank=True, max_length=64, null=True)),
                ('chat_room_url', models.URLField(blank=True, null=True)),
                ('chat_room_line_id', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='doctor')),
                ('verified', models.BooleanField(blank=True, default=False, null=True)),
                ('timezone', models.CharField(default='zh-tw', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('recurring', models.CharField(blank=True, max_length=255, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calender.Doctor')),
            ],
        ),
    ]
