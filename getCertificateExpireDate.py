# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

'''
팝빌에 등록되어 있는 홈택스 공인인증서의 만료일시를 확인합니다.
'''

try:
    print("=" * 15 + " 홈택스 공인인증서 만료일시 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    expireDate = htTaxinvoiceService.getCertificateExpireDate(CorpNum, UserID)

    print("공인인증서 만료일시 : %s" % expireDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
