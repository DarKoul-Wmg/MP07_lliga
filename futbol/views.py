from django.shortcuts import render

from futbol.models import *

def classificacio(request):
    lliga = Lliga.objects.all()[1]
    equips = lliga.equips.all()
    classi = []
    # calculem punts en llista de tuples (equip,punts)
    for equip in equips:
        punts = 0
        victories = 0
        derrotes = 0
        empats = 0
        gols_favor = 0
        gols_contra = 0

        for partit in lliga.partits.filter(equip_local=equip):
            gols_favor=partit.gols_local()
            gols_contra=partit.gols_visitant()

            if partit.gols_local() > partit.gols_visitant():
                punts += 3
                victories += 1

            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
                empats += 1

            else:
                derrotes += 1

        for partit in lliga.partits.filter(equip_visitant=equip):
            gols_contra=partit.gols_local()
            gols_favor=partit.gols_visitant()
            
            if partit.gols_local() < partit.gols_visitant():
                punts += 3
                victories += 1

            elif partit.gols_local() == partit.gols_visitant():
                punts += 1
                empats += 1
            
            else:
                derrotes += 1

        classi.append( {"punts":punts,"equip":equip.nom, "victories":victories,"derrotes":derrotes,"empats":empats,"gols_favor":gols_favor,"gols_contra":gols_contra} )
    # ordenem llista
    classi.sort(reverse=True, key=lambda x:x["punts"])
    return render(request,"classificacio.html",
                {
                    "classificacio":classi,
                    "lliga":lliga
                })