from flask import Flask, render_template, request
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

import io

def extract_text(file):
    file_content = file.read()
    reader = PyPDF2.PdfReader(io.BytesIO(file_content))
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

@app.route("/", methods=["GET","POST"])
def home():

    score = None

    if request.method == "POST":

        resume = request.files["resume"]
        job_desc = request.form["job"]

        resume_text = extract_text(resume)

        documents = [resume_text, job_desc]

        tfidf = TfidfVectorizer()

        matrix = tfidf.fit_transform(documents)

        similarity = cosine_similarity(matrix[0:1], matrix[1:2])

        score = round(similarity[0][0] * 100,2)

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)