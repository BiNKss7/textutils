#Created by Sonam
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def analyze(request):
    #Getting the text from the user input
    djtext= (request.POST.get('text', 'default'))

    #Check boxvalue,this gives if on or off
    removepunc= (request.POST.get('removepunc', 'off'))
    fullcaps= (request.POST.get('fullcaps', 'off'))
    newlineremover= (request.POST.get('newlineremover', 'off'))
    spaceremover= (request.POST.get('spaceremover', 'off'))
    charcount= (request.POST.get('charcount', 'off'))

    #Check which checkbox is on
    if removepunc == "on":
        analyzed= ""
        punctuation= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuation:
                analyzed= analyzed+ char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps== "on":
        analyzed=""
        for char in djtext:
            analyzed= analyzed+ char.upper()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover== "on":
        analyzed = ""
        for char in djtext:
            if char!= "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover== "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]== " "):
                analyzed= analyzed + char
        params = {'purpose': 'Remove Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount== "on":
        analyzed = 0
        for char in djtext:
            analyzed+=1
        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}

    if removepunc!="on" and fullcaps!="on" and spaceremover!="on" and newlineremover!="on" and charcount!="on":
        return HttpResponse("Please Choose one option")

    return render(request, 'analyze.html', params)

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

