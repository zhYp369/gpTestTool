#!/usr/bin/env python
# coding=utf-8


import time
import pymysql


class OperationMysql(object):

	def __init__(self, dict_peizhi):
		self.conn = pymysql.connect(
			host=dict_peizhi.get("host"),
			port=dict_peizhi.get("port"),
			user=dict_peizhi.get("user"),
			passwd=dict_peizhi.get("passwd"),
			db=dict_peizhi.get("db"),
			charset=dict_peizhi.get("charset"),
			cursorclass=pymysql.cursors.DictCursor,
			)
		self.cur = self.conn.cursor()

	# 查询一条数据
	def select(self, sql):
		self.cur.execute(sql)
		result = self.cur.fetchall()
		# result = json.dumps(result)
		return result

	# 写入
	def insert(self, sql):
		param = ("aaa", int(time.time()))
		self.conn.commit()
		n = self.cur.execute(sql, param)
		print (n)

	# 更新
	def update(self, sql):
		n = self.cur.execute(sql)
		self.conn.commit()
		print(n)

	# 删除
	def delete(self, sql):
		param = ("aaa")
		n = self.cur.execute(sql, param)
		self.conn.commit()
		print(n)

	# 关闭
	def __exit__(self):
		self.conn.close()


if __name__ == '__main__':
	dict1 = {'host': '172.25.2.24', 'port': 3306, 'user': 'root', 'passwd': '', 'db': 'fpsyy', 'charset': 'utf8', 'cursorclass': 'MySQLdb.cursors.DictCursor'}
	op_mysql = OperationMysql(dict1)
	res = op_mysql.select("SELECT dk.kp_sts FROM `ent_order` d, `ent_order_dkp` dk  WHERE d.od_lsh=dk.od_lsh AND d.od_no = '22_1901171007590'")
	print(res)
