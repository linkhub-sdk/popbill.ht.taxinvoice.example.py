# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest
htTaxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
htTaxinvoiceService.UseStaticIP = testValue.UseStaticIP
htTaxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
검색조건을 사용하여 수집 결과 요약정보를 조회합니다.
- https://docs.popbill.com/httaxinvoice/python/api#Summary
'''

try:
    print("=" * 15 + "수집 결과 요약정보 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집 요청(requestJob)시 발급받은 작업아이디
    JobID = "022080216000000005"

    # 문서형태 배열 ("N" 와 "M" 중 선택, 다중 선택 가능)
    # └ N = 일반 , M = 수정
    # - 미입력 시 전체조회
    Type = ["N", "M"]

    # 과세형태 배열 ("T" , "N" , "Z" 중 선택, 다중 선택 가능)
    # └ T = 과세, N = 면세, Z = 영세
    # - 미입력 시 전체조회
    TaxType = ["T", "N", "Z"]

    # 발행목적 배열 ("R" , "C", "N" 중 선택, 다중 선택 가능)
    # └ R = 영수, C = 청구, N = 없음
    # - 미입력 시 전체조회
    PurposeType = ["R", "C", "N"]

    # 종사업장번호 유무 (null , "0" , "1" 중 택 1)
    # - null = 전체 , 0 = 없음, 1 = 있음
    TaxRegIDYN = ""

    # 종사업장번호의 주체 ("S" , "B" , "T" 중 택 1)
    # └ S = 공급자 , B = 공급받는자 , T = 수탁자
    # - 미입력시 전체조회
    TaxRegIDType = "S"

    # 종사업장번호
    # 다수기재시 콤마(",")로 구분하여 구성 ex ) "0001,0002"
    # - 미입력시 전체조회
    TaxRegID = ""

    # 거래처 상호 / 사업자번호 (사업자) / 주민등록번호 (개인) / "9999999999999" (외국인) 중 검색하고자 하는 정보 입력
    # - 사업자번호 / 주민등록번호는 하이픈('-')을 제외한 숫자만 입력
    # - 미입력시 전체조회
    SearchString = ""

    response = htTaxinvoiceService.summary(CorpNum, JobID, Type, TaxType, PurposeType,
                                           TaxRegIDType, TaxRegIDYN, TaxRegID, UserID, SearchString)

    print("count (수집 결과 건수) : %s " % response.count)
    print("supplyCostTotal (공급가액 합계) : %s " % response.supplyCostTotal)
    print("taxTotal (세액 합계) : %s " % response.taxTotal)
    print("amountTotal (합계 금액) : %s " % response.amountTotal)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
