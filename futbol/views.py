from django.shortcuts import render,redirect,get_object_or_404
from django import forms

from futbol.models import *

#menu desplegable
class MenuForm(forms.Form):
    lliga = forms.ModelChoiceField(queryset=Lliga.objects.all())

def menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            lliga = form.cleaned_data.get("lliga")
            # cridem a /classificacio/<lliga_id>
            return redirect('classificacio',lliga.id)
    return render(request, "menu.html",{
                    "form": form,
            })

#data para clasificacion
def classificacio(request, lliga_id):
    lliga = get_object_or_404(Lliga, pk=lliga_id)
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