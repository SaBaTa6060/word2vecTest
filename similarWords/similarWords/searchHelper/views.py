from django.shortcuts import render
from .forms import wordSelectForm

from gensim.models import word2vec

model = word2vec.Word2Vec.load("searchHelper/jawikimodel/wiki.model")

WORD_CHOICES = (
    ('1', '政治'), ('2', '経済'), ('3', '技術'), ('4', 'ゲーム'), ('5', '教育'), ('6', 'スポーツ'), ('7', '芸能人'),
)
CATEGORY = WORD_CHOICES

def results_to_choices(results):
    choices = []
    for i, (word, similarity) in enumerate(results):
        id = str(i+1)
        choices.append((id, word))
    return tuple(choices)

def index(request):
    global WORD_CHOICES
    if(request.method == "POST"):
        form_input = wordSelectForm(data=request.POST)
        id = form_input.data['similarWords']
        choices = dict(WORD_CHOICES)
        choice = choices[id]
        print(choice)
        explanation = " に関連する言葉"
        results = model.most_similar(positive=choice)
        new_choices = results_to_choices(results)
        WORD_CHOICES = new_choices
    else:
        WORD_CHOICES = CATEGORY
        choice = ""
        explanation = "調べたい言葉を選んでください。"
    
    form = wordSelectForm(word_choices=WORD_CHOICES)

    content_dict = {
        'title': "searchHelper",
        'selected_word': choice,
        'explanation': explanation,
        'form': form
    }
    return render(
        request,
        "searchHelper/index.html",
        content_dict
    )

