from flask import Flask, jsonify, request, redirect, render_template
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            file.save("uploads/"+file.filename)
            return "Hecho"

    return render_template("index.html")


@app.route("/recognition", methods=['POST'])
def Recognition():
    print(request.files['file'])
    file = request.files['file']
    filename = file.filename

    if file and allowed_file(filename):
        # file.save("uploads/" + filename)
        return "Hecho"
        
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)