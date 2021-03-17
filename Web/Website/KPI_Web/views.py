from django.shortcuts import render
import requests as r
from .forms import InvestmentsByCity, InvestmentsByCityProgress, InvestmentsEntries
from django.core.paginator import Paginator #import Paginator
import json

# Create your views here.

def index(request):
    return render(request, "KPI_Web/index.html")

def investments(request):

    # Get datas
    datas = r.get("http://127.0.0.1:8000/investments")
    json_datas = datas.json()
    # Pagination
    paginator = Paginator(json_datas, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "KPI_Web/listing.html", context={"datas": page_obj})

def investments_by_city(request):

    # Watch if "page" is in url
    # If not it is the first time we access the page
    # else put session value in POST
    if not request.method == "POST":
        if "page" not in request.get_full_path():
            request.session["entry"] = ""
        else:
            request.POST = request.session["entry"]
            request.method = "POST"

    if request.method == "POST":

        context = {}

        form = InvestmentsByCity(request.POST)
        # Get post value in session
        request.session["entry"] = request.POST

        if form.is_valid():

            # Get datas
            city = form.cleaned_data["entry"]
            url = "http://127.0.0.1:8000/investments/ville/" + city
            datas = r.get(url)

            json_datas = datas.json()
            # Pagination
            paginator = Paginator(json_datas, 5)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

            if len(json_datas) > 0:
                
                return render(request, "KPI_Web/listing.html", context={"datas":page_obj})
            else:
                context["form"] = InvestmentsByCity()
                context["bool"] = True
                return render(request, "KPI_Web/city.html", context)

    else:
        context = {}
        context["form"] = InvestmentsByCity()
        context["bool"] = False
        return render(request, "KPI_Web/city.html", context)

def investments_by_progress(request):

    if not request.method == "POST":
        if "page" not in request.get_full_path():
            request.session["entry"] = ""
        else:
            request.POST = request.session["entry"]
            request.method = "POST"

    if request.method == "POST":

        context = {}

        form = InvestmentsByCity(request.POST)
        request.session["entry"] = request.POST

        if form.is_valid():
            progress = form.cleaned_data["entry"]
            url = "http://127.0.0.1:8000/investments/etat/" + progress
            datas = r.get(url)

            json_datas = datas.json()
            # Pagination
            paginator = Paginator(json_datas, 5)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

            if len(json_datas) > 0:
                
                return render(request, "KPI_Web/listing.html", context={"datas": page_obj})
            else:
                context["form"] = InvestmentsByCity()
                context["bool"] = True
                return render(request, "KPI_Web/progress.html", context)

    else:
        context = {}
        context["form"] = InvestmentsByCity()
        context["bool"] = False
        return render(request, "KPI_Web/progress.html", context)

def investments_by_code(request):

    if not request.method == "POST":
        if "page" not in request.get_full_path():
            request.session["entry"] = ""
        else:
            request.POST = request.session["entry"]
            request.method = "POST"

    if request.method == "POST":

        context = {}

        form = InvestmentsByCity(request.POST)
        request.session["entry"] = request.POST

        if form.is_valid():
            code = form.cleaned_data["entry"]
            url = "http://127.0.0.1:8000/investments/code/" + code
            datas = r.get(url)

            json_datas = datas.json()
            # Pagination
            paginator = Paginator(json_datas, 5)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

            if len(json_datas) > 0:
                context["datas"] = datas.json()
                return render(request, "KPI_Web/listing.html", context={"datas": page_obj})
            else:
                context["form"] = InvestmentsByCity()
                context["bool"] = True
                return render(request, "KPI_Web/code.html", context)

    else:
        context = {}
        context["form"] = InvestmentsByCity()
        context["bool"] = False
        return render(request, "KPI_Web/code.html", context)

