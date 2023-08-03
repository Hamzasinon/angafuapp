# Generated by Django 4.2.3 on 2023-08-02 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('angaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservations',
            options={},
        ),
        migrations.AddField(
            model_name='reservations',
            name='code_reservation',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Valide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_trans', models.CharField(max_length=80)),
                ('trans_id', models.CharField(max_length=150)),
                ('montant_paye', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angaapp.reservations')),
            ],
        ),
    ]