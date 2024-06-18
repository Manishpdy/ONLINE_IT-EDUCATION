from flask import *
from DBM import *

app = Flask(__name__)

@app.route("/")                          #It is used for Page view
def page():
	return render_template("Login_page.html")


@app.route("/signup")                    #It is used for Page view
def page3():
	return render_template("Signup_page.html")


@app.route("/index")                         #It is used for Page view
def page4():
	return render_template("home_page.html")


@app.route("/users")                      #It is used for Page view
def page5():
	table = getdata()
	return render_template("User_page.html" , data =table)


@app.route("/updateuser/<int:ids>")       #It is used for Page view
def page6(ids):
	table = getdatabyid(ids)
	return render_template("Update_page.html" , data=table)


@app.route("/deleteuser/<int:ids>")        #It is used for Page view
def page8(ids): 
	deletedata(ids)
	return redirect("/users")


@app.route("/student")                   #It is used for Page view
def page9():
	return render_template("Student.html")


@app.route("/AllStudent")                      #It is used for Page view
def page11():
	table = showstudentdata()
	return render_template("AllStudent.html" , data =table)


@app.route("/change/<int:ids>")       #It is used for Page view
def page12(ids):
	table = studentdatabyid(ids)
	return render_template("Update_student.html" , data=table)



@app.route("/updatstudentrec" ,methods=["POST"])      #It is worked on action which are on page
def page13():
	ids = request.form["ids"]
	name = request.form["fname"]
	lname = request.form["lname"]
	gmail = request.form["mail"]
	sub = request.form["course"]
	pay = request.form["payment"]

	d=[name, lname, gmail, sub, pay, ids]

	updatestudent(d)
	return redirect("/AllStudent")



@app.route("/Student_details", methods=["POST"])              #It is worked on action which are on page
def page10():
	ids = request.form["ids"]
	name = request.form["fname"]
	lname = request.form["lname"]
	gmail = request.form["mail"]
	sub = request.form["Course"]
	pay = request.form["payment"]

	d=[ids, name, lname, gmail, sub, pay]

	database = studentdetails(d)
	print(d)
	return redirect("/index")



@app.route("/updaterec" ,methods=["POST"])      #It is worked on action which are on page
def page7():
	ids = request.form["ids"]
	name = request.form["name"]
	uname = request.form["uname"]
	pin = request.form["pin"]
	gmail= request.form["mail"]

	d = (name, uname, pin, gmail,ids)
	updatedata(d)
	return redirect("/users")



@app.route("/Insert_data",methods=["POST"])      # It is worked on action which are on page
def page1():
	ids = request.form["ids"]
	name = request.form["name"]
	uname = request.form["uname"]
	pin = request.form["pin"]
	gmail= request.form["mail"]

	d=[ids, name, uname, pin, gmail]

	database = insertdata(d)
	print(d)
	return redirect("/")

	

@app.route("/validate",methods=["POST"])      # It is worked on action which are on page
def page2():
	uname = request.form["uname"]
	pin = request.form["pin"]

	d = (uname,pin)
	database = getlogindata()

	if d in database:
		return render_template("home_page.html")

	else:
		return redirect("/")



if __name__=='__main__':
	app.run(debug=True)
