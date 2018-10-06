from flask import Flask, render_template, request
from werkzeug import secure_filename
import databasecontroller
import os

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def homepage():
    return render_template('home.html', community = databasecontroller.getDatabase())

@app.route('/email_list')
def getEmails():
	return render_template('emailView.html', community = databasecontroller.getDatabase())

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploads_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      databasecontroller.load_data(f.filename)
      return '''<html><head>Cool! File uploaded Successfully.</head><body><p>Return to homepage: <a href="home">homepage</a></p></body></html>'''

if __name__ == '__main__':
	app.run()