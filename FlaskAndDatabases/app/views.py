from flask import Flask, render_template, request, send_from_directory
from app import app, STATIC_DIR



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        print(email, height)
        return render_template("success.html")


@app.route('/css/<path:filename>')
def handle_css(filename):
    return send_from_directory(app.config[STATIC_DIR], filename)