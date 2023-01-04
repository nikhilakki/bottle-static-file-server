# Copyright (c) 2023 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pathlib import os
from bottle import Bottle, run, template, static_file

PATH = os.path.join(os.getcwd(), "files")
os.makedirs(PATH, exist_ok=True)
app = Bottle()


@app.route("/files/<filename:path>")
def serve_static(filename):
    return static_file(filename, root=PATH)


@app.route("/")
def hello():
    files = os.listdir(PATH)
    return template(
        """
        <h2>Files in folder {{ PATH }}</h2>
        <p>
            <ol>
                % for file in files:
                <li> <a href=/files/{{ file }}>{{ file }}</a></li>
                % end
            </ol>
        </p>
    """,
        PATH=PATH,
        files=files,
    )


run(app, host="0.0.0.0", port=8080)
