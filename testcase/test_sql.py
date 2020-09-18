import json
import unittest
from common.opreatemysql import OperateMysql

class testmysql(unittest.TestCase):


    def testmysql(self):
        conn=OperateMysql()

        # data = [{'id': 1, 'name': '测试', 'age': 15}, {'id': 2, 'name': '老王', 'age': 10}, {'id': 3, 'name': '李四', 'age': 20}]
        # for i in data:
        #     i_data = (i['id'], i['name'], i['age'])
        #     insert_res = conn.insert_data(
        #         """
        #          INSERT INTO runoob_tbl (id,name,age) VALUES (%s,%s,%s)
        #         """, i_data
        #     )
        #     print(insert_res)

        # 查询
        one_data = conn.select_first_data(
            """
                SELECT name FROM runoob_tbl;
            """
        )
        all_data = conn.select_all_data(
            """
            SELECT * FROM runoob_tbl;
            """
        )
        print(one_data)
        # all_data字符串类型的list转list
        print("查询总数据:", len(json.loads(all_data)), "分别是:", all_data)

        # 修改
        # update_data = conn.update_data(
        #     """
        #     UPDATE runoob_tbl SET name = '王五' WHERE id = 1;
        #     """
        # )
        # print(update_data)
        #
        # # 删除
        # del_data = conn.del_data(
        #     """
        #     DELETE FROM runoob_tbl WHERE id in (1,2,3);
        #     """
        # )
        # print(del_data)

        conn.conn_close()


