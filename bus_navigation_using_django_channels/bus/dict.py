from .models import *

DB = {'lines': [
    {'name': 'Bagheri',
     'stations': [
         {'name': "Borzuyi",     'x_pos': 35.748783, 'y_pos': 51.529489, 'next': "Daneshvar",   'prev': "Daneshvar",    'is_final_station': 'True'},
         {'name': "Daneshvar",   'x_pos': 35.745979, 'y_pos': 51.526678, 'next': "Khodabande",  'prev': "Borzuyi",      'is_final_station': 'False'},
         {'name': "Khodabande",  'x_pos': 35.737053, 'y_pos': 51.520359, 'next': "Taghato",     'prev': "Daneshvar",    'is_final_station': 'False'},
         {'name': "Taghato",     'x_pos': 35.736356, 'y_pos': 51.519501, 'next': "Seraj",       'prev': "Khodabande",   'is_final_station': 'False'},
         {'name': "Seraj",       'x_pos': 35.737114, 'y_pos': 51.513954, 'next': "Kababi",      'prev': "Taghato",      'is_final_station': 'False'},
         {'name': "Kababi",      'x_pos': 35.738159, 'y_pos': 51.506090, 'next': "41",          'prev': "Seraj",        'is_final_station': 'False'},
         {'name': "41",          'x_pos': 35.739065, 'y_pos': 51.499063, 'next': "Meydan57",    'prev': "Kababi",       'is_final_station': 'False'},
         {'name': "Meydan57",    'x_pos': 35.739709, 'y_pos': 51.493870, 'next': "Hengam",      'prev': "41",           'is_final_station': 'False'},
         {'name': "Hengam",      'x_pos': 35.739961, 'y_pos': 51.492046, 'next': "Meydan57",    'prev': "Meydan57",     'is_final_station': 'True'}],
     'buses': [
        {'speed': "", 'x_pos': 35.747381,   'y_pos': 51.5280835,    'next': "Daneshvar",    'prev': "Borzuyi",      'is_on_station': "False",   'token': "qwerty"},
        {'speed': "", 'x_pos': 35.745979,   'y_pos': 51.526678,     'next': "Khodabande",    'prev': "Daneshvar",      'is_on_station': "True",    'token': "qwerty"},
        {'speed': "", 'x_pos': 35.7367045,  'y_pos': 51.5200000,    'next': "Taghato",      'prev': "Khodabande",    'is_on_station': "False",   'token': "qwerty"},
        {'speed': "", 'x_pos': 35.736687,   'y_pos': 51.517006,     'next': "Seraj",        'prev': "Taghato",   'is_on_station': "False",   'token': "qwerty"},
        {'speed': "", 'x_pos': 35.737114,   'y_pos': 51.513954,     'next': "Kababi",       'prev': "Seraj",      'is_on_station': "True",    'token': "qwerty"},
        {'speed': "", 'x_pos': 35.737445,   'y_pos': 51.511663,     'next': "41",           'prev': "Kababi",        'is_on_station': "False",   'token': "qwerty"},
        {'speed': "", 'x_pos': 35.747381,   'y_pos': 51.5280835,    'next': "Meydan57",     'prev': "41",       'is_on_station': "False",   'token': "qwerty"},
        {'speed': "", 'x_pos': 35.739709,   'y_pos': 51.493870,     'next': "Hengam",       'prev': "Meydan57",           'is_on_station': "True",    'token': "qwerty"},
        {'speed': "", 'x_pos': 35.739961,   'y_pos': 51.492046,     'next': "Meydan57",     'prev': "Hengam",     'is_on_station': "True",    'token': "qwerty"}, ]},

    {'name': 'Resalat',
     'stations':
        [{'name': "Resalat",    'x_pos': 35.730373, 'y_pos': 51.535745, 'next': "121st",      'prev': "121st",    'is_final_station': 'True'},
         {'name': "121st",      'x_pos': 35.731183, 'y_pos': 51.530091, 'next': "Hojr",       'prev': "Resalat",  'is_final_station': 'False'},
         {'name': "Hojr",       'x_pos': 35.731505, 'y_pos': 51.527516, 'next': "Gas",        'prev': "121st",    'is_final_station': 'False'},
         {'name': "Gas",        'x_pos': 35.732141, 'y_pos': 51.522752, 'next': "Bagheri",    'prev': "Hojr",     'is_final_station': 'False'},
         {'name': "Bagheri",    'x_pos': 35.732820, 'y_pos': 51.517581, 'next': "Yas",        'prev': "Gas",      'is_final_station': 'False'},
         {'name': "Yas",        'x_pos': 35.733516, 'y_pos': 51.512161, 'next': "shaparak",   'prev': "Bagheri",  'is_final_station': 'False'},
         {'name': "shaparak",   'x_pos': 35.734230, 'y_pos': 51.507226, 'next': "mehr",       'prev': "Yas",      'is_final_station': 'False'},
         {'name': "mehr",       'x_pos': 35.734805, 'y_pos': 51.502559, 'next': "salehi",     'prev': "shaparak", 'is_final_station': 'False'},
         {'name': "salehi",     'x_pos': 35.735275, 'y_pos': 51.498707, 'next': "sarsabz",    'prev': "mehr",     'is_final_station': 'False'},
         {'name': "sarsabz",    'x_pos': 35.735275, 'y_pos': 51.498707, 'next': "salehi",     'prev': "salehi",   'is_final_station': 'True'}],
     'buses': [
         {'speed': "", 'x_pos': 35.730756, 'y_pos': 51.533331, 'next': "121st",     'prev': "Resalat",  'is_on_station': "False",   'token': "qwerty"},
         {'speed': "", 'x_pos': 35.731183, 'y_pos': 51.530091, 'next': "Hojr",      'prev': "121st",    'is_on_station': "True",    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.732022, 'y_pos': 51.523732, 'next': "Gas",       'prev': "Hojr",     'is_on_station': "False",   'token': "qwerty"},
         {'speed': "", 'x_pos': 35.732141, 'y_pos': 51.522752, 'next': "Bagheri",   'prev': "Gas",      'is_on_station': "True",    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.733211, 'y_pos': 51.514920, 'next': "Yas",       'prev': "Bagheri",  'is_on_station': "False",   'token': "qwerty"},
         {'speed': "", 'x_pos': 35.733516, 'y_pos': 51.512161, 'next': "shaparak",  'prev': "Yas",      'is_on_station': "True",    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.734527, 'y_pos': 51.504759, 'next': "mehr",      'prev': "shaparak", 'is_on_station': "False",   'token': "qwerty"},
         {'speed': "", 'x_pos': 35.734805, 'y_pos': 51.502559, 'next': "salehi",    'prev': "mehr",     'is_on_station': "True",    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.735275, 'y_pos': 51.498707, 'next': "sarsabz",   'prev': "salehi",   'is_on_station': "True",    'token': "qwerty"}, ]},

    {'name': 'Hengam',
     'stations': [
        {'name': "Cheraghi",    'x_pos': 35.755564, 'y_pos': 51.511877, 'next': "6th",          'prev': "6th",          'is_final_station' :'True'},
        {'name': "6th",         'x_pos': 35.753492, 'y_pos': 51.509420, 'next': "Azadegan",     'prev': "Cheraghi",     'is_final_station' :'False'},
        {'name': "Azadegan",    'x_pos': 35.752125, 'y_pos': 51.507553, 'next': "Hasanpoor",    'prev': "6th",          'is_final_station' :'False'},
        {'name': "Hasanpoor",   'x_pos': 35.750392, 'y_pos': 51.505225, 'next': "Varbaz",       'prev': "Azadegan",     'is_final_station' :'False'},
        {'name': "Varbaz",      'x_pos': 35.748694, 'y_pos': 51.502843, 'next': "shahr",        'prev': "Hasanpoor",    'is_final_station' :'False'},
        {'name': "shahr",       'x_pos': 35.745185, 'y_pos': 51.498036, 'next': "mehr",         'prev': "Varbaz",       'is_final_station' :'False'},
        {'name': "mehr",        'x_pos': 35.743339, 'y_pos': 51.495869, 'next': "Bahar",        'prev': "shahr",        'is_final_station' :'False'},
        {'name': "Bahar",       'x_pos': 35.741617, 'y_pos': 51.493867, 'next': "mehr",         'prev': "mehr",         'is_final_station' :'True'}],
     'buses': [
         {'speed': "", 'x_pos': 35.755564, 'y_pos': 51.511877, 'next': "6th",       'prev': "Cheraghi",          'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.753492, 'y_pos': 51.509420, 'next': "Azadegan",  'prev': "6th",     'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.752125, 'y_pos': 51.507553, 'next': "Hasanpoor", 'prev': "Azadegan",          'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.750392, 'y_pos': 51.505225, 'next': "Varbaz",    'prev': "Hasanpoor",     'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.748694, 'y_pos': 51.502843, 'next': "shahr",     'prev': "Varbaz",    'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.745185, 'y_pos': 51.498036, 'next': "mehr",      'prev': "shahr",       'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.743339, 'y_pos': 51.495869, 'next': "Bahar",     'prev': "mehr",        'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.741617, 'y_pos': 51.493867, 'next': "mehr",      'prev': "Bahar",         'is_on_station': 'True',    'token': "qwerty"}, ]},

    {'name': 'Emam-Ali HW',
     'stations': [
        {'name': "Emam_ali",    'x_pos':35.758475, 'y_pos':51.484625, 'next':"aras"		, 'prev': "aras",      'is_final_station': 'True'},
        {'name': "aras",        'x_pos':35.755941, 'y_pos':51.485097, 'next':"park"		, 'prev': "Emam_ali",  'is_final_station': 'False'},
        {'name': "park",        'x_pos':35.752719, 'y_pos':51.485312, 'next':"sohrab"	, 'prev': "aras",      'is_final_station': 'False'},
        {'name': "sohrab",       'x_pos':35.749811, 'y_pos':51.484153,'next':"boostan"	, 'prev': "park",      'is_final_station': 'False'},
        {'name': "boostan",     'x_pos':35.747129, 'y_pos':51.483391, 'next':"taleghani", 'prev': "sohrab",	   'is_final_station': 'False'},
        {'name': "taleghani",   'x_pos':35.744475, 'y_pos':51.483115, 'next':"Farjam" 	, 'prev': "boostan"	 , 'is_final_station': 'False'},
        {'name': "Farjam",      'x_pos':35.742150, 'y_pos':51.483662, 'next':"nazemi"	, 'prev': "taleghani", 'is_final_station': 'False'},
        {'name': "nazemi",      'x_pos':35.739024, 'y_pos':51.483565, 'next':"Farjam" 	, 'prev': "Farjam",    'is_final_station': 'True'}],
     'buses': [
         {'speed': "", 'x_pos': 35.758475, 'y_pos': 51.484625, 'next':"aras",        'prev': "Emam_ali",    'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.755941, 'y_pos': 51.485097, 'next':"park",       'prev': "aras",         'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.752719, 'y_pos': 51.485312, 'next':"sohrab",     'prev': "park",         'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.749811, 'y_pos': 51.484153, 'next':"boostan",    'prev': "sohrab",       'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.747129, 'y_pos': 51.483391, 'next':"taleghani",  'prev': "boostan",	    'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.744475, 'y_pos': 51.483115, 'next':"Farjam",     'prev': "taleghani",    'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.742150, 'y_pos': 51.483662, 'next':"nazemi",     'prev': "Farjam",       'is_on_station': 'True',    'token': "qwerty"},
         {'speed': "", 'x_pos': 35.739024, 'y_pos': 51.483565, 'next':"Farjam",     'prev': "nazemi",       'is_on_station': 'True',    'token': "qwerty"}, ]}
]}


def build_stations(db_line, station):
    name = station['name']
    x = station['x_pos']
    y = station['y_pos']
    is_final = station['is_on_station']
    return Station.objects.create(line=db_line, name=station['name'], x_pos=x, y_pos=y, is_final_station=is_final)


def update_station_next_and_prev(db_stations, station_name):
    station = db_stations[station_name]['db']
    next = db_stations[station_name]['next']
    prev = db_stations[station_name]['prev']
    station.next_station = db_stations[next]
    station.prev_station = db_stations[prev]
    station.save()


def build_bus(bus, db_stations, db_line):
    speed = bus['speed']
    if not speed:
        speed = 5
    x = bus['x_pos']
    y = bus['y_pos']
    next = db_stations[bus['next']]['db']
    prev = db_stations[bus['prev']]['db']
    is_on = bus['is_on_station']
    Bus.objects.create(line=db_line,
                       speed=speed, x_pos=x, y_pos=y,
                       next_station=next, prev_station=prev,
                       is_on_station=is_on)


def build_db():
    lines = DB['lines']
    for line in lines:
        db_line = Line.objects.create(name=line['name'])
        db_stations = {}
        for station in line['stations']:
            db_stations[station['name']]['db'] = build_stations(db_line, station)
            db_stations[station['name']]['next'] = station['next']
            db_stations[station['name']]['prev'] = station['prev']
        for station_name in db_stations:
            update_station_next_and_prev(db_stations, station_name)
        for bus in line['buses']:
            build_bus(bus, db_stations, db_line)
