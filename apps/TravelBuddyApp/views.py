# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from .models import UserRegistration
from models import *
import bcrypt

def user_registration(request):
    errors = UserRegistration.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        pw = request.POST["password"]
        hash1 = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        b = UserRegistration.objects.create(name=request.POST["name"], username=request.POST["username"], password=hash1)
        request.session['name'] = request.POST["name"]
        request.session["user_id"] = b.id
        return redirect("/travels")
def login(request):
    errors = UserRegistration.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/")
    else:
        user = UserRegistration.objects.get(username = request.POST["username"])
        request.session['name'] = user.name
        request.session["user_id"] = user.id
        return redirect("/travels")
def index(request):
    return render(request, 'index.html')
def add_travel(request):
    return render(request, 'add.html')
def logout(request):
    request.session.flush()
    return redirect('/')
def add(request):
    errors = TravelPlans.objects.add_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect("/travels/add")
    else:
        a = UserRegistration.objects.get(name=request.session['name'])
        TravelPlans.objects.create(destination=request.POST["destination"], description=request.POST["description"], travel_date_from=request.POST["travel_date_from"], travel_date_to=request.POST["travel_date_to"], user = a)
        return redirect("/travels")
def travels(request):
    c = UserRegistration.objects.get(id=request.session["user_id"])
    d = UserRegistration.objects.exclude(id=request.session["user_id"])
    context = {
        "travel_plans" : TravelPlans.objects.filter(user = c),
        "others_plans" : TravelPlans.objects.filter(user = d),
        "joined_plans" : TravelPlans.objects.filter(travelers=request.session["user_id"])}
    

    return render(request, 'travels.html', context)
def destination(request, id):
    context = {
        "travel_plans" : TravelPlans.objects.get(id=id)
        }
    return render(request, 'destination.html', context)
def join(request, id):
    userjoin = UserRegistration.objects.get(id=request.session["user_id"])
    e = TravelPlans.objects.get(id=id)
    userjoin.trips.add(e)  
    return redirect('/travels')
    # e.travelers=request.session["user_id"]
