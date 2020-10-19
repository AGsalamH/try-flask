from flask import Flask, render_template, redirect, request
from repos.searchApi import repos_with_most_starts

app = Flask(__name__)

available_languages = ["Java", "Python", "JavaScript","Rust"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        selected_languages = available_languages

    elif request.method == "POST":
        selected_languages = request.form.getlist("languages") 

    results = repos_with_most_starts(selected_languages)

    return render_template(
        "index.html", 
        selected_languages = selected_languages,
        available_languages = available_languages,
        results = results
    )


if __name__ == "__main__":
    app.run(debug=True)
