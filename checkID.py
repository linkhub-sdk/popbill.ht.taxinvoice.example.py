# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

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
사용하고자 하는 아이디의 중복여부를 확인합니다.
- https://developers.popbill.com/reference/httaxinvoice/python/api/member#CheckID
"""

try:
    print("=" * 15 + " 팝빌회원 아이디 중복확인 " + "=" * 15)

    # 중복확인할 아이디
    memberID = "testkorea"

    response = htTaxinvoiceService.checkID(memberID)

    print("처리결과 : [%d] %s" % (response.code, response.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
