import requests
from requests.exceptions import HTTPError
from .githubRepo import GithubRepo
def create_query(languages, min_stars=50000):
    """ Creates a query parameter for Github API Url """
    query = f"stars:>{min_stars} "
    for language in languages:
        query += f"language:{language} " 
    return query

def repos_with_most_starts(languages, sort="stars", order_by="desc", min_stars=50000):
    """ Returns list of Dictionaries """
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages,min_stars)
    request_params = {"q":query, "sort":sort, "order":order_by }
    
    # Send request to Github Api
    response = requests.get(gh_api_repo_search_url, params=request_params)
    status_code = response.status_code
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
    response_json = response.json()  
    # response_json is a dictionary that contains [total_count, incomplete_results, items] as keys
    # items key is what we are looking for
    response_items = response_json["items"]
    return [GithubRepo(item["name"], item["language"], item["stargazers_count"]) for item in response_items]