import pymysql
import json


class OperateMysql(object):
    def __init__(self):
        # 数据库初始化连接
        self.connect_interface_testing = pymysql.connect(
            "localhost",
            "pig",
            "123456",
            "testdatabase",
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # 创建游标操作数据库
        self.cursor_interface_testing = self.connect_interface_testing.cursor()

    def select_first_data(self, sql):
        """
        查询第一条数据
        """
        try:
            # 执行 sql 语句
            self.cursor_interface_testing.execute(sql)
        except Exception as e:
            print("执行sql异常:%s" % e)
        else:
            # 获取查询到的第一条数据
            first_data = self.cursor_interface_testing.fetchone()
            # print(first_data)
            # 将返回结果转换成 str 数据格式，禁用acsii编码
            first_data = json.dumps(first_data, ensure_ascii=False)
            # self.connect_interface_testing.close()
            return first_data

    def select_all_data(self, sql):
        """
        查询结果集
        """
        try:
            self.cursor_interface_testing.execute(sql)
        except Exception as e:
            print("执行sql异常:%s" % e)
        else:
            first_data = self.cursor_interface_testing.fetchall()
            first_data = json.dumps(first_data, ensure_ascii=False)
            # self.connect_interface_testing.close()
            return first_data

    def del_data(self, sql):
        """
        删除数据
        """
        res = {}
        try:
            # 执行SQL语句
            result = self.cursor_interface_testing.execute(sql)
            # print(result)
            if result != 0:
                # 提交修改
                self.connect_interface_testing.commit()
                res = {'删除成功'}
            else:
                res = {'没有要删除的数据'}
        except:
            # 发生错误时回滚
            self.connect_interface_testing.rollback()
            res = {'删除失败'}
        return res

    def update_data(self, sql):
        """
        修改数据
        """
        try:
            self.cursor_interface_testing.execute(sql)
            self.connect_interface_testing.commit()
            res = {'更新成功'}
        except Exception as e:
            self.connect_interface_testing.rollback()
            res = {'更新删除'}
        return res

    def insert_data(self, sql, data):
        """
        新增数据
        """

        try:
            self.cursor_interface_testing.execute(sql, data)
            self.connect_interface_testing.commit()
            res = {data, '新增成功'}
        except Exception as e:
            res = {'新增失败', e}
        return res

    def conn_close(self):
        # 关闭数据库
        self.cursor_interface_testing.close()