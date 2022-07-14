
from django.shortcuts import render
from django.http import HttpResponse
from firstPage.models import get_df,get_plot
from firstPage.utils import get_db_register, get_db_login
import pandas as pd
from django.contrib.staticfiles import finders
import json
# Create your views here.
def index(request):
    context = {'a':''}
    return render(request,'index.html',context)
   
def analysis(request):
    result = finders.find('datasets/symbol.csv')
    filename = pd.read_csv(result)
    json_records = filename.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    return render(request,'analysis.html', {'data': data})

def predictValue(request):
    temp = {}
    if request.method == 'POST':
        temp['stocksymbol'] = request.POST.get('stocksymbol')
        start = pd.to_datetime('12-05-2020')
        end = pd.to_datetime('12-05-2022')
        df = get_df(temp['stocksymbol'], start , end)
        response = get_plot(df,temp['stocksymbol'])
        txt = f'{response[1]}'
        pred_value = txt.replace('[','').replace(']','')
    return render(request,'analysis.html',{'chart': response[0], 'pred_price': pred_value})

def login(request):
    context = {'a':''}
    return render(request,'login.html',context)

def validateRegisterCredentials(request):
    temp = {}
    res=''
    if request.method == 'POST':
        temp['email'] = request.POST.get('email')
        temp['password'] = request.POST.get('password')
        temp['number'] = request.POST.get('number')
        temp['name'] = request.POST.get('name')
        res = get_db_register(temp)
        return render(request,'login.html',{'res':res, 'display': "show" })
    return render(request,'login.html',{'res':res, 'display': "hide" })

def validateLoginCredentials(request):
    temp = {}
    if request.method == 'POST':
        temp['email'] = request.POST.get('email')
        temp['password'] = request.POST.get('password')
        res = get_db_login(temp)
        if res == 'admin':
            return render(request,'controlpanel.html')    
        if res!= True:
            return render(request,'login.html',{'res':res, 'display': "show" })    
    return render(request,'index.html',temp)


def controlpanel(request):
    return render(request,'controlpanel.html')    
    
def forgotpassword(request):
    return render(request, 'forgot.html')