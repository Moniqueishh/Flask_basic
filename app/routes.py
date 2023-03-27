from app import app

@app.route("/")
def homePage():
    return "Home Page!"
