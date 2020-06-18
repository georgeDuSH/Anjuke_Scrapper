import pymysql   
import pandas as pd
from sql import *

host = "localhost"
user = "root"
password = "123"
database = "py_database_anjuke"

class mydb():
    def __init__(self, host, user, pwd, database):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.database = database
        self.db = None
        self.curs = None
    
    # 最基础、核心、频繁的功能，每一次的增删改都会对数据库进行链接，随后会关闭，即下一个函数
    def connect(self):
        # 初始化链接
        self.db = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.pwd,
            database = self.database
        )
        # 设置游标中的数据返回类型设置为字典
        self.curs = self.db.cursor(pymysql.cursors.DictCursor)

    # 关闭游标和数据库的进程
    def close(self):
        self.curs.close()
        self.db.close()

    # 数据查询，如果成功会返回一个字典类型的记录
    def query(self, sql):
        """每一次的查询都是【链接】-【查询】-【关闭】的流程，因此这里也这样安排"""
        self.connect()
        # Excecuting the sql command, if there is an error, then raise error and rollback
        try:
            # todo: excecute sql query & return the results if there is a value
            self.curs.execute(sql)
            self.db.commit()
            q_result = self.curs.fetchall()
            print("Query Success")
            return q_result
        except:
            # todo: rollback incase something unexpected might happen, and raise exceptional error
            self.db.rollback()
            print('Query Process Error')
        finally:
            # todo: close the data base
            self.close()
    
    # 完成增删改的功能
    def update(self, sql):
        """这里的功能是实现不需要传参的【增】、【删】、【改】，因为不需要返回数据，所以直接执行sql语句就好了"""
        self.connect()
        try:
            # todo: excecute sql query
            print(sql)
            self.curs.execute(sql)
            self.db.commit()
            print("Success")
        except:
            # todo: rollback incase something unexpected might happen, and raise exceptional error
            self.db.rollback()
            print('Updating Process Error')

    # 删除既有的表单和数据的方法，并调用 sql.py 中的初始化代码，对数据库进行初始化，建立空表来为后续数据填充提供骨架
    def anjuke_data_initialize(self):
        ################################################
         ########这里导入初始数据，随后加入数据表中########
        ################################################

        ini_set = ['house', 'community']
        sql_del = "drop table if exists `{0}`;"

        # 建立连接，先将原有表单删除，随后进行相关表插入操作：
        ################################################
        ##################删除原有表单###################
        ################################################
        self.connect()
        for item in ini_set:
            try:
                # 删除数据表
                self.curs.execute(sql_del.format(item))
                self.db.commit()
                print('Clear Table '+item+' Success')
            except:
                # 出现问题则返回报错
                self.db.rollback()
                print('Clear Table '+item+' Failed')
        
        ################################################
        #####################表建立#####################
        ################################################
        # 函数3：执行sql语句进行数据表创建，并将pandas.DataFrame中的每一条数据记录用过sql语句存储在数据库中
        def create_table(sql_create_table='', name=''):
            try:
                # todo: 建立数据表（空）
                self.curs.execute(sql_create_table)
            except:
                # todo: rollback 并报错
                self.db.rollback()
                print('Initializing {0} Error'.format(name))

        #### ~community~ #### 首先建立这个表单，是因为community和小区之间存在外键依附关系
        create_table(sql_create_table=sql_create_community, name='community')
        
        #### ~house~ #### 建立完community之后就可以去建立house表单了
        create_table(sql_create_table=sql_create_house, name='hosuse')
        print('Initialize Success')
    
    def insert(self, table_name_indb, pd_table):
        # 首先，要把传入的数据变成sql能够处理的形式，比如传入pd.DataFrame之后，将列表型：
        #   ['翔顺公寓', '暂无', nan, '1.8', nan, '25%', '0.60元/m²'] 转化为字符串：
        #   '"翔顺公寓", "暂无", "nan", "1.8", "nan", "25%", "0.60元/m²"'
        # 这样一来就可以将数据放在SQL语句中进行执行插入了；

        # 函数1：建立数据库的时候将所有数值加上引号
        def quotation(item):
            return '"'+str(item)+'"'

        # 函数2：将pd中的数据格式化成所需要的形式
        def get_insert_value(df):
            lst = []
            for idx in list(df.index):
                value_set = [quotation(item) for item in df.iloc[idx].values]
                lst.append(", ".join(value_set))
            return lst 

        sql_insert = "insert into {0} values ({1});"
        
        insert_sql_cmd_lst = [sql_insert.format(table_name_indb, item) for item in get_insert_value(pd_table)]

        # print(insert_sql_cmd_lst[0])

        for item_sql in insert_sql_cmd_lst:
            try:
                # print(item_sql)
                self.curs.execute(item_sql)
                self.db.commit()
            except:
                print(item_sql)
                self.db.rollback()
                print('Initializing {0} Error'.format(table_name_indb))
                break
            
        print('Finish Initialize {0}'.format(table_name_indb))

    
db = mydb(host, user, password, database)
# db.anjuke_data_initialize() # 用来初始化数据库的表单信息

# comm = pd.read_csv('C:/Users/Dushenghui/Desktop/2017111136 杜圣辉/codes/crawl-preprocess-storage/01 Anjuke Crawler/input/comm_table.csv')
# house = pd.read_csv('C:/Users/Dushenghui/Desktop/2017111136 杜圣辉/codes/crawl-preprocess-storage/01 Anjuke Crawler/input/house_table.csv')

# db.insert(table_name_indb='COMMUNITY', pd_table=comm)
# db.insert(table_name_indb='HOUSE', pd_table=house)


# 用DBAPI构建数据库链接engine
# db.connect()
# df = pd.read_sql(sql_query_house, db.db)

# db.connect()
# df = pd.read_sql(sql_query_community, db.db)
# print(df.shape)
# print(df)
