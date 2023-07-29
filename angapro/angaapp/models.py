from django.db import models

class Societe(models.Model):
    nom=models.CharField(max_length=80, blank=True)
    img=models.ImageField()
    create_date=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural=('Societe')
    
    def __str__(self):
        return self.nom

class Heure_d(models.Model):
    time=models.DateTimeField()
    
    def __str__(self):
        return self.time
    
class Reservations(models.Model):
    societe=models.ManyToManyField(Societe,)
    nom=models.CharField(max_length=80, blank=True)
    prenom=models.CharField(max_length=80, blank=True)
    tel=models.CharField(max_length=80, blank=True)
    num_trans=models.CharField(max_length=80, blank=True)
    time=models.ForeignKey(Heure_d, on_delete=models.CASCADE)
    create_date= models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural =('Reservations')
        
    def __str__(self):
        return self.nom
