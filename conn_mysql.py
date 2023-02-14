import pymysql

# 打开数据库连接
db = pymysql.connect("www.baidu.com","admin","","echsop",port=3306,charset='utf-8')

cursor = db.cursor()
# 查询语句
query_sql='''SELECT password from espcms_user where user_name = admin'''
# 创建数据库表
add_sql='''CREATE TABLE Employee (Id CHAR(20) NOT NULL,Name CHAR(20),Age INT,SEX CHAR(1),Salary FLOAT)'''
# 删除数据库表
del_sql='''DROP TABLE Employee'''
# 更新数据库数据
update_sql='''UPDATE Employee SET Age=21,SEX=1 WHERE Name=admin'''

try:
    cursor.execute(query_sql)
    result = cursor.fetchall()
    if not result:
        print("数据为空！")
    else:
        for row in result:
            user_id = row[0]
            user_name = row[1]
            email = row[2]
            password = row[3]
            ec_salt = row[4]
            # 打印结果
            print("user_id:{0}用户名：{1}电子邮箱：{2}密码：{3}盐值：{4}".format(user_id,user_name,email,password,ec_salt))
            # 输出结果格式：1 用户名：admin 电子邮箱：##########密码：#######盐值：#########
except Exception as e:
# 错误回滚
    db.rollback()
    print("Error!:{0}".format(e))
finally:
    db.close()
