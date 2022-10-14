#
# client para consultar dados ao servidor
#
# Referencia
# https://docs.python.org/3.7/library/http.client.html
#
import http.client

urls=["www.gruposouzalima.com","www.deltasystems.com.br"]

for url in urls:
    conn = http.client.HTTPSConnection( url )
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.read()  # This will return entire content.
    # The following example demonstrates reading data in chunks.
    conn.request("GET", "/")
    r1 = conn.getresponse()
    while True:
        chunk = r1.read(200)  # 200 bytes
        if not chunk:
            break
        print(repr(chunk))


