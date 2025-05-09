from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def home(): return "Systäme de tickets en marche!" 
if __name__ == "__main__": app.run() 
