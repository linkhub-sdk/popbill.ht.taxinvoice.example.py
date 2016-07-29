# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService,PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + "팝빌회원 잔여포인트 확인" + "=" * 15)
    balance = htTaxinvoiceService.getBalance(testValue.testCorpNum)
    print("잔여포인트: %f" % balance)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
