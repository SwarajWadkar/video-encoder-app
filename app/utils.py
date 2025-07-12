import subprocess

def encode_video(input_path, output_path):
    command = [
        "ffmpeg","-y",
        "-i", input_path,
        "-vf", "scale=1280:720",
        output_path
    ]
    subprocess.run(command, check=True)
