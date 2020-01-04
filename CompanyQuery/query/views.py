from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from query import models
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

import pymysql

def LinkDatabase(): # 连接数据库
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'He981103',
        'database': 'Disclosure',
        'charset': 'utf8mb4',
    }
    conn = pymysql.connect(**config)
    return conn

@csrf_exempt
def index(request):
    conn = LinkDatabase()
    cursor = conn.cursor()

    # 查询个股总数
    NofStocks = "select count(distinct Stockcode) from Shareholder;"  # 注意：部分个股有持股信息没有个股基本信息
    cursor.execute(NofStocks)
    NS = cursor.fetchone()
    # 查询股东总数
    NofStockholders = "select count(distinct NameofShareholder) from Shareholder;"
    cursor.execute(NofStockholders)
    NSH = cursor.fetchone()
    cursor.close()
    conn.close()
    print(NS)

    res = {'company_num': NS, 'stock_num': NSH, 'status':True}
    # 以下为response消息头固定格式
    response = JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                               "Access-Control-Allow-Origin," \
                                               "X-Conten-Type-Options," \
                                               "Content-Type,Origin,Accept"
    response["Access-Control-Allow-Credentials"] = "true"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Type"] = "application/json; charset=UTF-8"
    return response

@csrf_exempt
def StockBasic(request):  #查询公司基本信息
    if request.method=="POST":
        conn = LinkDatabase()
        cursor = conn.cursor()

        d = json.loads(request.body.decode('utf-8'))
        S = d['info']
        M = int(d["query_type"])  # Method=1,2,3分别对应按照 公司名字、股票代码、股票简称 查询
        print (M,S)

        InfoSQL = ""

        if (M == 1):
            InfoSQL = "select * from Stock where FullnameofthecompanyinChinese = '" + S + "';"
        elif M == 2:
            InfoSQL = "select * from Stock where Stockcode = '\\'" + S + "';"
        elif M == 3:
            InfoSQL =  "select * from Stock where Sharesreferredtoas = '" + S + "';"

        print(InfoSQL)

        cursor.execute(InfoSQL)
        SInfo = cursor.fetchall()

        res = {'company_name': SInfo[0][3],'stock_name':SInfo[0][2],'location':SInfo[0][8],'CSRC1':SInfo[0][5],'GICS1':SInfo[0][6]}

        if not SInfo:
            res["status"] = False
            res["error"] = "抱歉，您所查询的公司/个股信息不存在！"
        else:
            res["status"] = True

            if M == 1:
                FSQL = "select Theannual,Totalassets,Netprofit,Operatingincome from Finance1 where Stockcode IN (select Stockcode from Stock where FullnameofthecompanyinChinese= '" + S + "');"
            elif M == 2:
                FSQL = "select Theannual,Totalassets,Netprofit,Operatingincome from Finance1 where Stockcode = '\\'" + S + "';"
            elif M == 3:
                FSQL = "select Theannual,Totalassets,Netprofit,Operatingincome from Finance1 where Stockcode IN (select Stockcode from Stock where Sharesreferredtoas = '" + S + "');"

            cursor.execute(FSQL)
            FInfo = cursor.fetchall()
            if FInfo:
                m = 7 # 仅取近4年的数据
                FI = FInfo[-m:]
                Totalassets = [];
                Netprofit = [];
                Operatingincome = [];
                years = [];
                for i in range(0, m):
                    years.append(FI[i][0])
                    Totalassets.append(FI[i][1])
                    Netprofit.append(FI[i][2])
                    Operatingincome.append(FI[i][3])
                res['Y']= years
                res['T'] = Totalassets
                res['N'] = Netprofit
                res['O'] = Operatingincome

            if M == 1:
                TransSQL = "select Theannual,Nameoftheaffiliatedpartyenterprise,Relatedpartycontrolrelationship,Transactionamountinvolved,Transactiontype from transact where Stockcode IN (select Stockcode from Stock where FullnameofthecompanyinChinese= '" + S + "');"
            elif M == 2:
                TransSQL = "select Theannual,Nameoftheaffiliatedpartyenterprise,Relatedpartycontrolrelationship,Transactionamountinvolved,Transactiontype from transact where Stockcode = '\\'" + S + "';"
            elif M == 3:
                TransSQL = "select Theannual,Nameoftheaffiliatedpartyenterprise,Relatedpartycontrolrelationship,Transactionamountinvolved,Transactiontype from transact where Stockcode IN (select Stockcode from Stock where Sharesreferredtoas = '" + S + "');"

            cursor.execute(TransSQL)
            Trans = cursor.fetchall()
            res["Trans"] = Trans[-m:]


        cursor.close()
        conn.close()
        print (res)


        # 以下为response消息头固定格式
    else:
        res = {}

    response = JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                               "Access-Control-Allow-Origin," \
                                               "X-Conten-Type-Options," \
                                               "Content-Type,Origin,Accept"
    response["Access-Control-Allow-Credentials"] = "true"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Type"] = "application/json; charset=UTF-8"
    return response

    return JsonResponse(res)

