# Generated by Django 4.2.4 on 2023-08-22 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_remove_response_business_name_remove_response_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('business_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='survey',
            name='business_name',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='email',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='name',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='response',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.personinfo'),
            preserve_default=False,
        ),
    ]
