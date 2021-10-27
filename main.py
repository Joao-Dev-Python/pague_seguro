from flask import Flask,request,jsonify
import os

app = Flask(__name__)


data = []


@app.route("/roms",methods = ['GET'])
def get_data():

    if len(data) == 0:
        return jsonify({"message" : "Nada no momento "}), 200
    return jsonify(data),200

@app.route("/webhooks",methods = ["POST"])
def web_hooks():
     result = request.get_json()
     data.append(result)
     return jsonify({
            "message" : "sucess" }),200

if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port)
    #,host="0.0.0.0"