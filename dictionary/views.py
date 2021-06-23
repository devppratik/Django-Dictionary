from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    
    meaning = dictionary.meaning(search)
    verb_meaning ,noun_meaning = None, None
    
    if(meaning == None):
        meaning = "No meaning found!"
    if 'Verb' in meaning :
        verb_meaning = meaning['Verb'][0]
    if 'Noun' in meaning:
        noun_meaning = meaning['Noun'][0]
    
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    
    context = {
        'word' : search,
        'noun_meaning' : noun_meaning,
        'verb_meaning' : verb_meaning,
        'synonyms' : synonyms,
        'antonyms' : antonyms    
    }
    return render(request, 'word.html', context)
