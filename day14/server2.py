from fastapi import FastAPI
from scrape import run as scrape_runner

app = FastAPI()


@app.get('/')
def hello_world():
    return {'Hello': 'World'}


@app.get('/abc')
def abc_view():
    return {'data': [1, 2, 3, 4, 5, ]}


@app.post('/box-office-mojo-scraper')
def box_office_scraper_view():
    scrape_runner()
    return {'box_office': 'World'}
