# Generated by Django 4.2 on 2025-02-07 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('any_fundacio', models.IntegerField()),
                ('estadi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lliga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Partit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('equip_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits_locals', to='futbol.equip')),
                ('equip_visitant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits_visitants', to='futbol.equip')),
                ('lliga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits', to='futbol.lliga')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('posicio', models.CharField(choices=[('PT', 'Porter'), ('DF', 'Defensa'), ('MC', 'Migcampista'), ('DL', 'Davanter')], max_length=50)),
                ('dorsal', models.IntegerField()),
                ('nacionalitat', models.CharField(max_length=50)),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadors', to='futbol.equip')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipus_esdeveniment', models.CharField(choices=[('gol', 'Gol'), ('targeta_groga', 'Targeta Groga'), ('targeta_vermella', 'Targeta Vermella'), ('substitucio', 'Substitució')], max_length=50)),
                ('minut', models.IntegerField()),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='esdeveniments', to='futbol.jugador')),
                ('partit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='esdeveniments', to='futbol.partit')),
            ],
        ),
        migrations.AddField(
            model_name='equip',
            name='lliga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equips', to='futbol.lliga'),
        ),
    ]
