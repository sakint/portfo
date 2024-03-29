from flask import Flask, render_template, url_for, request
app = Flask(__name__)
print(__name__)

@app.route('/<string:page_name>')
def hello_world(page_name):
  return render_template(page_name)

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    mine=data["mine"]
    email=data["email"]
    subject = data["subject"]
    message = data["message"]
    
    file = database.write(f'\n{mine}, {email}, {subject}, {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      data = request.form.to_dict()
      write_to_file(data)
      return ' form submitted'
    else:
      return 'something went wrong'