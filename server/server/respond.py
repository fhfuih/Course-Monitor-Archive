from . import retriever

from server.json_rectifier import get_correct_json
from server.json_rectifier import get_error_json

sem_list = [
    {
        'name': '2022-23 Spring',
        'semCode': 2230,
    },
    {
        'name': '2022-23 Fall',
        'semCode': 2210,
    },
    {
        'name': '2021-22 Summer',
        'semCode': 2140,
    },
    {
        'name': '2021-22 Spring',
        'semCode': 2130,
    },
    {
        'name': '2021-22 Winter',
        'semCode': 2120,
    },
    {
        'name': '2021-22 Fall',
        'semCode': 2110,
    },
    {
        'name' : '2020-21 Spring',
        'semCode' : 2030,
    },
    {
        'name' : '2020-21 Winter',
        'semCode' : 2020
    },
    {
        'name' : '2020-21 Fall',
        'semCode' : 2010
    },
    {
        'name' : '2019-20 Summer',
        'semCode' : 1940
    },
    {
        'name' : '2019-20 Spring',
        'semCode' : 1930
    },
    {
        'name' : '2019-20 Winter',
        'semCode' : 1920
    },
    {
        'name' : '2019-20 Fall',
        'semCode' : 1910
    },
    {
        'name' : '2018-19 Summer',
        'semCode' : 1840
    },
    {
        'name' : '2018-19 Spring',
        'semCode' : 1830 
    }
]

def default(request):
    return get_correct_json(sem_list)

def semester(request):
    if request.GET:
        if 'semCode' in request.GET:
            return retriever.get_sem_info(request.GET['semCode'])
        else:
            return get_error_json('Parameter(s) missing.')
    else:
        return get_error_json('Please use GET method to get info.')

def course(request):
    if request.GET:
        if 'semCode' in request.GET and \
            'courseCode' in request.GET:
            return retriever.get_course_section(request.GET['semCode'], request.GET['courseCode'])
        else:
            return get_error_json('Parameter(s) missing.')
    else:
        return get_error_json('Please use GET method to get info.')

def section(request):
    if request.GET:
        if 'semCode' in request.GET and \
            'courseCode' in request.GET and \
            'section' in request.GET:
            args = [
                request.GET['semCode'],
                request.GET['courseCode'],
                request.GET['section'],
                request.GET['startTime'] if 'startTime' in request.GET else -1,
                request.GET['endTime'] if 'endTime' in request.GET else -1,
                ]
            return retriever.get_data(*args)
        else:
            return get_error_json('Parameter(s) missing.')
    else:
        return get_error_json('Please use GET method to get info.')
