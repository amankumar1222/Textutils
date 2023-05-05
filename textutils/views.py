from django.http import HttpResponse 
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')





def analyze(request):
     #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off' )

    #check wich checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        parms = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', parms)


    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        parms = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}

        #Analyze the text
        return render(request, 'analyze.html', parms)
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        parms = {'purpose':'Removed NewLines', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', parms)
    
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
          
        parms = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', parms)
    else:
        return HttpResponse("Error")









def removepunc(request):
   
    return HttpResponse("remove punc")

def capfirst(request):
    
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("new line remover")

def spaceremove(request):
    return HttpResponse("space remover")

def charcount(request):
    return HttpResponse("space remover")




