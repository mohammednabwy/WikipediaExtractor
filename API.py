#Libraries
import warnings
warnings.filterwarnings("ignore")
from flask import Flask
from flask import  request
from Service import WikiExtractor
import jsonpickle
#--------------------------------------------------------
#Public Variables
app = Flask(__name__)
#--------------------------------------------------------
@app.route('/')
@app.route('/home')
def home():
    return "Welcome to Wiki Extractor" 

@app.route('/api/v1/extractWikipediaInfo', methods=["GET"])
def extractTextFromImage():    
    keyword=request.args["keyword"]   
    wikiResult=WikiExtractor.extractInfoFromWikipedia(keyword)
    json_string=jsonpickle.encode(wikiResult,unpicklable=False)       
    response = app.response_class(
        response=json_string,
        status=200,
        mimetype='application/json'
    )
    return response    
#-----------------------------------------------------
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

