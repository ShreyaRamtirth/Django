from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from firstPage.models import get_df,get_plot
from firstPage.utils import add_search, get_db_register, get_db_login, getAllUsers
import pandas as pd
from django.contrib.staticfiles import finders
import json
from firstPage.encode import encode_data_values
from firstPage.decode import decode_data_values
res = ''
jwt = {}


def index(request):
    if 'jwt' in request.COOKIES:
        if request.COOKIES['jwt'] == "{}" or request.COOKIES['jwt'] == {} or request.COOKIES['jwt'] == None or res == '':
            response = render(request,'index.html',{'res':''})
        else:
            response = render(request,'index.html',{'res':res['Name'], 'role': res['role']})
            response.set_cookie('jwt',jwt)
        return response
    else:
        response = render(request,'index.html',{'res':''})
        return response
    


def analysis(request):
    result = finders.find('datasets/symbol.csv')
    filename = pd.read_csv(result)
    json_records = filename.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    global res
    if 'jwt' in request.COOKIES:
        if res == '':
            return render(request,'analysis.html', {'data': data, 'res': res})
        else:
            return render(request,'analysis.html', {'data': data, 'res': res['Name'], 'role': res['role']})
    else:
        res = ''
        return render(request,'analysis.html', {'data': data, 'res': res})



def predictValue(request):
    temp = {}
    if request.method == 'POST':
        temp['stocksymbol'] = request.POST.get('stocksymbol')
        start = pd.to_datetime('12-05-2020')
        end = pd.to_datetime('12-05-2022')
        df = get_df(temp['stocksymbol'], start , end)
        response = get_plot(df,temp['stocksymbol'])
        if request.COOKIES['jwt'] != "{}":
            user = decode_data_values(request.COOKIES['jwt'])
            add_search(temp['stocksymbol'], user)
        txt = f'{response[1]}'
        pred_value = txt.replace('[','').replace(']','')
    return render(request,'analysis.html',{'chart': response[0], 'pred_price': pred_value, 'res': res})


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
    global jwt,res
    if request.method == 'POST':
        temp['email'] = request.POST.get('email')
        temp['password'] = request.POST.get('password')
        res = get_db_login(temp)
        temp['name'] = res[1]
        temp['role'] = res[0]
        jwt = encode_data_values(temp)

        if res[0] == 'admin':
            return redirect('controlpanel')
        elif res[0] != 'user':
            return redirect('/')

    response = render(request,'index.html',{'res': res[1]})
    response.set_cookie('jwt',jwt)
    # print("cookie set ")
    return response


def controlpanel(request):
    if 'jwt' in request.COOKIES:
        if request.COOKIES['jwt'] == {}:
            pass
        else:
            global res
            res = decode_data_values(jwt)
        search = ''
        if request.method == 'GET':
            search = request.GET.get('search')
            users = getAllUsers(search)
            response = render(request,'controlpanel.html', {'res': res['Name'], 'users': users, 'role': res['role']  })
            response.set_cookie('jwt',jwt)
            return response
    else:
        if request.method == 'GET':
            search = request.GET.get('search')
            users = getAllUsers(search)
            response = render(request,'controlpanel.html', {'res': '', 'users': users })
            response.set_cookie('jwt',jwt)
            return response



def logout_request(request):
    global res
    res = ''
    response = render(request, 'index.html', {'res':res})
    response.delete_cookie('jwt')
    # response.set_cookie('jwt',"")
    return response