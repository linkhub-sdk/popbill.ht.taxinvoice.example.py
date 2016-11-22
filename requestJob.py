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

'''
전자(세금)계산서 매출/매입 내역 수집을 요청합니다
- 매출/매입 연계 프로세스는 "[홈택스 전자(세금)계산서 연계 API 연동매뉴얼]
  > 1.2. 프로세스 흐름도" 를 참고하시기 바랍니다.
- 수집 요청후 반환받은 작업아이디(JobID)의 유효시간은 1시간 입니다.
'''

try:
    print("=" * 15 + " 수집 요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 전자세금계산서  발행유형, SELL-매출, BUY-매입, TRUSTEE-위수탁
    Type = "SELL"

    # 일자유형, W-작성일자, I-발행일자, S-전송일자
    DType = "W"

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20161001"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20161131"

    jobID = htTaxinvoiceService.requestJob(CorpNum, Type, DType, SDate, EDate, UserID)

    print("작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
