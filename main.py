'''from flask import Flask,request,jsonify
from flask_cors import CORS
import os,pix

app = Flask(__name__)
CORS(app)
p  =pix.PixModel()

data = []


@app.route("/",methods = ['GET'])
def get_data():

    if len(data) == 0:
        return jsonify({"message" : "Nada no momento "}), 200
    return jsonify(data),200

@app.route("/webhooks",methods = ["POST"])
def web_hooks():
     result = request.get_json()
     data.append(*result)
     
     p.check_cob(txid= dict(*result).get("txId") )
     return jsonify({
            "message" : "sucess" }),200

if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
    #,host="0.0.0.0"
    '''


from flask import Flask,jsonify,request

app = Flask(__name__)

events = []


@app.route("/webhooks",methods= ['POST'])
def post_events():
    data = request.get_json()
    events.append(data)
    return jsonify(data)

@app.route("/",methods=['GET'])
def get_events():
    return jsonify(events)


if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
#,host="0.0.0.0"

