
from django.shortcuts import render
from django.http import HttpResponse
from firstPage.models import get_df,get_plot
from firstPage.utils import get_db_register, get_db_login, setcookie
import pandas as pd
from django.contrib.staticfiles import finders
import json
from django.contrib.auth import login, authenticate, logout
# from decode import decode_data_values 
from firstPage.encode import encode_data_values
# Create your views here.
jwt = {}
def index(request):
    res = ''
    if request.user.is_authenticated:
        
        print("user login")
    return render(request,'index.html',{'res':res})
   
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
    res = ''
    return render(request,'login.html',{'res':res})

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
        jwt = encode_data_values(temp)
        print(setcookie(jwt))

        if res[0] == 'admin':
            return render(request,'controlpanel.html', {'res': res[0]})    
        elif res[0] != 'user':
            return render(request,'login.html',{'res':res[0] })    
    return render(request,'index.html',{'res': res[1]})


def controlpanel(request):
    return render(request,'controlpanel.html')    
    

def logout_request(request):
    res = ''
    logout(request)
    return render(request, 'index.html', {'res':res})
