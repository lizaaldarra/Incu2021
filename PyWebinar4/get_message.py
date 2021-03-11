import requests

roomId = 'Y2lzY29zcGFyazovL3VzL1JPT00vZGFjMzdkZTItMTg3Ny0zMmJjLTlhM2UtZjQ4NWNiYzE5YmU5'
token = 'NzUxNzU1OTgtYTQzYy00ZDk4LWEzMzEtYjliN2EwNmVhNjczN2JiODQxNzItNjM0_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'

url = "https://webexapis.com/v1/messages?roomId=" + roomId

header = {"content-type": "application/json; charset=utf-8",
         "authorization": "Bearer " + token}

response = requests.get(url, headers = header, verify = True)

print(response.json())
