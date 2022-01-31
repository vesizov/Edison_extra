from django.shortcuts import render
from .sense import kashpirovskiy, david_blaine, houdini


def home(request):
    return render(request, 'home.html')


def extra(request):
    user_number = request.GET['user_number']

    story = request.session.get('story', '')
    request.session['story'] = story + ' ' +user_number

    tries=request.session.get('tries', 1)
    request.session['tries'] = tries+1

    k_num = request.session.get('k_num', 0)
    request.session['k_num'] = kashpirovskiy.abracadabra(user_number)
    k_bingos = request.session.get('k_bingos', 0)
    if user_number == kashpirovskiy.number:
        request.session['k_bingos'] = k_bingos + 1
    k_accuracy = k_bingos/tries * 100
    kashpirovskiy_res = {'name':'Анатолий Кашпировский',
                         'sense_number': k_num,
                         'sense_bingos': k_bingos,
                         'sense_accuracy': round(k_accuracy, 2)}

    db_num = request.session.get('db_num', 0)
    request.session['db_num'] = david_blaine.abracadabra(user_number)
    db_bingos = request.session.get('db_bingos', 0)
    if user_number == david_blaine.number:
        request.session['db_bingos'] = db_bingos + 1
    db_accuracy = db_bingos / tries * 100
    db_res={'name':'David Blane',
            'sense_number': db_num,
            'sense_bingos': db_bingos,
            'sense_accuracy': round(db_accuracy, 2)}

    harry_num = request.session.get('harry_num', 0)
    request.session['harry_num'] = houdini.abracadabra(user_number)
    harry_bingos = request.session.get('harry_bingos', 0)
    if user_number == houdini.number:
        request.session['harry_bingos'] = harry_bingos + 1
    harry_accuracy = harry_bingos / tries * 100
    harry_res = {'name':'Harry Houdini',
                 'sense_number': harry_num,
                 'sense_bingos': harry_bingos,
                 'sense_accuracy': round(harry_accuracy, 2)}

    result = (kashpirovskiy_res, db_res, harry_res)

    return render(request, 'extra.html',
                  {'tries':tries, 'user_number': user_number, 'result':result, 'story':story})
