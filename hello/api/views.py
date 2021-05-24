import json
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def add_view(request, *args, **kwargs):
    print(request)
    if request.method == 'POST':
        print(request.body)
        if request.body:
            number = json.loads(request.body)
            if number.get('A') or number.get('A')==0 and number.get('B') or number.get('B')==0:
                try:
                    result = int(number['A']) + int(number['B'])
                    return JsonResponse({'result': result})
                except:
                    response = JsonResponse({'error': "A or B is not a number"})
                    response.status_code = 400
                    return response

            elif number.get('A') or number.get('B'):
                response = JsonResponse({'error': "You didn't write A or B"})
                response.status_code = 400
                return response
            else:
                response = JsonResponse({'error': "Here is an empty dictionary"})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': "It's empty here"})
            response.status_code = 400
            return response


def substract_view(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.body)
        if request.body:
            number = json.loads(request.body)
            if number.get('A') or number.get('A') == 0 and number.get('B') or number.get('B') == 0:
                try:
                    result = int(number['A']) - int(number['B'])
                    return JsonResponse({'result': result})
                except:
                    response = JsonResponse({'error': "A or B is not a number"})
                    response.status_code = 400
                    return response

            elif number.get('A') or number.get('B'):
                response = JsonResponse({'error': "You didn't write A or B"})
                response.status_code = 400
                return response
            else:
                response = JsonResponse({'error': "Here is an empty dictionary"})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': "It's empty here"})
            response.status_code = 400
            return response


def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.body)
        if request.body:
            number = json.loads(request.body)
            if number.get('A') or number.get('A') == 0 and number.get('B') or number.get('B') == 0:
                try:
                    result = int(number['A']) * int(number['B'])
                    return JsonResponse({'result': result})
                except:
                    response = JsonResponse({'error': "A or B is not a number"})
                    response.status_code = 400
                    return response

            elif number.get('A') or number.get('B'):
                response = JsonResponse({'error': "You didn't write A or B"})
                response.status_code = 400
                return response
            else:
                response = JsonResponse({'error': "Here is an empty dictionary"})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': "It's empty here"})
            response.status_code = 400
            return response


def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.body)
        if request.body:
            number = json.loads(request.body)
            if number.get('A') or number.get('A') == 0 and number.get('B'):
                try:
                    result = int(number['A']) / int(number['B'])
                    return JsonResponse({'result': result})
                except:
                    response = JsonResponse({'error': "A or B is not a number"})
                    response.status_code = 400
                    return response
            elif number.get('B') == 0:
                response = JsonResponse({'error': "Division by zero!"})
                response.status_code = 400
                return response

            elif number.get('A') or number.get('B'):
                response = JsonResponse({'error': "You didn't write A or B"})
                response.status_code = 400
                return response
            else:
                response = JsonResponse({'error': "Here is an empty dictionary"})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': "It's empty here"})
            response.status_code = 400
            return response


@ensure_csrf_cookie
def token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse(json.dumps({'token': "ok"}))
    return HttpResponseNotAllowed('Only GET request are allowed')
