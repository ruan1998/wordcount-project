from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for i in wordlist:
        worddictionary[i] = worddictionary.get(i, 0)+1
    sorteddic = sorted(worddictionary.items(), key=lambda x:x[1], reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':sorteddic})

def about(request):
    return render(request, 'about.html')
