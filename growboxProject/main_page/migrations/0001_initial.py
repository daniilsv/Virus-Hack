# Generated by Django 2.2 on 2020-05-02 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrowBox',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ident', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WaterShare',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ident', models.IntegerField(default=0)),
                ('plan', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=3)),
                ('grow_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.GrowBox')),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ident', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=3)),
                ('plan', models.DateTimeField(auto_now=True)),
                ('grow_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.GrowBox')),
            ],
        ),
        migrations.CreateModel(
            name='DHT22',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ident', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(blank=True, null=None)),
                ('grow_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.GrowBox')),
            ],
        ),
    ]
