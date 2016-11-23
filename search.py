# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService,PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

'''
검색조건을 사용하여 수집결과를 조회합니다.
- 응답항목에 관한 정보는 "[홈택스 전자(세금)계산서 연계 API 연동매뉴얼]
  > 3.3.1. Search (수집 결과 조회)" 을 참고하시기 바랍니다.
'''

try:
    print("=" * 15 + " 수집 결과 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "016112315000000001"

    # 문서형태 배열, N-일반전자세금계산서, M-수정전자세금계산서
    Type = ["N", "M"]

    # 과세형태 배열, T-과세, N-면세, Z-영세
    TaxType = ["T", "N", "Z"]

    # 영수/청구, R-영수, C-청구, N-없음
    PurposeType = ["R", "C", "N"]

    # 종사업자번호 사업자 유형, S-꽁급자, B-공급받는자, T-수탁자
    TaxRegIDType = "S"

    # 종사업장번호 유무, 공백-전체조회, 0-종사업장번호 없음, 1-종사업장번호 있음
    TaxRegIDYN = ""

    # 종사업장번호, 콤마(",")로 구분하여 구성 ex) "0001", "0007"
    TaxRegID = ""

    # 페이지번호
    Page = 1

    # 페이지당 목록개수, 최대값 1000
    PerPage = 10

    # 정렬방향 D-내림차순, A-오름차순
    Order = "D"

    response = htTaxinvoiceService.search(CorpNum, JobID, Type, TaxType, PurposeType,
        TaxRegIDType, TaxRegIDYN, TaxRegID, Page, PerPage, Order, UserID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    i = 1
    for info in response.list :
        print("====== 세금계산서 정보 [%d] ======"% i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print("")


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
