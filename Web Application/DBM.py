import pymysql as p

def getconnect():
	return p.connect(user="root",password="",host="localhost",database="flaskproject")

def getlogindata():
	db = getconnect()
	cr = db.cursor()

	sql = "select uname,password from users"
	cr.execute(sql)

	data=cr.fetchall()
	print(data) 

	db.commit()
	db.close()
	return data
 
def insertdata(t):
    db=getconnect()
    cr = db.cursor()

    sql = "insert into users values(%s,%s,%s,%s,%s)"
    cr.execute(sql,t)
    print("Data insert successfully")

    db.commit()
    db.close()

def getdata():
	db = getconnect()
	cr = db.cursor()

	sql = "select * from users"
	cr.execute(sql)

	data=cr.fetchall()

	db.commit()
	db.close()
	return data

def getdatabyid(ids):
	db = getconnect()
	cr = db.cursor()

	sql = "select * from users where id=%s"
	cr.execute(sql,ids)
	data=cr.fetchall()

	db.commit()
	db.close()
	return data[0]


def updatedata(t):
	db = getconnect()
	cr = db.cursor()

	sql = "update users set name=%s,uname=%s,password=%s,gmail=%s where id=%s"
	cr.execute(sql,t)

	db.commit()
	db.close()
	print(t)


def deletedata(t):
	db = getconnect()
	cr = db.cursor()

	sql = "delete from users where id=%s"
	cr.execute(sql,t)

	db.commit()
	db.close()
	print(t)

def studentdetails(b):
    db = getconnect()
    cr = db.cursor()

    sql = "insert into student values(%s,%s,%s,%s,%s,%s)"
    cr.execute(sql,b)
    print("data insert successfully")

    db.commit()
    db.close()
	
def showstudentdata():
    db = getconnect()
    cr = db.cursor()

    sql = "select * from student"
    cr.execute(sql)
    data = cr.fetchall()

    db.commit()
    db.close()
    return data


def studentdatabyid(ids):
    db = getconnect()
    cr = db.cursor()

    sql = "select * from student where id =%s"
    cr.execute(sql,ids)
    data = cr.fetchall()

    db.commit()
    db.close()
    return data[0]

def updatestudent(t):
    db = getconnect()
    cr = db.cursor()

    sql = "update student set f_name=%s,l_name=%s,gmail=%s,course=%s,payment=%s where id=%s"
    cr.execute(sql,t)

    db.commit()
    db.close()
    print(t)

