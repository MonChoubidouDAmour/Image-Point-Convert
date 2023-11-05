from flask import Flask, render_template, request
from PIL import Image
from PNGtoTXT import image_to_txt
from io import BytesIO
import base64

app = Flask(__name__)

# Helper function to process the uploaded image and return it as a base64 encoded image


def get_image_data(image, width, height, ratio):
    python_data = image_to_txt(image, width, height, ratio)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return python_data, img_base64

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
    img_base64 = None

    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            img_stream = image.stream  # Get the image as a stream
            img_stream.seek(0)  # Rewind the stream
            img = Image.open(img_stream)

            # Process the image and get it as base64
            python_data, img_base64 = get_image_data(
                img, uploaded_width, uploaded_height, uploaded_ratio)
            print(python_data)
    else:
        return render_template('index.html', python_data=None, img_base64=None, uploaded=True,
                               decimal_value=uploaded_decimal, integer_value=uploaded_height, ratio=uploaded_ratio)

    return render_template('index.html', python_data=python_data, img_base64=img_base64, uploaded=True,
                           decimal_value=uploaded_decimal, integer_value=uploaded_height, ratio=uploaded_ratio)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
