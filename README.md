PyTorch Flower Classifier 🌸

This project is a deep learning-based flower classification system built using PyTorch. The model is trained on a dataset containing images of five different types of flowers: Daisy, Dandelion, Rose, Sunflower, and Tulip. The project also includes a web demo built with Flask, allowing users to upload an image and get a prediction in real-time.

Features:
- Deep Learning Model: Uses a pre-trained ResNet-18 model fine-tuned for flower classification.
- Advanced Metrics: Includes not just accuracy but also precision, recall, and F1-score for a more nuanced evaluation.
- Confusion Matrix: Provides a detailed view of the model's performance.
- Web Demo: A Flask-based web interface for real-time classification.
- Confidence Threshold: Filters out predictions below a certain confidence level, providing more reliable results.

Technologies Used:
- PyTorch
- Flask
- HTML/CSS
- Python
- Installation and Setup

How To Use:

git clone https://github.com/YourUsername/PyTorchFlowerClassifier.git
Navigate to the project directory and create a virtual environment:

cd PyTorchFlowerClassifier
python -m venv venv
Activate the virtual environment:

On Windows: .\venv\Scripts\Activate
On macOS and Linux: source venv/bin/activate
Install the required packages:

pip install -r requirements.txt
Run the Flask app:

cd flask_app
python app.py
Open your web browser and go to http://127.0.0.1:5000/.

Usage
Click the "Upload" button to upload an image of a flower.
Click "Classify" to get the prediction.
The result will be displayed along with the confidence level.

License
MIT License
