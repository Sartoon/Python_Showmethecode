import mysql.connector

config={'host':'127.0.0.1',#默认127.0.0.1
        'user':'root',
        'password':'123456',
        'port':2048 ,
        'database':'showmethecode',
        'charset':'utf8'#默认即为utf8
        }

  
def store_mysql(filepath):
    conn=mysql.connector.connect(**config)
    cursor=conn.cursor()

    #判断表是否已经存在
    cursor.execute('show tables in showmethecode;')
    tables=cursor.fetchall()
    findtables=False
    for table in tables:
        if 'Needcode' in table:
            findtables=True
            print('findtables:'+findtables)
    if not findtables:
        cursor.execute('''
                CREATE TABLE `showmethecode`.`Needcode` (
                `Cid` INT NOT NULL AUTO_INCREMENT,
                `Fixcode` VARCHAR(10) NOT NULL,
                PRIMARY KEY (`Cid`));
        ''')

    f=open(filepath,'rb')
    for line in f.readlines():
        code=line.strip()
        cursor.execute("insert into showmethecode")

    conn.comnit()
    cursor.close()
    conn.close()
    


if __name__=='__main__':
    store_mysql('Activation_code.txt');