def investments_by_city_progress(request):

    if not request.method == "POST":
        if "page" not in request.get_full_path():
            request.session["entry"] = ""
        else:
            request.POST = request.session["entry"]
            request.method = "POST"

    if request.method == "POST":

        context = {}

        form = InvestmentsByCityProgress(request.POST)
        request.session["entry"] = request.POST
        
        if form.is_valid():
            city = form.cleaned_data["entry"]
            progress = form.cleaned_data["entry2"]
            url = "http://127.0.0.1:8000/investments/ville_etat/" + city + "+" + progress
            datas = r.get(url)

            json_datas = datas.json()
            # Pagination
            paginator = Paginator(json_datas, 5)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

            if len(json_datas) > 0:
                
                return render(request, "KPI_Web/listing.html", context={"datas": page_obj})
            else:
                context["form"] = InvestmentsByCityProgress()
                context["bool"] = True
                return render(request, "KPI_Web/city_progress.html", context)

    else:
        context = {}
        context["form"] = InvestmentsByCityProgress()
        context["bool"] = False
        return render(request, "KPI_Web/city_progress.html", context)

def new_investment(request):

    if request.method == "POST":

        context = {}
        
        form = InvestmentsEntries(request.POST)

        if form.is_valid():
            # Get form values and create dict
            datas = {}
            datas["titreoperation"] = form.cleaned_data["titreoperation"]
            datas["entreprise"] = form.cleaned_data["entreprise"]
            datas["annee_de_livraison"] = form.cleaned_data["annee_de_livraison"]
            datas["ville"] = form.cleaned_data["ville"]
            datas["mandataire"] = form.cleaned_data["mandataire"]
            datas["nombre_de_lots"] = form.cleaned_data["nombre_de_lots"]
            datas["ppi"] = form.cleaned_data["ppi"]
            datas["lycee"] = form.cleaned_data["lycee"]
            datas["notification_du_marche"] = form.cleaned_data["notification_du_marche"]
            datas["codeuai"] = form.cleaned_data["codeuai"]
            datas["longitude"] = form.cleaned_data["longitude"]
            datas["etat_d_avancement"] = form.cleaned_data["etat_d_avancement"]
            datas["montant_des_ap_votes_en_meu"] = form.cleaned_data["montant_des_ap_votes_en_meu"]
            datas["cao_attribution"] = form.cleaned_data["cao_attribution"]
            datas["latitude"] = form.cleaned_data["latitude"]
            datas["maitrise_d_oeuvre"] = form.cleaned_data["maitrise_d_oeuvre"]
            datas["mode_de_devolution"] = form.cleaned_data["mode_de_devolution"]
            datas["annee_d_individualisation"] = form.cleaned_data["annee_d_individualisation"]
            datas["enveloppe_prev_en_meu"] = form.cleaned_data["enveloppe_prev_en_meu"]

            url = "http://127.0.0.1:8000/investments/"
            response = r.post(url, data=datas)
            if response.status_code == 201:
                return render(request, "KPI_Web/success.html")
            else:
                context["form"] = form
                context["error"] = False
                context["status"] = True
                context["code"] = response.status_code
                return render(request, "KPI_Web/new.html", context)

        else:
            context["form"] = form
            context["error"] = True
            context["status"] = False
            return render(request, "KPI_Web/new.html", context)

    else:
        context = {}
        context["form"] = InvestmentsEntries()
        context["error"] = False
        context["status"] = False
        return render(request, "KPI_Web/new.html", context)

def investments_map(request):

    import folium

    # Investments are on Paris area, so center the map on Paris
    paris_coord = [48.856614, 2.3522219]
    map = folium.Map(location=  paris_coord)

    # Get datas from API
    datas = r.get("http://127.0.0.1:8000/investments")
    json_datas = datas.json()
    
    # Add marker to map
    for i in json_datas:
        popup = ""
        if i["longitude"] == None or i["latitude"] == None:
            continue
        else:
            for k, v in i.items():
                popup += f"{k.capitalize()}: {v}<br>"
            folium.Marker([float(i["latitude"]), float(i["longitude"])], popup=popup).add_to(map)

    map.save("./KPI_Web/static/Image/map_save.html")

    return render(request, "KPI_Web/map.html")
    