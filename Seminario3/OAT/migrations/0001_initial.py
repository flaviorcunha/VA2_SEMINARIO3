# Generated by Django 4.1.3 on 2022-12-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_professor', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('CPF', models.CharField(max_length=11)),
            ],
        ),
    ]