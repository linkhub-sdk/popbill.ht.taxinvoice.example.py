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

'''
검색조건을 사용하여 수집결과를 조회합니다.
- 응답항목에 관한 정보는 "[홈택스연동(전자세금계산서) API 연동매뉴얼]
  > 3.2.1. Search (수집 결과 조회)" 을 참고하시기 바랍니다.
'''

try:
    print("=" * 15 + " 수집 결과 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "019103014000000001"

    # 문서형태 배열, N-일반전자세금계산서, M-수정전자세금계산서
    Type = ["N", "M"]

    # 과세형태 배열, T-과세, N-면세, Z-영세
    TaxType = ["T", "N", "Z"]

    # 영수/청구, R-영수, C-청구, N-없음
    PurposeType = ["R", "C", "N"]

    # 종사업자번호 사업자 유형, S-공급자, B-공급받는자, T-수탁자
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

    # 조회 검색어, 거래처 사업자번호 또는 거래처명 like 검색
    SearchString = ""

    response = htTaxinvoiceService.search(CorpNum, JobID, Type, TaxType, PurposeType, TaxRegIDType,
                                    TaxRegIDYN, TaxRegID, Page, PerPage, Order, UserID, SearchString)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    for info in response.list:
        print("\n==============전자세금계산서 정보>==============")
        print("ntsconfirmNum (국세청승인번호) : %s" % info.ntsconfirmNum)
        print("writeDate (작성일자) : %s" % info.writeDate)
        print("issueDate (발행일자) : %s" % info.issueDate)
        print("sendDate (전송일자) : %s" % info.sendDate)
        print("taxType (과세형태) : %s" % info.taxType)
        print("purposeType (영수/청구) : %s" % info.purposeType)
        print("supplyCostTotal (공급가액 합계) : %s" % info.supplyCostTotal)
        print("taxTotal (세액 합계) : %s" % info.taxTotal)
        print("totalAmount (합계금액) : %s" % info.totalAmount)
        print("remark1 (비고) : %s" % info.remark1)
        print("invoiceType (매입/매출) : %s" % info.invoiceType)

        print("\n수정 전자세금계산서 정보>")
        print("modifyYN (수정 전자세금계산서 여부) : %s" % info.modifyYN)
        print("orgNTSConfirmNum (원본 전자세금계산서 국세청승인번호) : %s" % info.orgNTSConfirmNum)

        print("\n전자세금계산서 품목 정보 (1개만 반환)>")
        print("purchaseDate (거래일자) : %s" % info.purchaseDate)
        print("itemName (품명) : %s" % info.itemName)
        print("spec (규격) : %s" % info.spec)
        print("qty (수량) : %s" % info.qty)
        print("unitCost (단가) : %s" % info.unitCost)
        print("supplyCost (공급가액) : %s" % info.supplyCost)
        print("tax (세액) : %s" % info.tax)
        print("remark (비고) : %s" % info.remark)

        print("\n공급자 정보>")
        print("invoicerCorpNum (공급자 사업자번호) : %s" % info.invoicerCorpNum)
        print("invoicerTaxRegID (공급자 종사업장번호) : %s" % info.invoicerTaxRegID)
        print("invoicerCorpName (공급자 상호) : %s" % info.invoicerCorpName)
        print("invoicerCEOName (공급자 대표자 성명) : %s" % info.invoicerCEOName)
        print("invoicerEmail (공급자 담당자 이메일) : %s" % info.invoicerEmail)

        print("\n공급받는자 정보>")
        print("invoiceeCorpNum (공급받는자 사업자번호) : %s" % info.invoiceeCorpNum)
        print("invoiceeType (공급받는자 구분) : %s" % info.invoiceeType)
        print("invoiceeTaxRegID (공급받는자 종사업장번호) : %s" % info.invoiceeTaxRegID)
        print("invoiceeCorpName (공급받는자 상호) : %s" % info.invoiceeCorpName)
        print("invoiceeCEOName (공급받는자 대표자 성명) : %s" % info.invoiceeCEOName)
        print("invoiceeEmail1 (공급받는자 담당자 이메일) : %s" % info.invoiceeEmail1)
        print("invoiceeEmail2 (ASP 연계사업자 메일) : %s" % info.invoiceeEmail2)

        print("\n수탁자 정보>")
        print("trusteeCorpNum (수탁자 사업자번호) : %s" % info.trusteeCorpNum)
        print("trusteeTaxRegID (수탁자 종사업장번호) : %s" % info.trusteeTaxRegID)
        print("trusteeCorpName (수탁자 상호) : %s" % info.trusteeCorpName)
        print("trusteeCEOName (수탁자 대표자 성명) : %s" % info.trusteeCEOName)
        print("trusteeEmail (수탁자 담당자 이메일) : %s" % info.trusteeEmail) + '\n'
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
