# Generated by Django 2.2.16 on 2022-11-18 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название группы.', max_length=200, verbose_name='Заголовок группы:')),
                ('slug', models.CharField(help_text='Введите уникальный индентификатор.', max_length=50, unique=True, verbose_name='Имя в адресной строке:')),
                ('description', models.TextField(blank=True, help_text='Добавьте описание группы.', verbose_name='Описание:')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Выберите группу для публикации.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.Group', verbose_name='Группа:'),
        ),
    ]
