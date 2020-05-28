from flask import Flask,request
import json
app = Flask(__name__)
from flask_cors import CORS
CORS(app)

@app.route('/',methods=['POST'])
def hello():
    query_string = str(request.get_data())
    query_string = request.get_data().decode('utf-8')

    query_string = json.loads(query_string)
    question_string = query_string['query']
    selected_ontology = query_string['ontology']
    print(question_string)
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True,port=8005)