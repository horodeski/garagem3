# Generated by Django 4.2.4 on 2023-08-12 19:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="cpf",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="data_nascimento",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="telefone",
        ),
    ]