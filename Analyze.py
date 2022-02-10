import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
import re

class Market:
    def __init__(self):
        """생성자: DB연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', passwd='ghost@0@', db='invest', charset='utf8')
        self.codes = {}
        self.get_comp_info()

    def __del__(self):
        """MariaDB 연결해제"""
        self.conn.close()

    def get_company_info(self):
        """codes에 company_info 읽어와서 저장"""
        sql = "SELECT * FROM company_info"
        krx = pd.read_sql(sql, self.conn)

        for idx in range(len(krx)):
            self.codes[krx['code'].values[idx] = krx['company'].values[idx]

    def get_daily_price(self, code, start_date=None, end_date=None):
            