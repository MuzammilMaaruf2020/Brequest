from flask import Flask
from flask import render_template,jsonify
app = Flask(__name__,template_folder='template')


Works = [{
  'id' : 1,
  'category': 'Carpentry works'},

  
  {'id' : 2,
  'category': 'Plumbing works'},

  
  {'id' : 3,
  'category': 'Masonry works'
  
},

   
  {'id' : 4,
  'category': 'General works'
  
}       
  
]

@app.route("/api/works")
def list_works():
  return jsonify(Works)


@app.route("/")
def hello_world():
  return render_template('home.html',works=Works)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
