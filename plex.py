from flask import Flask, request
import json

# Webhook in Plex: http://192.168.188.26:5000/plex
# Webhook Documentation: https://support.plex.tv/articles/115002267687-webhooks/

app = Flask(__name__)

@app.route('/plex', methods=['POST'])
def listener():
    data = request.form.getlist('payload')
    m = data[0]
    n = json.dumps(m)
    o = json.loads(n)
    p = json.loads(o)
    print("event : "+p['event'])
    print("user : "+str(p['user']))
    print("owner : "+str(p['owner']))
    print("Account title : "+p["Account"]['title'])
    print("Server title : "+p["Server"]["title"])
    print("Player title : "+p["Player"]["title"])
    print("Metadata librarySectionTitle : "+p["Metadata"]["librarySectionTitle"])
    return "Ack"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
