# Generated by Django 5.1.6 on 2025-02-19 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='icons/phrasebook/')),
            ],
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phrasebook.category')),
            ],
        ),
        migrations.CreateModel(
            name='TranslatePhrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/dictionary/')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.language')),
                ('phrase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phrasebook.phrase')),
            ],
        ),
    ]
