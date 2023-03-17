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
from popbill import HTTaxinvoiceService, PopbillException, RefundForm

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest
htTaxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
htTaxinvoiceService.UseStaticIP = testValue.UseStaticIP
htTaxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원 포인트를 환불 신청합니다.
- https://developers.popbill.com/reference/httaxinvoice/python/api/point#Refund
"""

try:
    print("=" * 15 + " 환불 신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 환불 신청 객체 정보
    refundForm = RefundForm(
        # 담당자명
        contactName="환불신청테스트",
        # 담당자 연락처
        tel="01077777777",
        # 환불 신청 포인트
        requestPoint="10",
        # 은행명
        accountBank="국민",
        # 계좌번호
        accountNum="123123123-123",
        # 예금주명
        accountName="예금주",
        # 환불사유
        reason="테스트 환불 사유",
    )

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    response = htTaxinvoiceService.refund(CorpNum, refundForm, UserID)

    print(" code (요청에 대한 응답 상태 코드) : %s" % response.code)
    print(" message (요청에 대한 응답 메시지) : %s" % response.message)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
