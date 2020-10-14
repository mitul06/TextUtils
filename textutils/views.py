# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspacermover = request.POST.get('extraspacermover', 'off')

    # checkbox value which one is on
    if removepunc == 'on':
        punctuation = '''!@#$%&*(){}:"?><~`[];',./\|-=,.'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed += char
        params = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Capitalize Text', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspacermover == 'on':
        analyzed = ""
        for i, char in enumerate(djtext):
            if not(djtext[i] == " " and djtext[i] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remove', 'analyzed_text': analyzed}

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspacermover != 'on'):
        return HttpResponse("<h1> Error </h1>")

    return render(request, 'analyze.html', params)