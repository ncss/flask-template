import requests

OPENAI_PROXY_URL = "https://openai.ncss.cloud/v1/chat/completions"
def query_openai(message):
    request_body = {

    }
    ncss_auth = ("group4", "")

    response = requests.post(
        OPENAI_PROXY_URL,
        json=request_body,
        auth=ncss_auth
    )
    data = response.json()

    return data