# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import ContactInfo, HTTaxinvoiceService ,PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

updateInfo = ContactInfo(
                    personName = "담당자 성명_0728",
                    tel = "010-1234-1234",
                    hp = "010-4324-4324",
                    fax = "02-6442-9700",
                    email = "code@linkhub.co.kr",
                    searchAllAllowYN = True,
                    mgtYN = False
                    )
try:
    print("=" * 15 + " 담당자 정보 수정 " + "=" * 15)

    result = htTaxinvoiceService.updateContact(testValue.testCorpNum, updateInfo, testValue.testUserID)

    print("처리결과 : [%d] %s" % (result.code,result.message) )
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
