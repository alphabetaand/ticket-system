from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def home(): return "Syst�me de tickets en marche!" 
if __name__ == "__main__": app.run() 
