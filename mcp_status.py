import requests


def get_mcp_waitings_status():

    data = requests.get("http://10.3.36.199/programs/waitings")
    if data.status_code == 200:
        return "There are not waitings"
    else:
        return "There are some waitings"
