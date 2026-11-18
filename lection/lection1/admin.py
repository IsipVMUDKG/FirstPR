from django.contrib import admin
from .models import (
    Type_client, Svobodni_nomera, Tarifini_plan, Clienti, 
    Mendgeri, Podchenie_nomera, JurnalSoversheniZvonkov, Abonentska_plata
)

@admin.register(Type_client)
class TypeClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'Type_client')

@admin.register(Svobodni_nomera)
class SvobodniNomeraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomer_clienta')

@admin.register(Tarifini_plan)
class TarifiniPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'Naimenovanie_plana', 'S_Vhodachi', 'S_Ishodachi')

@admin.register(Clienti)
class ClientiAdmin(admin.ModelAdmin):
    list_display = ('id', 'Familia', 'Imya', 'Gorod_Projuvania', 'photo')

@admin.register(Mendgeri)
class MendgeriAdmin(admin.ModelAdmin):
    list_display = ('id', 'Familya', 'Imya', 'Stoimost_v_mesaz', 'photo')

@admin.register(Podchenie_nomera)
class PodchenieNomeraAdmin(admin.ModelAdmin):
    list_display = ('id', 'ID_Clienti', 'ID_Tarifini_plan', 'Date_Podchenia')

@admin.register(JurnalSoversheniZvonkov)
class JurnalZvonkovAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nomer_s_kem_soedinenia', 'Date_zvonka', 'Stoimost_zvonka')

@admin.register(Abonentska_plata)
class AbonentskaPlataAdmin(admin.ModelAdmin):
    list_display = ('id', 'ID_Podchenie_nomera', 'Date_oplati', 'Obshai_stoimost')