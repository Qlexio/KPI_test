from django.db import models

# Create your models here.

class JsonDataset(models.Model):

    # Create model to put json in DB
    titreoperation = models.CharField(max_length= 256)
    entreprise = models.CharField(max_length= 256)
    annee_de_livraison = models.CharField(max_length= 256)
    ville = models.CharField(max_length= 256)
    mandataire = models.CharField(max_length= 256)
    ppi = models.CharField(max_length= 256)
    lycee = models.CharField(max_length= 256)
    notification_du_marche = models.CharField(max_length= 256)
    codeuai = models.CharField(max_length= 256, unique= True)
    longitude = models.DecimalField(max_digits= 17, decimal_places=15)
    etat_d_avancement = models.CharField(max_length= 256)
    montant_des_ap_votes_en_meu = models.DecimalField(max_digits= 10, decimal_places=3)
    cao_attribution = models.CharField(max_length= 256)
    latitude = models.DecimalField(max_digits= 17, decimal_places= 15)
    maitrise_d_oeuvre = models.CharField(max_length= 256)
    mode_de_devolution = models.CharField(max_length= 256)
    annee_d_individualisation = models.CharField(max_length= 256)
    enveloppe_prev_en_meu = models.DecimalField(max_digits= 10, decimal_places= 3)