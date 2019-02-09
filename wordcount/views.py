from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html',{'name':'Hi this is Trideep Ghosh a web Developer','d':'Maker of this website'})

def count(request):
    data = request.GET['fulltextarea']
    word_split = data.split()
    length = len(word_split)

    worddic = {}

    for word in word_split:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    sortr = sorted(worddic.items(),key = operator.itemgetter(1))

    return render(request,'count.html',{'f':data,'len':length,'w':sortr})

def about_me(request):
    return render(request,'about_me.html')
