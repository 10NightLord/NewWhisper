from flask import Flask, request, render_template
from moviepy.editor import VideoFileClip
from main import main

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def home():
    errors = ""
    if request.method == "POST":
        video = None

        try:
            file = request.files["video"]
            file.save('temp_video.mp4')
            video = VideoFileClip('temp_video.mp4')
             
            # we need to validate if model is empty or not if empty then we need to set it to base
            model = request.form["model"]
            if model == "":
                model = "base"
        except:
            errors += "<p>{!r} is not a valid file.</p>\n".format(request.files["video"])
        if video is not None:
            result = main(video,model)

            return render_template("result.html", result=result)
    return render_template("home.html", errors=errors)

if __name__ == "__main__":
    # Mmust use port 80 to work with Docker app feature.
    app.run(port=80, host="0.0.0.0")
