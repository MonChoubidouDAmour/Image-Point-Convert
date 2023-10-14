from flask import Flask, render_template, request, send_from_directory
from PIL import Image
from PNGtoTXT import image_to_txt

app = Flask(__name__)

# Helper function to process the uploaded image
def get_python_data(image, width, height, ratio):
    resized_image = Image.open('static/uploaded_image.jpg')
    python_data = image_to_txt(image, width, height, ratio)
    return python_data

# Route for the main page
@app.route('/')
def index():
    python_data = "Data comes from a Python script!"
    return render_template('index.html', python_data=python_data)

# Route for handling image uploads
@app.route('/upload', methods=['POST'])
def upload():
    uploaded_height = int(request.form.get('integer_value', default=None))
    uploaded_decimal = float(request.form.get('decimal_value', default=None))
    uploaded_height = int((uploaded_height // 4) * 4)
    uploaded_width = int(((uploaded_decimal * uploaded_height) // 2) * 2)
    uploaded_ratio = float(request.form.get('ratio', default=None))
    python_data = None

    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            image.save('static/uploaded_image.jpg')  # Save in the 'static' folder
            resized_image = Image.open('static/uploaded_image.jpg')
            resized_image = resized_image.resize((int(uploaded_decimal * uploaded_height), uploaded_height))
            resized_image = resized_image.convert('L')
            resized_image.save('static/uploaded_image.jpg')
            python_data = get_python_data(Image.open('static/uploaded_image.jpg'), uploaded_width, uploaded_height, uploaded_ratio)
            print(python_data)
    else:
        return index()

    return render_template('index.html', python_data=python_data, uploaded=True)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('static', filename)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
