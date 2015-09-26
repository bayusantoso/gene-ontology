from flask import render_template, flash, redirect
from app import app
from .forms import SearchForm

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
  form = SearchForm()
  return render_template('index.html', form=form)

@app.route('/result', methods=['GET','POST'])
def result():
  form = SearchForm()
  return render_template('result.html', form = form)

@app.route('/detail', methods=['GET','POST'])
def detail():
  form = SearchForm()
  return render_template('detail.html', form = form)
