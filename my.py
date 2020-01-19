from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)
dl=[]
@app.route("/")
def form():
    return render_template("shopB.html")
@app.route("/result",methods=["POST","GET"])
def result():
    if request.method == 'POST':
        search=request.form["product_name"]
        db=MySQLdb.connect("localhost","root","Goodluck","productdetails")
        cur=db.cursor()
        query="select product_name from inventory"
        cur.execute(query)
        m=cur.fetchall()
        dl=m
        print(dl)
        cur.close()
        return render_template("result.html" ,m=m)

        #return render_template("result.html" ,name=search)
#@app.route("/addtocart",methods=["POST","GET"]
#def addtocart():
    
    
    
if __name__=="__main__":
    app.run(debug=True)
