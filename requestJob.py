# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest
htTaxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
htTaxinvoiceService.UseStaticIP = testValue.UseStaticIP
htTaxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
홈택스에 신고된 전자세금계산서 매입/매출 내역 수집을 팝빌에 요청합니다. (조회기간 단위 : 최대 3개월)
- 주기적으로 자체 DB에 세금계산서 정보를 INSERT 하는 경우, 조회할 일자 유형(DType) 값을 "S"로 하는 것을 권장합니다.
- https://developers.popbill.com/reference/httaxinvoice/python/api/job#RequestJob
"""

try:
    print("=" * 15 + " 수집 요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 전자세금계산서  발행유형, SELL-매출, BUY-매입, TRUSTEE-위수탁
    Type = "SELL"

    # 일자유형, W-작성일자, I-발행일자, S-전송일자
    DType = "S"

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20250801"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20250831"

    jobID = htTaxinvoiceService.requestJob(CorpNum, Type, DType, SDate, EDate)

    print("작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
