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

'''
연동회원의 정액제 서비스 이용상태를 확인합니다.
'''

try:
    print("=" * 15 + " 정액제 서비스 상태 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = htTaxinvoiceService.getFlatRateState(CorpNum, UserID)

    for key, value in response.__dict__.items():
        print("%s : %s" % (key, value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
