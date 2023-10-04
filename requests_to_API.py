# send the post request with an array of data
headers = {"W-Token": "Ilovemyboss"}
data = [
    {
        'url': '/rest/shifts',
        'params': {'user_id': 0, 'other_stuff': 'value'},
        'method': 'post',
    },
    {
        'url': '/rest/shifts',
        'params': {'user_id': 1,'other_stuff': 'value'},
        'method':'post',
    },
]
requests.post(url, json=data, headers=headers)
