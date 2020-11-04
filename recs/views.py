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
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def upload(request):
    context = {}
    if request.method == 'POST':
        """File handling"""
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        data_folder = Path("C:/Users/sambe/Projects/Cover_Letter_Analysis/data/documents/")
        document_path = str(data_folder) + '\\'+  uploaded_file.name
        """Recommendation functions"""
        resume_text = document_to_text(document_path)
        basic_documentdf = compile_document_text(resume_text)
        verbose_documentdf = text_to_bagofwords(basic_documentdf)
        recommend_df = join_and_condense(verbose_documentdf)
        cosine_sim = vectorize_text(recommend_df)
        recommended_jobs = recommend_100(recommend_df, cosine_sim)
        final_jobs = format_recommendations(recommended_jobs)


        context['recommendations'] = final_jobs
        context['recommendation_0'] = final_jobs[0]
        # final_jobs.pop(0)
        context['recommendation_1'] = final_jobs[1]
        # final_jobs.pop(0)
        context['recommendation_2'] = final_jobs[2]

    if request.is_ajax():
        text = request.GET.get('button_text')
        test = 'test'
        print()
        print(text)
        print()
        print('test')


   # if request.method == 'GET':
        # text = request.GET.get('button_text')
        # print()
        # print(text)
        # print()



        # final_jobs.pop(0)
    # if thumbs up button clicked:
        # scrape jobs related to that job title
        # put jobs in dictionary with keys of
        # job title, company, link to job application, description, date posted, location, full-time/part-time, remote?
    return render(request, 'rookieplays/upload.html', context)
