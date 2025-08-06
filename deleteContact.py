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
연동회원의 담당자를 삭제합니다.
- https://developers.popbill.com/reference/httaxinvoice/python/common-api/member#DeleteContact
"""

try:
    print("=" * 15 + " 담당자 삭제 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 삭제할 담당자 아이디
    TargetUserID = "testkorea20250806_01"

    # 팝빌 담당자 아이디
    UserID = testValue.testUserID

    result = htTaxinvoiceService.deleteContact(CorpNum, TargetUserID, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Popbill Exception : [%d] %s" % (PE.code, PE.message))
