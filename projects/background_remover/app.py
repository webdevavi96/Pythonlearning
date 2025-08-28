from flask import Flask, render_template, request, redirect, url_for, abort
import requests, os, time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Ensure folders exist
os.makedirs("static/uploads", exist_ok=True)
os.makedirs("static/downloads", exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "img" not in request.files:
        abort(400)

    image = request.files["img"]

    if image.filename == "":
        abort(400)

    if not image.mimetype.startswith("image/"):
        abort(404)

    ext = os.path.splitext(image.filename)[1]
    new_image = f"uploads_{int(time.time())}{ext}"
    upload_path = os.path.join("static/uploads", new_image)

    image.save(upload_path)

    return removeBackgroundRequest(new_image)


def removeBackgroundRequest(image):
    url = "https://api.remove.bg/v1.0/removebg"

    upload_path = os.path.join("static/uploads", image)

    with open(upload_path, "rb") as img_file:
        response = requests.post(
            url,
            files={"image_file": img_file},
            data={"size": "auto"},
            headers={"X-Api-Key": os.getenv("API")},
        )

    if response.status_code == requests.codes.ok:
        output_file = f"no_bg_{int(time.time())}.png"
        output_path = os.path.join("static/downloads", output_file)

        with open(output_path, "wb") as out:
            out.write(response.content)

        os.remove(upload_path)

        return redirect(url_for("preview", filename=output_file))
    else:
        print("Error:", response.status_code, response.text)
        return "Error removing background"


@app.route("/preview/<filename>")
def preview(filename):
    return render_template("no-bg.html", filename=filename)


@app.errorhandler(400)
def bad_request(e):
    return render_template("400.html"), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
