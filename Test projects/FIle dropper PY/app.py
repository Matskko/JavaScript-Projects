from flask import Flask, render_template, request
from flask_dropzone import Dropzone
import os

app = Flask(__name__)
dropzone = Dropzone(app)

# Configuratie van Dropzone
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_MAX_FILE_SIZE'] = 1  # Max grootte in MB
app.config['DROPZONE_MAX_FILES'] = 10
app.config['UPLOAD_FOLDER'] = 'uploads'  # Map om bestanden op te slaan

# Controleer of de upload map bestaat, anders maken we deze aan
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Sla de geüploade bestanden op in de upload folder
        files = request.files.getlist('file')
        for file in files:
            if file:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
        return "Bestanden succesvol geüpload."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