@csrf_exempt
def GetLawCase(request):  #得到涉案信息
    if request.method=="POST":
        conn = LinkDatabase()
        cursor = conn.cursor()

        d = json.loads(request.body.decode('utf-8'))
        conn = LinkDatabase()
        cursor = conn.cursor()

        S = d['info']
        M = int(d["query_type"])  # Method=1,2,3分别对应按照 公司名字、股票代码、股票简称 查询
        print (M, S)
        if M == 1:
            LCSQL = "select Theannouncementdate,Inthecaseoftype,Thecompanyspositioninthecase,Thecauseofaction,Theamountofmoneyinvolvedinthecase,Decisionsituation,Theimplementationof from LawCase where Stockcode IN (select Stockcode from Stock where FullnameofthecompanyinChinese= '" + S + "');"
        elif M == 2:
            LCSQL = "select Theannouncementdate,Inthecaseoftype,Thecompanyspositioninthecase,Thecauseofaction,Theamountofmoneyinvolvedinthecase,Decisionsituation,Theimplementationof from LawCase where Stockcode = '\\'" + S + "';"
        elif M == 3:
            LCSQL = "select Theannouncementdate,Inthecaseoftype,Thecompanyspositioninthecase,Thecauseofaction,Theamountofmoneyinvolvedinthecase,Decisionsituation,Theimplementationof from LawCase where Stockcode IN (select Stockcode from Stock where Sharesreferredtoas = '" + S + "');"

        cursor.execute(LCSQL)
        m = 6
        LCInfo = cursor.fetchall()[-m:]
        res = {}
        if LCInfo:
            res ['case']= LCInfo
            res['status'] = True
        else:
            res['status'] = False
            res['error']="no info get from database"

        # meetings
        if M == 1:
            CSQL = "select Theannual,Number0,Attendrate0,Number1,Attendrate1,Number2,Attendrate2 " \
                   "from Conference where Stockcode IN (select Stockcode from Stock where FullnameofthecompanyinChinese= '" + S + "');"
        elif M == 2:
            CSQL = "select Theannual,Number0,Attendrate0,Number1,Attendrate1,Number2,Attendrate2 " \
                   "from Conference where Stockcode = '\\'" + S + "';"
        elif M == 3:
            CSQL = "select Theannual,Number0,Attendrate0,Number1,Attendrate1,Number2,Attendrate2 " \
                   "from Conference where Stockcode IN (select Stockcode from Stock where Sharesreferredtoas = '" + S + "');"

        cursor.execute(CSQL)
        CInfo = cursor.fetchall()[-m:]
        cursor.close()
        conn.close()

        df = pd.DataFrame(list(CInfo), columns=["year", "num1", "rate1", "num2", "rate2", "num3", "rate3"])

        for col in df.columns:
            res[col] = df[col].tolist()

    else:
        res = {}

    print (res)

    response = JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                               "Access-Control-Allow-Origin," \
                                               "X-Conten-Type-Options," \
                                               "Content-Type,Origin,Accept"
    response["Access-Control-Allow-Credentials"] = "true"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Type"] = "application/json; charset=UTF-8"
    return response


