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
팝빌에 전자세금계산서 전용 부서사용자를 등록합니다.
- https://developers.popbill.com/reference/httaxinvoice/python/api/cert#RegistDeptUser
"""

try:
    print("=" * 15 + " 부서사용자 계정등록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 부서사용자 계정아이디
    DeptUserID = "deptuserid"

    # 부서사용자 계정비밀번호
    DeptUserPWD = "deptuserpwd"

    # 부서사용자 대표자 주민번호
    IdentityNum = ""

    # 팝빌회원 아이디
    UserID = "testkorea"

    result = htTaxinvoiceService.registDeptUser(CorpNum, DeptUserID, DeptUserPWD, IdentityNum, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
