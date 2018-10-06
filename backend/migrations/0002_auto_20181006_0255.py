# Generated by Django 2.1.2 on 2018-10-06 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='high_priority',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='actions',
            name='encouraged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='activity_warnings',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Actions'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='diet_change',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Diet'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='environment_warnings',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Environment'),
        ),
        migrations.AlterField(
            model_name='diet',
            name='encouraged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='environment',
            name='encouraged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='primary_doctor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Doctor'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='activity_warnings',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Actions'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='diet_change',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Diet'),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='dosage',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='environment_warnings',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Environment'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='treatment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Treatment'),
        ),
    ]
