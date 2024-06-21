# gif_creator.py
import subprocess

def create_gif(input_video, start_time, duration, output_gif):
    command = [
        'ffmpeg',
        '-ss', str(start_time),
        '-t', str(duration),
        '-i', input_video,
        '-vf', 'fps=10,scale=320:-1:flags=lanczos',
        '-y', output_gif
    ]
    subprocess.run(command, check=True)
