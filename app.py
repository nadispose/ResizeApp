import os
from flask import Flask, render_template, request, send_from_directory
#from PIL import Image
#from resizeimage import resizeimage

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route ("/upload", methods = ["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print (target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create directory: {}".format(target))
    print(request.files.getlist("file"))
    
    for upload in request.files.getlist("file"):
        print(upload)
        #print("{} is the file name".format(upload, filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save to: ", destination)
        
        
        # with send_from_directory("images", filename) as f:
        #with Image.open(f) as image:
        #        cover = resizeimage.resize_cover(image, [200, 100])
        #        cover.save(filename, destination)


        upload.save(destination)
    return render_template("complete.html", image_name = filename)
#To download the file:
#return send_from_directory("images", filename, as_attachment = True)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

#to view all images together (not needed for assignment:)
@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    return render_template("gallery.html", image_name = image_names)



if __name__ == "__main__":
    app.run(debug=True)
