from flask import Flask, render_template, request, abort
import json

app = Flask(__name__)

with open("books.json", "r", encoding="utf-8") as f:
    books = json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/books")
def book_list():
    category = request.args.get("category")

    if category:
        filtered_books = []

        for book in books:
            if book["category"] == category:
                filtered_books.append(book)
    else:
        filtered_books = books

    return render_template("books.html", books=filtered_books)


@app.route("/books/<int:book_id>")
def book_detail(book_id):
    for book in books:
        if book["id"] == book_id:
            return render_template("book_detail.html", book=book)

    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)