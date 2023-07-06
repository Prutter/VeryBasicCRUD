from flask import Flask, render_template, redirect

app = Flask(__name__)
entries = {}  # Dictionary to store the data

@app.route('/create/<key>/<value>')
def create_entry(key, value):
    entries[key] = value
    return redirect('/read')

@app.route('/read')
def read_entries():
    return entries

@app.route('/update/<key>/<value>')
def update_entry(key, value):
    if key in entries:
        entries[key] = value
    return redirect('/read')

@app.route('/delete/<key>')
def delete_entry(key):
    if key in entries:
        del entries[key]
    return redirect('/read')

if __name__ == '__main__':
    app.run(debug=True)
