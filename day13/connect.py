import requests
import pandas as pd
import pprint

api_key = 'xyz'
movie_id = 400
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie'
search_query = 'EndGame'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}'

r = requests.get(endpoint)
movie_ids = set()
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        for result in results:
            _id = result['id']
            movie_ids.add(_id)

output = 'movies.csv'
movie_data = []
if movie_ids:
    for movie_id in movie_ids:
        api_version = 3
        api_base_url = f'https://api.themoviedb.org/{api_version}'
        endpoint_path = f'/movie/{movie_id}'
        endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
        r = requests.get(endpoint)
        if r.status_code in range(200, 299):
            data = r.json()
            movie_data.append(data)

if movie_data:
    df = pd.DataFrame(movie_data)
    df.to_csv(output, index=False)

