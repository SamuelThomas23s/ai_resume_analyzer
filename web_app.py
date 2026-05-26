from flask import Flask, request, render_template_string
from file_reader import read_file
from ai import smart_analysis, job_fit_score

app = Flask(__name__)

HTML = """
<h1>AI HR Dashboard</h1>

<form method="post" enctype="multipart/form-data">
  <input type="file" name="file">
  <input type="submit">
</form>

<pre>{{ result }}</pre>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        file = request.files["file"]
        path = "temp.txt"
        file.save(path)

        text = read_file(path)
        result = smart_analysis(text)

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True)