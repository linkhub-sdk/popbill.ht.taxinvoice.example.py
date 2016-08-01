# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 정액제 서비스 상태 확인 " + "=" * 15)
    '''
        FlatRateState 구성
            referenceID     (사업자번호)
            contractDT      (정액제 서비스 시작일시)
            useEndDate      (정액제 서비스 종료일)
            baseDate        (자동연장 결제일)
            state           (정액제 서비스 상태)
            closeRequestYN  (정액제 서비스 해지신청 여부)
            useRestrictYN   (정액제 서비스 사용제한 여부)
            closeOnExpired  (정액제 서비스 만료 시 해지여부)
            unPaidYN        (미수금 보유여부)
    '''

    response = htTaxinvoiceService.getFlatRateState(testValue.testCorpNum, testValue.testUserID)

    for key, value in response.__dict__.items():
        print("%s : %s" % (key, value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
