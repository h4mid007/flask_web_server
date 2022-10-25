# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)



@app.route('/query-example', methods=['GET'])
def query_example():
    language = request.args.get('language')
    return language

  
  
@app.route('/form-example', methods=['POST'])
def form_example():
    if request.method == 'POST':
      language = request.form.get('language')
      framework = request.form.get('framework')
    return 'Form Data Example'

  
  
@app.route('/json-example')
def json_example():
    request_data = request.get_json()  // auto json loads
    language = request_data['language']
    return 'JSON Object Example'

  
  
  
if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=100)
