from flask import Flask, render_template, request
from yt_dlp import YoutubeDL
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        url = request.form["url"]

        ydl_opts = {
    "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
    "cookiefile": "cookies.txt"
}
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            message = "Video downloaded successfully!"
        except Exception as e:
            message = f"Error: {e}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
