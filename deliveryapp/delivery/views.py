from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser


def index(request):
    return HttpResponse("Hello")