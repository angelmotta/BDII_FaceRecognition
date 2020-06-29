from flask import Flask, jsonify, request, redirect, render_template, send_from_directory
from Extraccion import genCaracteristicas, genCaracPic
from KNNEuclidiano import knnSearchED
from KNNManhattan import knnSearchMD
from RTree import buildRTree
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

## Call Backend ##
dirFotos = "fotos_bd_2"
resDB = genCaracteristicas(dirFotos)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_image():
    return render_template("index.html")


@app.route("/recognition", methods=['POST'])
def Recognition():
    return render_template("resultados.html")
    print(request.files['file'])
    file = request.files['file']
    filename = file.filename

    if file and allowed_file(filename):
        image_path = "uploads/" + filename
        file.save(image_path)
        q_pic = genCaracPic(image_path)
        result = knnSearchED(resDB, q_pic, 16)
        print(result)
        for index, score in result:
            print(resDB[index][0])
            print(score)
        return render_template("resultados.html")

    return redirect('/')


@app.route("/image/<filename>")
def show_image(filename):
    return send_from_directory(dirFotos, filename)


if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)
