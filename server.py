from flask import Flask,request,render_template,redirect,send_from_directory
from werkzeug.utils import secure_filename
import os
import encoder as enc
import decoder as dec

app=Flask(__name__)

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'


# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'jpeg','png','bmp'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/encrypt',methods=['GET','POST'])
def encrypt():
    if request.method == 'POST':
        # check if the post request has the file part

        if 'up_pic' not in request.files:
            return "No file selected"
            return redirect(request.url)
        file = request.files['up_pic']
        degree = int(request.form.get('degree'))
        pwd = request.form.get('pwd')

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return "No file selected"
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        links = [str(os.path.join(app.config['UPLOAD_FOLDER'], filename))]
        if request.form['submit']=="enc":
            (im,arr,path)=enc.encode(links[0], pwd)
        else:
            (im,arr,path)=dec.decode(links[0], pwd)
        links.append(path)
        return render_template("display.html",link=links)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True) # Flask server is run
