import re
import random
import csv
import os
from random import shuffle
import ast
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from models import Question


def home(request):
    question_types_list = []
    return render(request, 'index.html', {"question_types_list":question_types_list})


def get_question_types():
    return ["hello", "byebye"]


def process_question(request):
    question_types = request.POST.getlist('question_types')
    nsfw = request.POST['nsfw']
    question = get_question(question_types, nsfw)
    return render(request, 'index.html', {"question": question,
                                          "question_types": question_types,
                                          "nsfw": nsfw})


def get_question(question_types, nsfw):
    question_pool = []
    for question_type in question_types:
        question_pool.extend(list(question_pool.filter(type=question_type)))

    return question_pool[random.randint(0, len(question_pool)-1)]


def get_csv_data(filename):
    data = []
    workpath = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(workpath, filename + '.csv'), 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    data.pop(0)  # to remove the first row, which is the heading
    return data


def refresh_database():
    # clear database
    Question.objects.all().delete()

    # question
    data = get_csv_data("question")
    for row in data:
        Question.objects.create(question=int(row[0]),
                                type=row[1],
                                nsfw=bool(row[2]))