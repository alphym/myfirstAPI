
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime
from easynmt import EasyNMT

model = EasyNMT('opus-mt')

storage = FastAPI(title='MY FASTAPI')


@storage.get('/')
def index():
    return "this is the my first pageeeee"

@storage.get('/today')
def today():
    return str(datetime.now())

@storage.get('/mynames')
def names(first_name: bool = False, last_name: bool= False, full_name: bool=False):
    full_names = ""
    if first_name:
        full_names += 'Fofo'
    if last_name:
        full_names += 'M'
    if full_name:
        full_names += 'Fofo RWANDA'

    return full_names
@storage.get('/translation')
def translate(text : str = ''):
  response = model.translate([text], target_lang='fr')
  return response[0]
@storage.get('/translation-form', response_class=HTMLResponse)
def form():
  content =  f"""<html>
  <form action='/translation' method='GET'>
   <input type='text' name='text' placeholder='Please Input your Sentence'>
   <input type='submit' value='submit'>
  </form>
  </html>
  """
  return content