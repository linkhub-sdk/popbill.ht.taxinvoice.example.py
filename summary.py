# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService,PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + "수집결과 요약정보 조회 " + "=" * 15)
    '''
        수집 결과에 대한 요약정보를 반환합니다.
        count : 결과건수
        supplyCostTotal : 공급가액 합계
        taxTotal : 세액 합계
        amountTotal : 합계 금액
    '''


    # 수집 요청(requestJob)시 발급받은 작업아이디
    JobID = "016080110000000007"

    # 문서형태 배열, N-일반전자세금계산서, M-수정전자세금계산서
    Type = ["N", "M"]

    # 과세형태, T-과세, N-면세, Z-영세
    TaxType = ["T", "N", "Z"]

    # 영수/청구, R-영수, C-청구, N-없음
    PurposeType = ["R", "C", "N"]

    # 종사업장번호 사업자유형, S-공급자, B-공급받는자, T-수탁자
    TaxRegIDType = "S"

    # 종사업장번호 유무,,공백 - 전체조회, 0- 종사업장번호 없음, 1-종사업장번호 있음
    TaxRegIDYN = ""

    # 종사업장번호, 콤마(",")로 구분하여 구성 Ex) "0001,0007"
    TaxRegID = ""

    response = htTaxinvoiceService.summary(testValue.testCorpNum, JobID, Type, TaxType, PurposeType, TaxRegIDType, TaxRegIDYN, TaxRegID, testValue.testUserID)

    print("count (수집결과 건수) : %s " % response.count)
    print("supplyCostTotal (공급가액 합계) : %s " % response.supplyCostTotal)
    print("taxTotal (세액 합계) : %s " % response.taxTotal)
    print("amountTotal (합계 금액) : %s " % response.amountTotal)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))