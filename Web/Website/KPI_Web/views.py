from django.shortcuts import render
import requests as r
from .forms import InvestmentsByCity, InvestmentsByCityProgress
from django.core.paginator import Paginator #import Paginator

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

    if request.method == "POST":

        context = {}

        form = InvestmentsByCity(request.POST)
        if form.is_valid():
            progress = form.cleaned_data["entry"]
            url = "http://127.0.0.1:8000/investments/etat/" + progress
            datas = r.get(url)

            if len(datas.json()) > 0:
                context["datas"] = datas.json()
                return render(request, "KPI_Web/listing.html", context)
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

    if request.method == "POST":

        context = {}

        form = InvestmentsByCity(request.POST)
        if form.is_valid():
            code = form.cleaned_data["entry"]
            url = "http://127.0.0.1:8000/investments/code/" + code
            datas = r.get(url)

            if len(datas.json()) > 0:
                context["datas"] = datas.json()
                return render(request, "KPI_Web/listing.html", context)
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

    if request.method == "POST":

        context = {}

        form = InvestmentsByCityProgress(request.POST)
        if form.is_valid():
            city = form.cleaned_data["entry"]
            progress = form.cleaned_data["entry2"]
            url = "http://127.0.0.1:8000/investments/ville_etat/" + city + "+" + progress
            datas = r.get(url)

            if len(datas.json()) > 0:
                context["datas"] = datas.json()
                return render(request, "KPI_Web/listing.html", context)
            else:
                context["form"] = InvestmentsByCityProgress()
                context["bool"] = True
                return render(request, "KPI_Web/city_progress.html", context)

    else:
        context = {}
        context["form"] = InvestmentsByCityProgress()
        context["bool"] = False
        return render(request, "KPI_Web/city_progress.html", context)