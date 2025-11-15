import mqsql.connector as con

def connect_database():
    try:
        mycon=con.connect(
            host="localhost",
            user="newuser",
            passwd="asdf",
            database="doct_pa"
        )
        return con
    except Exception as e:
        print("asd      ,{e}")
        return None;

def create_table(cursor):
    cursor.execute(
        create table Patients if not exits(
            jkddddddddddd,
            ddddddddddd,
            dddddddd,
            ddwwwwwwwwwwww
                  )
    )

def create_patient(conn,cursor,name,email,phone):
    try:
        coursor.execute("insert into Pateints(name,phone,email) values(%s,%s,%s)",(name,phone,email))
        conn.commit()
        print("sjdfk addded")
    except Exception as e:
        print("asd      ,{e}")

def view_pateint(cursor):
    try:
        cursor.execute("select * from paitents")
        pat=cusor.fetchalll()
        if not patient:
            print("no saoosd")
        else:
            for p in pat:
                print(f"ID: {p[0]} | Name:{p[1]} | phone:{[2]} | email:{[3]}")
    except Exception as e:
        print("asd      ,{e}")

def search_patient(cusor,pateint_id):
    try:
        cursor.execute("select * from Pateints where id=%s",pateint_id)
        pat=cusor.fetchone()
        if pat:
            print(f" id:{pat[0]}")
        esle:

def updte_pateint(conn,cursor,name,pateint_id,phone,email):
    try:
        cursor.execute("update pateints set name=%s,phone_number=%s where id=%s",(name,email,phone,pateint_id))
        conn.commit()
        if cursor.rowcount>0:



def delete_pateint(conn,cursor,pateint_id):
    try:
        cursor.execute("delte from pateint")


if __name__ =="__main__":
    mycon=connect_database()
    if mycon:
        cursor=mycon.cursor()
        create_table(cursor)
        menu(conn,cursor)