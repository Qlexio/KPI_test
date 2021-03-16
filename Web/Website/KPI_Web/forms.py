from django import forms

class InvestmentsByCity(forms.Form):
    entry = forms.CharField(max_length= 256)

class InvestmentsByCityProgress(forms.Form):
    entry = forms.CharField(max_length= 256)
    entry2 = forms.CharField(max_length= 256)

class InvestmentsEntries(forms.Form):

    #Form to post new entry
    titreoperation = forms.CharField(max_length= 256, required= False)
    entreprise = forms.CharField(max_length= 256, required= False)
    annee_de_livraison = forms.CharField(max_length= 256, required= False)
    ville = forms.CharField(max_length= 256, required= False)
    mandataire = forms.CharField(max_length= 256, required= False)
    nombre_de_lots = forms.CharField(max_length= 256, required= False)
    ppi = forms.CharField(max_length= 256, required= False)
    lycee = forms.CharField(max_length= 256, required= False)
    notification_du_marche = forms.CharField(max_length= 256, required= False)
    codeuai = forms.CharField(max_length= 256, required= False)
    longitude = forms.CharField(max_length= 256, required= False)
    etat_d_avancement = forms.CharField(max_length= 256, required= False)
    montant_des_ap_votes_en_meu = forms.CharField(max_length= 256, required= False)
    cao_attribution = forms.CharField(max_length= 256, required= False)
    latitude = forms.CharField(max_length= 256, required= False)
    maitrise_d_oeuvre = forms.CharField(max_length= 256, required= False)
    mode_de_devolution = forms.CharField(max_length= 256, required= False)
    annee_d_individualisation = forms.CharField(max_length= 256, required= False)
    enveloppe_prev_en_meu = forms.CharField(max_length= 256, required= False)