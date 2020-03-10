from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from json import dumps, loads, JSONEncoder
from django.http import JsonResponse
from .models import *
import json
import datetime


def CU_refresh():
    with open('C:\\python\\mybbs\\convenience\\CU_salesList.txt', 'r+', encoding='utf-8') as f:
        lst = f.read()
    replaced_lst = lst.replace("'", "\"")
    json_lst = json.loads(replaced_lst)
    for j in json_lst['prodlist']:
        CU = CU_Products(
            prodName=j['prodName'],
            prodPrice=j['prodPrice'],
            prodBonus=j['prodBonus']
        )
        CU.save()


def CU_index(req):
    '''
    print(datetime.datetime.today().day == 10)
    if datetime.datetime.today().day == 10:
        CU_refresh()
    else:
        pass
    '''
    parameter = req.GET.get("q")

    if parameter:
        Prodlist = CU_Products.objects.filter(prodName__contains=parameter)
    else:
        Prodlist = CU_Products.objects.all()

    if req.is_ajax():
        html = render_to_string(
            template_name="convenience/search_partial.html",
            context={"ctx": Prodlist}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    ctx = {'ctx': Prodlist}
    return render(req, 'convenience/CU_index.html', context=ctx)