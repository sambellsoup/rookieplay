from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Document

# recommendation packages
from .text_processing import document_to_text, compile_document_text, text_to_bagofwords, join_and_condense, vectorize_text, recommend_100, format_recommendations, top_100_categories, freq, viz_data, make_viz

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from rake_nltk import Rake
from tika import parser
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from pathlib import Path

# Job Search API
from serpapi import GoogleSearchResults

from time import time

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "recs/index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "recs/db.html", {"greetings": greetings})
