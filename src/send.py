import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkzMzc1MDgyLCJqdGkiOiJlMTFlMzg3YjljNzY0ZTBkYjUxMjkxZWExNTgyYjg3NCIsInVzZXJfaWQiOjF9.n21CPFIQxe9alrpXAyuqExY1FEfLte3ftRUwhQFfSb8'

r = requests.get('http://127.0.0.1:8000/users', headers= headers)

print(r.text)