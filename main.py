from flask import Flask,render_template,request,redirect
import database
app = Flask('app')

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/login')
def login_page():
  return render_template("login.html")

@app.route('/signup')
def signup_page():
  print(request.args)
  return render_template("signup.html", email=request.args.get("e"))

@app.route('/home', methods=["GET","POST"])
def home_page():
  r = request.form
  print(r.get("signup"))
  if request.method == "POST" and r.get("login") == "":
    return render_template("homepage.html", data=[r["email"],r["password"]])
  else:
    return render_template("homepage.html", data="")
    
  if request.method == "POST" and r.get("signup") == "":
    re = database.add_user(r["username"],r["email"],r["password"])
    if re == 0:
      return render_template("homepage.html", data=[r["username"],r["email"],r["password"]])
    else:
      return redirect("https://NorcalSpring23.botman2424.repl.co/signup?e=This Email is Already in use")

app.run(host='0.0.0.0', port=8080)