@csrf_exempt
def Login(request):
    res = {}

    if request.method=="POST":
        conn = LinkDatabase()
        cursor = conn.cursor()

        d = json.loads(request.body.decode('utf-8'))
        conn = LinkDatabase()
        cursor = conn.cursor()


        UName = d["user_id"]
        Upassword = d["password"]

        getUserSQL = "select * from Users where UserName = '" + UName + "';"
        cursor.execute(getUserSQL)
        UInfo = cursor.fetchall()
        cursor.close()
        conn.close()
        if not UInfo:
            res['status'] = False
            res['error'] = '抱歉！此用户不存在！'
        else:
            if not UInfo[0][1] == Upassword:
                res['status'] = False
                res['error'] = '密码错误！'
            else:  # 用户存在且密码正确
                if UInfo[0][2] == 0:
                    res['status'] = False
                    res['error'] = '抱歉，您没有权限修改企业信息！'
                else:
                    res['status'] = True
                    res['UStockcode'] = UInfo[0][3]

    print (res)

    response = JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                               "Access-Control-Allow-Origin," \
                                               "X-Conten-Type-Options," \
                                               "Content-Type,Origin,Accept"
    response["Access-Control-Allow-Credentials"] = "true"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Type"] = "application/json; charset=UTF-8"
    return response

@csrf_exempt
def GetStock(request):  #查询公司基本信息

    if request.method=="POST":
        conn = LinkDatabase()
        cursor = conn.cursor()

        d = json.loads(request.body.decode('utf-8'))
        S = str(d['info'])
        M = int(d["query_type"])  # Method=1,2,3分别对应按照 公司名字、股票代码、股票简称 查询
        print (M,S)

        if M == 1:
            CV = "Create or replace view SpecialStock as select* from Shareholder where Stockcode =" \
                 " (select Stockcode from Stock where FullnameofthecompanyinChinese = '" + S + "') ;"
        elif M == 2:
            CV = "Create or replace view SpecialStock as select* from Shareholder where Stockcode = '\\'" + S + "' ;"
        elif M == 3:
            CV = "Create or replace view SpecialStock as select* from Shareholder where Stockcode =" \
                 " (select Stockcode from Stock where Sharesreferredtoas = '" + S + "') ;"
        SDetailSQL ="select Theannual,NameofShareholder,Shareholdratio from SpecialStock where NameofShareholder IN " \
             "(select S.NameofShareholder from (select NameofShareholder from SpecialStock group by NameofShareholder order by max(shareholdratio) desc limit 4)as S);";
        DV = "drop view SpecialStock;"

        cursor.execute(CV)
        re1 = cursor.fetchall()
        print ("re1: ", re1)
        cursor.execute(SDetailSQL)
        SDetail = cursor.fetchall()
        print ("sdetail: ",SDetail)
        cursor.execute(DV)

        cursor.close()
        conn.close()

        df = pd.DataFrame(list(SDetail), columns=["year", "company", "ratio"])
        dict = []
        num = 6
        name = []
        print (df)
        for i in range(0, 4):
            i = i * num
            df_1 = df['ratio'][i:(i + num)].tolist()
            name.append(df['company'][i])
            dict.append(df_1)
        res = {'year': df['year'][0:num].tolist(), 'name_1': dict[0], 'name_2': dict[1], 'name_3': dict[2],
               'name_4': dict[3], 'name_all': name}

    else:
        res = {}

    print (res)

    response = JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                               "Access-Control-Allow-Origin," \
                                               "X-Conten-Type-Options," \
                                               "Content-Type,Origin,Accept"
    response["Access-Control-Allow-Credentials"] = "true"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Type"] = "application/json; charset=UTF-8"
    return response

