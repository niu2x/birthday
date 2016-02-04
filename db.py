# -*- coding:utf8 -*-
import MySQLdb

# @app.route(u'/英雄榜')
# def hero_list():
#     ret0 = ((u'称号', u'昵称', u'发帖总数'), [])
#     try:
#         db = None
#         cursor = None
#         db = connect_db()
#         cursor = db.cursor()
#         sql = "select * from num_of_words_per_user limit 10";
#         cursor.execute(sql)
#         for row in cursor:
#             ret0[1].append((u'称号', row[0], row[1]))
#         db.commit()
#         cursor.close()
#         db.close()
#         return render_template('hero_list.html', state='ok', ret0 = ret0)
#     except mysql.connector.Error, e:
#         if cursor:
#             cursor.close()
#         if db:
#             db.close()
#         return render_template('hero_list.html', state='error')
#     return 'This website Work.'

def connect_db():
    config = {
        'db':'birthday', 
        'charset':'utf8', 
        'host':'127.0.0.1', 
        'user':'root', 
        'passwd':'wolf0355wolf', 
        'port':3306
    }
    return MySQLdb.connect(**config)

def execute(sql):
    try:
        db = None
        cursor = None
        db = connect_db()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return True
    except MySQLdb.Error, e:
        if cursor:
            cursor.close()
        if db:
            db.close()
        return False

def select(sql, callback):
    try:
        db = None
        cursor = None
        db = connect_db()
        cursor = db.cursor()
        cursor.execute(sql)
        if callback:
            for item in cursor:
                callback(item)
        cursor.close()
        db.close()
        return True
    except MySQLdb.Error, e:
        if cursor:
            cursor.close()
        if db:
            db.close()
        return False

import sys
if __name__ == '__main__':
    select(
        'select name, sex, birthday, calendar, mail from person',
        lambda item:sys.stdout.write(repr(item)+'\n')
    )
