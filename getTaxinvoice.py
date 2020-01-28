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
수집된 전자(세금)계산서 1건의 상세정보를 확인합니다.
- https://docs.popbill.com/httaxinvoice/python/api#GetTaxinvoice
'''

try:
    print("=" * 15 + " 세금계산서 상세정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 전자세금계산서 국세청승인번호
    NTSConfirmNum = "201812264100020300002e07"

    taxinvoice = htTaxinvoiceService.getTaxinvoice(CorpNum, NTSConfirmNum, UserID)

    print("\n전자세금계산서 정보>")
    print("writeDate (작성일자) : %s" % taxinvoice.writeDate)
    print("issueDT (발행일시) : %s" % taxinvoice.issueDT)
    print("invoiceType (전자세금계산서 종류) : %s" % taxinvoice.invoiceType)
    print("taxType (과세형태) : %s" % taxinvoice.taxType)
    print("taxTotal (세액 합계) : %s" % taxinvoice.taxTotal)
    print("supplyCostTotal (공급가액 합계) : %s" % taxinvoice.supplyCostTotal)
    print("totalAmount (합계금액) : %s" % taxinvoice.totalAmount)
    print("purposeType (영수/청구) : %s" % taxinvoice.purposeType)
    print("serialNum (일련번호) : %s" % taxinvoice.serialNum)
    print("cash (현금) : %s" % taxinvoice.cash)
    print("chkBill (수표) : %s" % taxinvoice.chkBill)
    print("credit (외상) : %s" % taxinvoice.credit)
    print("note (어음) : %s" % taxinvoice.note)
    print("remark1 (비고1) : %s" % taxinvoice.remark1)
    print("remark2 (비고2): %s" % taxinvoice.remark2)
    print("remark3 (비고3): %s" % taxinvoice.remark3)
    print("ntsconfirmNum (국세청승인번호) : %s" % taxinvoice.ntsconfirmNum)

    print("\n수정 전자세금계산서 정보>")
    print("modifyCode (수정사유코드) : %s" % taxinvoice.modifyCode)
    print("orgNTSConfirmNum (원본 전자세금계산서 국세청승인번호) : %s" % taxinvoice.orgNTSConfirmNum)

    print("\n공급자 정보>")
    print("invoicerCorpNum (공급자 사업자번호) : %s" % taxinvoice.invoicerCorpNum)
    print("invoicerMgtKey (공급자 문서관리번호) : %s" % taxinvoice.invoicerMgtKey)
    print("invoicerTaxRegID (공급자 종사업장번호) : %s" % taxinvoice.invoicerTaxRegID)
    print("invoicerCorpName (공급자 상호) : %s" % taxinvoice.invoicerCorpName)
    print("invoicerCEOName (공급자 대표자명) : %s" % taxinvoice.invoicerCEOName)
    print("invoicerAddr (공급자 주소) : %s" % taxinvoice.invoicerAddr)
    print("invoicerBizType (공급자 업태) : %s" % taxinvoice.invoicerBizType)
    print("invoicerBizClass (공급자 종목) : %s" % taxinvoice.invoicerBizClass)
    print("invoicerContactName (공급자 담당자명) : %s" % taxinvoice.invoicerContactName)
    print("invoicerTEL (공급자 담당자 연락처) : %s" % taxinvoice.invoicerTEL)
    print("invoicerHP (공급자 담당자 휴대폰) : %s" % taxinvoice.invoicerHP)
    print("invoicerEmail (공급자 담당자 메일) : %s" % taxinvoice.invoicerEmail)

    print("\n공급받는자 정보>")
    print("invoiceeCorpNum (공급받는자 사업자번호) : %s" % taxinvoice.invoiceeCorpNum)
    print("invoiceeType (공급받는자 구분) : %s" % taxinvoice.invoiceeType)
    print("invoiceeMgtKey (공급받는자 문서관리번호) : %s" % taxinvoice.invoiceeMgtKey)
    print("invoiceeTaxRegID (공급받는자 종사업장번호) : %s" % taxinvoice.invoiceeTaxRegID)
    print("invoiceeCorpName (공급받는자 상호) : %s" % taxinvoice.invoiceeCorpName)
    print("invoiceeCEOName (공급받는자 대표자명) : %s" % taxinvoice.invoiceeCEOName)
    print("invoiceeAddr (공급받는자 주소) : %s" % taxinvoice.invoiceeAddr)
    print("invoiceeBizType (공급받는자 업태) : %s" % taxinvoice.invoiceeBizType)
    print("invoiceeBizClass (공급받는자 종목) : %s" % taxinvoice.invoiceeBizClass)
    print("invoiceeContactName1 (공급받는자 담당자명) : %s" % taxinvoice.invoiceeContactName1)
    print("invoiceeDeptName1 (공급받는자 부서명) : %s" % taxinvoice.invoiceeDeptName1)
    print("invoiceeTEL1 (공급받는자 담당자 연락처) : %s" % taxinvoice.invoiceeTEL1)
    print("invoiceeEmail1 (공급받는자 담당자 이메일) : %s" % taxinvoice.invoiceeEmail1)

    print("\n수탁자 정보>")
    print("trusteeCorpNum (수탁자 사업자번호) : %s" % taxinvoice.trusteeCorpNum)
    print("trusteeMgtKey (수탁자 문서관리번호) : %s" % taxinvoice.trusteeMgtKey)
    print("trusteeTaxRegID (수탁자 종사업장번호) : %s" % taxinvoice.trusteeTaxRegID)
    print("trusteeCorpName (수탁자 상호) : %s" % taxinvoice.trusteeCorpName)
    print("trusteeCEOName (수탁자 대표자명) : %s" % taxinvoice.trusteeCEOName)
    print("trusteeAddr (수탁자 주소) : %s" % taxinvoice.trusteeAddr)
    print("trusteeBizType (수탁자 업태) : %s" % taxinvoice.trusteeBizType)
    print("trusteeBizClass (수탁자 종목) : %s" % taxinvoice.trusteeBizClass)
    print("trusteeContactName (수탁자 담당자명) : %s" % taxinvoice.trusteeContactName)
    print("trusteeTEL (수탁자 담당자 연락처) : %s" % taxinvoice.trusteeTEL)
    print("trusteeHP (수탁자 담당자 휴대폰) : %s" % taxinvoice.trusteeHP)
    print("trusteeEmail (수탁자 담당자 메일) : %s" % taxinvoice.trusteeEmail) + '\n'

    print("=" * 15 + "상세항목(품목) 정보" + "=" * 15)
    if taxinvoice.detailList is not None:
        for detailList in taxinvoice.detailList:
            print("serialNum (일련번호) : %s" % detailList.serialNum)
            print("purchaseDT (거래일자) : %s" % detailList.purchaseDT)
            print("itemName (품명) : %s" % detailList.itemName)
            print("spec (규격) : %s" % detailList.spec)
            print("qty (수량) : %s" % detailList.qty)
            print("unitCost (단가) : %s" % detailList.unitCost)
            print("supplyCost (공급가액) : %s" % detailList.supplyCost)
            print("tax (세액) : %s" % detailList.tax)
            print("remark (비고) : %s" % detailList.remark)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
