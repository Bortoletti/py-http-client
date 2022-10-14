#
# envio de informacoes por POST
#
# Referencia
# https://docs.python.org/3.7/library/http.client.html
#
import http.client, urllib.parse

url = ""

headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})


conn = http.client.HTTPSConnection( url )
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()
