# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from  datetime import *
import bcrypt
password_regex = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 3:
            errors["name"] = "Name should be more than 3 characters"
        if len(postData["username"]) < 3:
            errors["username"] = "Username should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password should be more thatn 8 characters"
        # elif not password_regex.match(postData["password"]):  
        #     errors["password"] = "Invalid password"
        if postData["password"] != postData["confirm"]:
            errors["confirm"] = "Password confirmation does not match"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData["username"]) < 3:
            errors["username"] = "Username should be more than 3 characters"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be longer than 8 characters"
        check = UserRegistration.objects.filter(username=postData["username"])
        if len(check) == 0:
            errors["password"] = "Password test"
            return errors
        if not bcrypt.checkpw(postData["password"].encode(), check[0].password.encode()):
            errors["password"] = "Password doesn't match"
        return errors
    def add_validator(self, postData):
        errors = {}
        if len(postData["destination"]) < 1:
            errors["destination"] = "Destination field cannot be empty"
        if len(postData["description"]) < 1:
            errors["description"] = "Description field cannot be empty"
        if len(postData["travel_date_from"]) < 1:
            errors["travel_date_from"] = "Travel Date From field cannot be empty"
        if len(postData["travel_date_to"]) < 1:
            errors["travel_date_to"] = "Travel Date To field cannot be empty"
        if postData["travel_date_from"] < datetime.now().strftime("%Y-%m-%d"):
            errors["travel_date_from"] = "Travel Date From needs to be in the future"   
        
        if postData["travel_date_to"] < postData["travel_date_from"]:
            errors["travel_date_to"] = "Travel Date From needs to be in the future"
        return errors

class UserRegistration(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()

class TravelPlans(models.Model):
    destination = models.CharField(max_length=255)
    travel_date_from = models.DateField(null=True, blank=True)
    travel_date_to = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(UserRegistration, related_name = "destination")
    travelers = models.ManyToManyField(UserRegistration, related_name = "trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()