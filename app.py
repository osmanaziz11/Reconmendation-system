
from flask import Flask,jsonify
import modules.estimation as estimation

app = Flask(__name__)


@app.route('/api/<product>',methods=['GET'])
def main(product):
    resp=estimation.Handler()
    res=resp.Scrape(product)
    if res!= 0:
        return jsonify({"status":1,"Details":res})
    else:
        return jsonify({"status": 0})
    
@app.route('/api/system-update/',methods=['GET'])
def update():
    return jsonify({"status": 0})

@app.route('/api/system/content',methods=['GET'])
def update():
    return jsonify({"status": 0})


@app.route('/',methods=['GET'])
def index():
    return "Server is running..."
    
if __name__=='__main__':
    app.run()

