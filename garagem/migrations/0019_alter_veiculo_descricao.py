# Generated by Django 4.2.4 on 2023-08-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0018_remove_veiculo_categoria_remove_veiculo_marca_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veiculo",
            name="descricao",
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]