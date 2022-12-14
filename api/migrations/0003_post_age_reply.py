# Generated by Django 4.1.1 on 2022-09-20 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='age',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='api.comment')),
                ('reply_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_post', to='api.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
