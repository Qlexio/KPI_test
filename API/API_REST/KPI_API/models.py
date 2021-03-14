from django.db import models

# Create your models here.

class JsonDataset(models.Model):

    # Create model to put json in DB
    titreoperation = models.CharField(max_length= 256, null= True)
    entreprise = models.CharField(max_length= 256, null= True)
    annee_de_livraison = models.CharField(max_length= 256, null= True)
    ville = models.CharField(max_length= 256, null= True)
    mandataire = models.CharField(max_length= 256, null= True)
    nombre_de_lots = models.DecimalField(max_digits= 10, decimal_places=3, null= True)
    ppi = models.CharField(max_length= 256, null= True)
    lycee = models.CharField(max_length= 256, null= True)
    notification_du_marche = models.CharField(max_length= 256, null= True)
    codeuai = models.CharField(max_length= 256, null= True)
    longitude = models.DecimalField(max_digits= 17, decimal_places=15, null= True)
    etat_d_avancement = models.CharField(max_length= 256, null= True)
    montant_des_ap_votes_en_meu = models.DecimalField(max_digits= 10, decimal_places=3, null= True)
    cao_attribution = models.CharField(max_length= 256, null= True)
    latitude = models.DecimalField(max_digits= 17, decimal_places= 15, null= True)
    maitrise_d_oeuvre = models.CharField(max_length= 256, null= True)
    mode_de_devolution = models.CharField(max_length= 256, null= True)
    annee_d_individualisation = models.CharField(max_length= 256, null= True)
    enveloppe_prev_en_meu = models.DecimalField(max_digits= 10, decimal_places= 3, null= True)