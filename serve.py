import os
import subprocess

from gevent.pywsgi import WSGIServer
from flask import Flask, render_template, request

app = Flask(__name__)

def doi2bib(doitext):
   return subprocess.check_output(["doi2bib", doitext],universal_newlines=True)

@app.route('/', methods=['GET'])
def api():
    if request.method == 'GET':
        url = request.args.get('url', type=str)
        if not url:
            return render_template('doi2bib.html')
        else:
            res=doi2bib(url) 
    return render_template("doi2bib.html",result=str(res).lstrip())

if __name__ == "__main__":
    http_server = WSGIServer(('', int(os.environ.get('PORT', 8080))), app)
    http_server.serve_forever()