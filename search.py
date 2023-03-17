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
수집 상태 확인(GetJobState API) 함수를 통해 상태 정보 확인된 작업아이디를 활용하여 현금영수증 매입/매출 내역을 조회합니다.
- https://developers.popbill.com/reference/httaxinvoice/python/api/search#Search
"""

try:
    print("=" * 15 + " 수집 결과 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob)시 발급받은 작업아이디
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

    # 종사업장번호 유무 (None , "0" , "1" 중 택 1)
    # - None = 전체 , 0 = 없음, 1 = 있음
    TaxRegIDYN = ""

    # 종사업장번호의 주체 ("S" , "B" , "T" 중 택 1)
    # └ S = 공급자 , B = 공급받는자 , T = 수탁자
    # - 미입력시 전체조회
    TaxRegIDType = "S"

    # 종사업장번호
    # 다수기재시 콤마(",")로 구분하여 구성 ex ) "0001,0002"
    # - 미입력시 전체조회
    TaxRegID = ""

    # 페이지번호
    Page = 1

    # 페이지당 목록개수, 최대값 1000
    PerPage = 10

    # 정렬방향 D-내림차순, A-오름차순
    Order = "D"

    # 거래처 상호 / 사업자번호 (사업자) / 주민등록번호 (개인) / "9999999999999" (외국인) 중 검색하고자 하는 정보 입력
    # - 사업자번호 / 주민등록번호는 하이픈('-')을 제외한 숫자만 입력
    # - 미입력시 전체조회
    SearchString = ""

    response = htTaxinvoiceService.search(
        CorpNum,
        JobID,
        Type,
        TaxType,
        PurposeType,
        TaxRegIDType,
        TaxRegIDYN,
        TaxRegID,
        Page,
        PerPage,
        Order,
        UserID,
        SearchString,
    )

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
        print("trusteeEmail (수탁자 담당자 이메일) : %s" % info.trusteeEmail)
        print("*" * 50)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
