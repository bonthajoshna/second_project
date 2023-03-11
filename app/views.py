from django.shortcuts import render

# Create your views here.
def sample(reqest):
    return render(reqest,'sample.html')