
from django.db import models

class Type_client(models.Model):
    Type_client = models.CharField(max_length=20)
    def __str__(self): return self.Type_client

class Svobodni_nomera(models.Model):
    nomer_clienta = models.CharField(max_length=18)
    def __str__(self): return self.nomer_clienta

class Tarifini_plan(models.Model):
    Naimenovanie_plana = models.CharField(max_length=25)
    MR_Vhodachi = models.IntegerField()
    MR_Ishodachi = models.IntegerField()
    S_Vhodachi = models.IntegerField()
    S_Ishodachi = models.IntegerField()
    def __str__(self): return self.Naimenovanie_plana

class Clienti(models.Model):
    ID_Type_Client = models.ForeignKey(Type_client, on_delete=models.CASCADE)
    Familia = models.CharField(max_length=25)
    Imya = models.CharField(max_length=25)
    Otchestvo = models.CharField(max_length=25)
    Vozrast_Let = models.IntegerField()
    Gorod_Projuvania = models.CharField(max_length=55)
    Date_zackluchenia = models.DateTimeField()
    Nomer_scheta = models.IntegerField()
    Opisanie = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='clients_photos/', null=True, blank=True, verbose_name="Фото клиента")
    def __str__(self): return f"{self.Familia} {self.Imya}"

class Mendgeri(models.Model):
    Familya = models.CharField(max_length=25)
    Imya = models.CharField(max_length=25)
    Otchestvo = models.CharField(max_length=25)
    Stoimost_v_mesaz = models.IntegerField()
    photo = models.ImageField(upload_to='managers_photos/', null=True, blank=True, verbose_name="Фото менеджера")
    def __str__(self): return f"{self.Familya} {self.Imya}"

class Podchenie_nomera(models.Model):
    ID_Clienti = models.ForeignKey(Clienti, on_delete=models.CASCADE)
    ID_Svobodni_nomera = models.ForeignKey(Svobodni_nomera, on_delete=models.CASCADE)
    ID_Tarifini_plan = models.ForeignKey(Tarifini_plan, on_delete=models.CASCADE)
    Date_Podchenia = models.DateTimeField()
    def __str__(self): return f"Подписка {self.ID_Clienti}"

class JurnalSoversheniZvonkov(models.Model):
    ID_Podchenie_nomera = models.ForeignKey(Podchenie_nomera, on_delete=models.CASCADE)
    Nomer_s_kem_soedinenia = models.CharField(max_length=18)
    Date_zvonka = models.DateTimeField()
    Stoimost_zvonka = models.IntegerField()
    def __str__ (self): return f"Звонок {self.Nomer_s_kem_soedinenia}"

class Abonentska_plata(models.Model):
    ID_Podchenie_nomera = models.ForeignKey(Podchenie_nomera, on_delete=models.CASCADE)
    Date_oplati = models.DateTimeField()
    Obshai_stoimost = models.IntegerField()
    def __str__ (self): return f"Плата {self.ID_Podchenie_nomera}"