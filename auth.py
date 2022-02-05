import subprocess
import mysql.connector


db = mysql.connector.connect(user=None, password=None,
                              host=None,
                              database=None, port=None)

cursor = db.cursor()

def gethwid():
    HWID = subprocess.check_output("wmic csproduct get uuid").decode().split("\n")[1].strip()
    return HWID
    

def check():
    try:
        cursor.execute(f"""SELECT HWID FROM UserData WHERE HWID = {gethwid()}""")
        
        if cursor.fetchall():
            print("In database")
    except Exception as e:
        print(e)
    


if __name__ == "__main__":
    check()