from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from contact.forms import ContactForm 
  

def create(request):
    if request.method == 'POST':
        context = {
        'forms':ContactForm(request.POST)      
        }
         
        return render(
            request,
            "contact/create.html",
            context,
        )
        
            
    
   
    context = {
        'forms':ContactForm()      
    }
    
    
    return render(
        request,
        "contact/create.html",
        context,
    )
    