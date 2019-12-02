# Generated by Django 2.1.5 on 2019-04-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_admin_event_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusOnChannel',
            fields=[
                ('table_id', models.IntegerField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=30)),
                ('site_url', models.CharField(max_length=350)),
                ('country', models.CharField(max_length=30)),
                ('site_id', models.IntegerField()),
                ('website', models.IntegerField()),
                ('app', models.CharField(max_length=30)),
                ('coverage', models.CharField(max_length=30)),
                ('method', models.CharField(max_length=30)),
                ('doc_name', models.CharField(max_length=30)),
                ('email1', models.CharField(max_length=30)),
                ('email2', models.CharField(max_length=30)),
                ('cc', models.CharField(max_length=30)),
                ('restriction', models.CharField(max_length=100)),
                ('support_name', models.CharField(max_length=30)),
                ('support_email', models.CharField(max_length=30)),
                ('support_mobile', models.CharField(max_length=15)),
                ('payment_policy', models.CharField(max_length=200)),
                ('payment_within_days', models.IntegerField()),
                ('merchant_name', models.CharField(max_length=30)),
                ('official_convenience_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('official_transaction_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('official_flat_charges', models.DecimalField(decimal_places=2, max_digits=6)),
                ('official_tax_charges', models.DecimalField(decimal_places=2, max_digits=6)),
                ('negotiated_convenience_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('negotiated_transaction_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('negotiated_flat_charges', models.DecimalField(decimal_places=2, max_digits=6)),
                ('negotiated_tax_charges', models.DecimalField(decimal_places=2, max_digits=6)),
                ('convenience_fee_organizer', models.DecimalField(decimal_places=2, max_digits=6)),
                ('transaction_fee_organizer', models.DecimalField(decimal_places=2, max_digits=6)),
                ('flat_fee_organizer', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tax_fee_organizer', models.DecimalField(decimal_places=2, max_digits=6)),
                ('additional_msg', models.CharField(max_length=200)),
                ('active_state', models.IntegerField()),
            ],
            options={
                'db_table': 'partner_sites',
                'managed': False,
            },
        ),
    ]