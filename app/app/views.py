from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')


def analyze(request):
    #receive data from index.html
    received_text = request.POST.get('text', 'default')
    print(received_text)
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    
    #punctuation list
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    
    #check which checkboxes are on or off
    #remove punctuations
    punch_less_text = ''
    final_text = received_text
    if removepunc == 'on':
        for char in received_text:
            if char not in punctuations:
                punch_less_text += char
        final_text = punch_less_text
    
    #upper case words
    upper_cased_text = ''
    if fullcaps == 'on':
        for char in final_text:
            upper_cased_text += char.upper()
        final_text = upper_cased_text
    
    #new line remover
    new_line_removed = ''
    if newlineremover == 'on':
        for char in final_text:
            if char != '\n' and char != '\r':
                new_line_removed += char
        final_text = new_line_removed
        
    #extra space remover
    extra_space_removed = ''
    if spaceremover == 'on':
        for index in range(len(final_text)):
            if final_text[index] == ' ' and final_text[index+1] == ' ':
                pass
            else:
                extra_space_removed += final_text[index]
        final_text = extra_space_removed
             
        
    params = {'purpose': 'removed punctuations', 'analyzedText': final_text}
    return render(request, 'analyze2.html', params)
    