from hashlib import sha256
from flask import request

@app.route("/sqlinject/2", methods=["POST"])
def login():
    username = request.form["username"]
    escaped_username = mysql_real_escape_string(username)
    password_bytes = ("bungle-" + \
request.form["password"]).encode("latin-1")
    password_digest = sha256(password_bytes).digest().decode("latin-1")
    query = "SELECT * FROM users WHERE username='" + escaped_username
    query += "' AND password='" + password_digest + "'"
    selected_users = mysql.execute(query).fetchall()
    if len(selected_users) > 0:
        return "Login successful!"
    else:
        return "Incorrect username or password."