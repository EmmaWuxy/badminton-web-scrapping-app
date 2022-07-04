import requests
def web_request(url, headers):
    # Try to connct 5 times upon connection error
    for i in range(5):
        try:
            response = requests.get(url, headers)
            break
        except requests.exceptions.RequestException as e:
            continue
        
    if response is None or response.status_code != 200:
        raise e
    return response
