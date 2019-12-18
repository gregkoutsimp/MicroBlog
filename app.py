from flask import Flask,render_template,request
import datetime
import database

app = Flask(__name__)


database.create_tables()

@app.route("/home",methods = ["GET","POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        # entries.append({"content": entry_content, "date" :datetime.datetime.today().strftime("%b %d")})
        database.create_entry(entry_content, datetime.datetime.today().strftime("%b %d"))
    return render_template("home.html",entries = database.retrieve_entries())

