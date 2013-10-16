import httplib, urllib, json, time, math, random
def setColor(conn, i, h, s, v):
    params = json.dumps({'hue': h, 'sat': s, 'bri': v, 'on': True}) 
    headers = {"Content-type": "text/plain", "Accept": "text/plain"}
    url = str.format("/api/timdeveloper/lights/{0}/state", i+1)
    conn.request("PUT", url, params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data

conn = httplib.HTTPConnection("192.168.1.114")
random.seed()
i = random.randrange(0, 100000)
while True:
    for k  in range (0, 3):
        t = float(i/2 - k*200)/15
        h = int((math.sin(t*0.8)+1)*32230)
        s = int((math.cos(t*0.7)+1)*127)
        v = int((math.cos(1.3 + t*0.9)+1)*100)+54
        setColor(conn, k, h, s, v)
    time.sleep(0.25)
    i += 1

conn.close()
