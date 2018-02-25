# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from pprint import pprint
import json
import re

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from datetime import datetime
# Create your views here.
from .models import TestDB

def dashboard(request):
    _all = TestDB.objects.all()
    print _all
    return render(request, 'index.html')
