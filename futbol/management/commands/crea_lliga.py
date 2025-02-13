from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from random import randint
 
from futbol.models import *
 
faker = Faker(["es_CA","es_ES"])
 
class Command(BaseCommand):
    help = 'Crea una lliga amb equips i jugadors'
 
    def add_arguments(self, parser):
        parser.add_argument('titol_lliga', nargs=1, type=str)
 
    def handle(self, *args, **options):
        titol_lliga = options['titol_lliga'][0]
        lliga = Lliga.objects.filter(nom=titol_lliga)
        if lliga.count()>0:
            print("Aquesta lliga ja està creada. Posa un altre nom.")
            return
 
        print("Creem la nova lliga: {}".format(titol_lliga))
        lliga = Lliga( nom=titol_lliga )
        lliga.save()
 
        print("Creem equips")
        prefixos = ["RCD", "Athletic", "", "Deportivo", "Unión Deportiva"]
        for i in range(20):
            ciutat = faker.city()
            prefix = prefixos[randint(0,len(prefixos)-1)]
            if prefix:
                prefix += " "
            nom =  prefix + ciutat
            any_fundacio = randint(1850,2010)
            equip = Equip(ciutat=ciutat,nom=nom,lliga=lliga, any_fundacio=any_fundacio)
            #print(equip)
            equip.save()
            lliga.equips.add(equip)
 
            print("Creem jugadors de l'equip "+nom)
            for j in range(25):
                nom = faker.name()
                posicio = "jugador"
                dorsal = randint(1,99)
                edat = 25
                jugador = Jugador(nom=nom,posicio=posicio,equip=equip,dorsal=dorsal)
                #print(jugador)
                jugador.save()
 
        print("Creem partits de la lliga")
        for local in lliga.equips.all():
            for visitant in lliga.equips.all():
                if local!=visitant:
                    partit = Partit(equip_local=local,
                                    equip_visitant=visitant,
                                    lliga=lliga)
                    partit.lliga = lliga
                    partit.save()
                    # crear Event tipus gol + temps
                    totalGols = randint(0,10)

                    for i in range (totalGols):
                        equip = local
                        choice = randint(0,1)

                        if choice == 0:
                            equip = visitant

                        jugadors_golejadors = Jugador.objects.filter(equip = equip)

                        jugador = jugadors_golejadors[randint(0,len(jugadors_golejadors))]
                        minut = randint(0,90)
                        gol = Event(partit=partit, jugador=jugador, tipus="gol", minut=minut)
                        gol.save()
                        print(f"{i} - Gol de {jugador.nom} per {equip.nom} al minut {minut}")
                            


                    # seleccionar jugador aleatorio entre els dos equips
                    # guardar gol