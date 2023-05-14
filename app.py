
from flask import Flask,jsonify,request
import modules.reconmendation as rs
import modules.estimation as es
import modules.system as sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/estimation/<product_name>',methods=['GET'])
def estimation(product_name):
    instance=es.EstimatePrice()
    result=instance.Scrape(product_name)
    return jsonify(result)
    
    
@app.route('/api/system-update/',methods=['GET'])
def system():
    instance=sys.System()
    result=instance.Update()
    return jsonify(result)

@app.route('/api/reconmendation/',methods=['POST'])
def reconmendation():
    instance=rs.ReconmendationSys()
    data={
        'id':[request.json['_id']],
        'name':[request.json['name']],
        'description':[request.json['description']],
        'categories':[request.json['categories']],
        'price':[request.json['price']],
    }
    result=instance.contentFiltering(data)
    
    return jsonify(result)

@app.route('/',methods=['GET'])
def index():
    return "Server is running..."
    
if __name__=='__main__':
    app.run()

