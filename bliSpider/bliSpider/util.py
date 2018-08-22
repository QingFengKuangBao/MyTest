
import pymysql
import logging
from bliSpider import setting as se

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -%(threadName)s %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

class db_utils():


    def  connect(self):
        return pymysql.connect(**se.db_config)

    def sql_executemany(self,sql,data=None):
        result=None
        db=self.connect()
        cursor=db.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 执行sql语句
            cursor.executemany(sql,data)
            db.commit()
            result=cursor.fetchall()
        except:
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()
        return result

    def sql_execute(self,sql,data=None):
        result=None
        db=self.connect()
        cursor=db.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 执行sql语句
            cursor.execute(sql,data)
            db.commit()
            result=cursor.fetchall()
        except:
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()
        return result


sql_util=db_utils()

