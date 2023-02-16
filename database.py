import json

def read_file(f):
  fi = open(f, "r")
  return fi.read()

def add_user(n,e,p):
  content = read_file("users.json")
  d = json.loads(content)
  try:
    print(d["users"][e])
    return 1
  except:
    d["users"][e] = {
      "name": n,
      "password": p
    }
  f = open("users.json", "w")
  f.write(json.dumps(d))
  return 0

def get_id():
  content = read_file("users.json")
  d = json.loads(content)
  return d["current_id"]