@csrf_exempt
def Modify(request):  #查询公司基本信息
    if request.method=="POST":
        conn = LinkDatabase()
        cursor = conn.cursor()
        res = {}
        d = json.loads(request.body.decode('utf-8'))
        UStockcode = d["company_id"] # 可以修改的企业股票代码
        C = int(d["attribute"] )# 需要修改的列：1公司名字 2股票简称 3证券交易所 4CSRC分类 5GICS分类;注意！C要是数字不能为字符
        NewValue = d["new_val"]  # 修改后的新值

        CNameList = ["FullnameofthecompanyinChinese", "Sharesreferredtoas", "Stockexchange",
                     "CSRCindustryclassification", "GICSindustryclassification"];
        CName = CNameList[C - 1]
        MSQL = "Update Stock set " + CName + " = '" + NewValue + "' where Stockcode = '\\" + UStockcode + "';"
        try:
            cursor.execute(MSQL)
            # 提交事务
            conn.commit()
        except Exception as e:
            # 有异常，回滚事务
            conn.rollback()
            res['status'] = False
            res['error'] = "修改失败，事务回滚"
        if not res:  # 如果res是空列表
            res['status'] = True

        cursor.close()
        conn.close()
    else:
        res = {}
    # 以下为response消息头固定格式
    response = JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                               "Access-Control-Allow-Origin," \
                                               "X-Conten-Type-Options," \
                                               "Content-Type,Origin,Accept"
    response["Access-Control-Allow-Credentials"] = "true"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Type"] = "application/json; charset=UTF-8"
    return response

@csrf_exempt
def Insert(request):
    if request.method == "POST":
        conn = LinkDatabase()
        cursor = conn.cursor()
        res = {}
        d = json.loads(request.body.decode('utf-8'))
        conn = LinkDatabase()
        cursor = conn.cursor()
    
        UStockcode = str(d["UStockcode"])  # 对应企业的股票代码,自动返回，无需用户手动输入
        AD = str(d["AnnouncementDate"] ) # 公告日期
        CType = str(d["CaseType"])  # 涉案类型
        CPosition = str(d["CompanyPosition"] ) # 公司在案件中的地位
        CCause = str(d["CaseCause"])  # 案由
        MIn = str(d["MoneyInvolved"])  # 涉及金额
        DS = str(d["DecisionSituation"] ) # 判决情况
        IS = str(d["ImplementSituation"] ) # 执行情况
    
        FindMAX = "select max(Caseno) from LawCase"
        cursor.execute(FindMAX)
        maxno = cursor.fetchone()  # 案件号自动取为 maxno[0] + 1
    
        InsertSQL = "Insert into LawCase Values(" + str( int(maxno[0]) + 1) + ",'\\" + UStockcode + "','" + AD + "','" + CType + "','" + CPosition + "','" + CCause + "','" + MIn + "','" + DS + "','" + IS + "',''); "
        try:
            cursor.execute(InsertSQL)
            # 提交事务
            conn.commit()
        except Exception as e:
            # 有异常，回滚事务
            conn.rollback()
            res['status'] = False
            res['error'] = "插入失败，事务回滚"
        if not res:  # 如果res是空列表
            res['status'] = True
    
        cursor.close()
        conn.close()
    else:
        res = {}
    response = JsonResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Methods,Access-Control-Allow-Credentials," \
                                               "Access-Control-Allow-Origin," \
                                               "X-Conten-Type-Options," \
                                               "Content-Type,Origin,Accept"
    response["Access-Control-Allow-Credentials"] = "true"
    response["X-Content-Type-Options"] = "nosniff"
    response["Content-Type"] = "application/json; charset=UTF-8"
    return response