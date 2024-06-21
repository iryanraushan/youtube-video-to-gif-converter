# app.py
from flask import Flask, request, render_template, send_file
import os
import uuid
from downloader import download_video
from gif_creator import create_gif

app = Flask(__name__)

# Ensure directories exist
os.makedirs('videos', exist_ok=True)
os.makedirs('gifs', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        start_time = int(request.form['start_time'])
        duration = int(request.form['duration'])
        
        # Download video
        video_filename = download_video(url, 'videos')
        
        # Create unique GIF filename
        gif_filename = f'{uuid.uuid4()}.gif'
        gif_path = os.path.join('gifs', gif_filename)
        
        # Create GIF
        create_gif(video_filename, start_time, duration, gif_path)
        
        return send_file(gif_path, as_attachment=True)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
