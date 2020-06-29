from flask import Flask, jsonify, request, redirect, render_template, send_from_directory
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_image():
    return render_template("index.html")


@app.route("/recognition")#, methods=['POST'])
def Recognition():
    return render_template("resultados.html")
    '''print(request.files['file'])
    file = request.files['file']
    filename = file.filename

    if file and allowed_file(filename):
        file.save("uploads/" + filename)
        return render_template("resultados.html")
        
    return redirect('/')
    '''


@app.route("/image/<filename>")
def show_image(filename):
    return send_from_directory("fotos_bd_2", filename)

if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)