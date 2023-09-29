from flask import Flask,render_template,jsonify,request
import json
import cv2
import tensorflow as tf
import numpy as np

# Create an instance of the Flask class
app = Flask(__name__)

model = tf.keras.models.load_model('./cars_planes.h5')
class_names = ["Plane","Car"]


# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/train')
def home_page():
    return render_template('index.html')

@app.route('/model',methods=['POST'])
def modelTraining():
    global model
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        image_path = data["imagepath"]
        vector_image = cv2.imread(image_path,cv2.COLOR_BGR2RGB)
        resized_vector_image = cv2.resize(vector_image,(40,40))
        predictions = model.predict(np.array([resized_vector_image])/255)
        pred = np.argmax(predictions)
        confidence_score = predictions[0][pred]
        data = {"success":True,"prediction":class_names[pred],"confidence":str(confidence_score)}
        return jsonify(data)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
