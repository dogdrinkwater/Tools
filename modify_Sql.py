# -*- coding:utf-8 -*-
import pymysql


class updateSQL:
    # 打开数据库连接
    db_mysql = pymysql.connect(host='10.33.85.236',
                               port=3306,
                               user='wftest',
                               passwd='8eCGWcqp8pk0h22F',
                               db='uic')
    db_mycat = pymysql.connect(host='10.33.85.236',
                               port=8066,
                               user='dev',
                               passwd='dev@2019',
                               db='mycatuic')

    def modifyGroup(userId):  # 修改用户分组
        # 使用 cursor() 方法创建一个游标对象cur
        cur = updateSQL.db_mysql.cursor()
        # 使用 execute()  方法执行 SQL 查询
        group = input("输入用户分组（9：黑名单/10:白名单/11:灰名单）：")
        while (group != '9') & (group != '10') & (group != '11'):
            print("输入有误！")
            group = input("输入用户分组（9：黑名单/10:白名单/11:灰名单）：")
        cur.execute("select group_type_id,group_type_parent_id from uic.uic_group where user_id=%s" % userId)
        # 使用 fetchall() 方法获取查询结果
        data = cur.fetchone()

        # 如果表里查询不到该userId的数据，新增一条
        if data is None:
            sql = "INSERT INTO uic.uic_group (id, user_id, user_data, group_type_id,\
             group_type_parent_id, operation_username, create_time, update_time, delete_flag)\
              SELECT max(id)+1, %s, NULL, %s, '8', NULL, now(), now(), '0'\
              from uic.uic_group" % (userId, group)
            cur.execute(sql)

        else:
            sql = "UPDATE uic.uic_group SET group_type_id = %s WHERE user_id=%s" % (group, userId)
            cur.execute(sql)
        # print(data)  # 取出对应的psw值
        cur.close()
        updateSQL.db_mysql.commit()
        # 关闭数据库连接
        updateSQL.db_mysql.close()
        print('sql执行成功')

    def modifyState(userId):  # 修改用户创建时间
        # 使用 cursor() 方法创建一个游标对象cur
        cur = updateSQL.db_mycat.cursor()
        state = input("输入切换新/老（0：新用户/1:老用户）：")
        while (state != '0') & (state != '1'):
            print("输入有误！")
            state = input("输入切换新/老（0：新用户/1:老用户）：")
        if state == '0':  # 修改时间为当前时间
            # 使用 execute()  方法执行 SQL 查询
            cur.execute("UPDATE mycatuic.uic_user SET \
            create_time= now() WHERE id=%s" % userId)
            print("切换成新用户")
        else:  # 修改时间为创建时间-8天
            cur.execute("UPDATE mycatuic.uic_user SET \
            create_time= date_add(create_time,interval -8 day) WHERE id=%s" % userId)
            print("切换成老用户")
        # print(data)  # 取出对应的psw值
        cur.close()
        updateSQL.db_mycat.commit()
        # 关闭数据库连接
        updateSQL.db_mycat.close()
        print('sql执行成功')
