# Generated by Django 3.2.4 on 2021-12-01 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_category_node_subcategory_subsubcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSCategory',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Sub S Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('base.node',),
        ),
    ]