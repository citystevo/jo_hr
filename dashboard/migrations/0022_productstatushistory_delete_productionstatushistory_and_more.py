# Generated by Django 4.2 on 2024-10-29 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0021_productionstatushistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_history', to='dashboard.product')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Production Status History',
                'verbose_name_plural': 'Production Status Histories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='ProductionStatusHistory',
        ),
        migrations.AddIndex(
            model_name='productstatushistory',
            index=models.Index(fields=['created_at', 'is_active'], name='dashboard_p_created_4341bc_idx'),
        ),
    ]
