# Generated by Django 3.0.6 on 2020-06-15 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200605_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='kvstore',
            name='kv_format',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='kvstore',
            name='kv_type',
            field=models.CharField(choices=[('text', 'Text'), ('money', 'Currency'), ('numeric', 'Numeric'), ('date', 'Date')], default='text', max_length=16),
        ),
        migrations.AlterField(
            model_name='page',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='core.Document'),
        ),
    ]
