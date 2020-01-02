from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from query import models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    print(request.POST.get("username"))
    resp = {"status":True, 'company_num' : "111", "stock_num":'222'}
    res = JsonResponse(resp)
    res["Access-Control-Allow-Origin"] = "*"
    res["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    res["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                          "Access-Control-Allow-Origin," \
                                          "X-Conten-Type-Options," \
                                          "Content-Type,Origin,Accept"
    res["Access-Control-Allow-Credentials"] = "true"
    res["X-Content-Type-Options"] = "nosniff"
    res["Content-Type"] = "application/json; charset=UTF-8"

    return res
    #return render(request, "index.html", res)