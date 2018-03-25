# Generated by Django 2.0.3 on 2018-03-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('url', models.URLField(blank=True)),
                ('content', models.TextField()),
                ('Created_time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=False, to='myblog.Article')),
            ],
        ),
    ]