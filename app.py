from flask import Flask, render_template, request
import torch
import torch.nn as nn
import torch.nn.functional as F  # Added for softmax
from torchvision import models, transforms
from PIL import Image
import io

app = Flask(__name__)

# Initialize the model architecture first
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 5)  # Assuming 5 classes

# Then load the state dictionary
model_state = torch.load('best_model_epoch_8.pth')
model.load_state_dict(model_state)

# Finally, set to evaluation mode
model.eval()


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image = Image.open(file)
            transform = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
            ])
            image = transform(image).unsqueeze(0)
            output = model(image)

            # Convert to probabilities using softmax
            probabilities = F.softmax(output, dim=1)

            # Get the maximum probability and corresponding class index
            confidence, predicted_class = torch.max(probabilities, 1)

            # Set your confidence threshold
            confidence_threshold = 0.6

            classes = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

            if confidence.item() < confidence_threshold:
                result_text = f'The image is not confidently recognized. Highest confidence is for {classes[predicted_class]} with confidence {confidence.item()}'
            else:
                result_text = f'The image is a {classes[predicted_class]} with confidence {confidence.item()}'

            return render_template('results.html', result_text=result_text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
