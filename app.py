from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num_versions = int(request.form.get('num_versions', '2'))
        except ValueError:
            num_versions = 2
        return render_template('compare.html', num_versions=num_versions)
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        num_versions = int(request.form.get('num_versions', '2'))
    except ValueError:
        num_versions = 2

    code_versions = []
    for i in range(num_versions):
        code = request.form.get(f'code{i}', '')
        code_versions.append(code)

    diffs = []
    for i in range(num_versions - 1):
        lines1 = code_versions[i].splitlines()
        lines2 = code_versions[i+1].splitlines()
        diff_table = difflib.HtmlDiff(wrapcolumn=80).make_table(
            lines1, lines2,
            fromdesc=f'Version {i+1}',
            todesc=f'Version {i+2}',
            context=True, numlines=3
        )
        diffs.append(diff_table)

    return render_template('result.html', diffs=diffs)

if __name__ == '__main__':
    app.run(debug=True) 