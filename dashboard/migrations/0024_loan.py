# Generated by Django 4.2 on 2024-11-01 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0023_alter_product_options_product_category_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(choices=[('Salary_Advance', 'Salary Advance'), ('Personal_Loan', 'Personal Loan'), ('Emergency_Loan', 'Emergency Loan'), ('Education_Loan', 'Education Loan'), ('Medical_Loan', 'Medical Loan'), ('Housing_Loan', 'Housing Loan'), ('Vehicle_Loan', 'Vehicle Loan'), ('Business_Loan', 'Business Loan'), ('Travel_Loan', 'Travel Loan'), ('Wedding_Loan', 'Wedding Loan'), ('Debt_Consolidation', 'Debt Consolidation Loan'), ('Home_Improvement', 'Home Improvement Loan'), ('Short_Term', 'Short Term Loan'), ('Long_Term', 'Long Term Loan'), ('Other', 'Other')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('response_date', models.DateTimeField(blank=True, null=True)),
                ('response_message', models.TextField(blank=True, null=True)),
                ('admin_response', models.TextField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_loans', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
