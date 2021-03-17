# KPI_test by Alexandre BENARD

This is project I made for KPI Intelligence technical test.
The initial test can be found [here](https://github.com/kpi-intelligence/technical-test).

Both stages 1 and 2 were entirely made.
I also added an endpoint to edit investment and a map to web app as bonus stage.

The API REST part is located in *API* folder.
The web application is in *Web* folder.
Both are given with specific virutal environment based on python 3.9 but *requirements.txt* file is provided if needed.

# Installation

First, [download](https://github.com/Qlexio/KPI_test/archive/master.zip) the project in the folder of your choice.

If you don't use python 3.9 and Windows, you'll need to create two virtual environments for both *API* and *Web* parts using this commande:

`python3 -m venv /<path to>/API/env`

Then, activate virtual environement:
* On Linux:
  * `source env/bin/activate`
* On Windows:
  * `env/Scripts/activate`

At last, install packages using:
`pip install -r requirements.txt`

Create a second virtual environment in `/<path to>/Web/`

# Running

You'll need two terminals to run this project. One for API REST part and one for Web app.
* API:
  * Go to *API* folder: `cd ./<path to>/API`.
  * Run virtual environment you created or run `./KPI_venv/Scripts/activate` command if you use python 3.9 and Windows.
  * Go to *API_REST* folder: `cd ./API_REST/`
  * Run API server: `python3 manage.py runserver`
* Web:
  * Go to *Web* folder: `cd ./<path to>/Web`.
  * Run virtual environment you created or run `./Web_venv/Scripts/activate` command if you use python 3.9 and Windows.
  * Go to *Website* folder: `cd ./Website/`
  * Run Web server: `python3 manage.py runserver 8080`

Use `127.0.0.1:8080` url in your browser to access web application.

You may want to access API in your browser to have an overview. You can use `127.0.0.1:8000/investments/` for exemple.

Enjoy !!!
