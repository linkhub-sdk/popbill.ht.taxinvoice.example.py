# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 수집 요청 " + "=" * 15)
    print("* 작업아이디의 유효시간은 1시간 입니다.")

    # 전자세금계산서 유형, SELL-매출, BUY-매입, TRUSTEE-위수탁
    Type = "SELL"

    # 일자유형, W-작성일자, I-발행일자, S-전송일자
    DType = "W"

    # 시작일자, 표시형식(yyyyMMdd)
    SDate = "20160601"

    # 종료일자, 표시형식(yyyyMMdd)
    EDate = "20160831"

    jobID = htTaxinvoiceService.requestJob(testValue.testCorpNum, Type, DType, SDate, EDate, testValue.testUserID)

    print( "작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
