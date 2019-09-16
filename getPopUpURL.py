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
홈택스 전자세금계산서 보기 팝업 URL을 반환합니다.
- 보안정책에 따라 반환된 URL은 30초의 유효시간을 갖습니다.
'''

try:
    print("=" * 15 + " 홈택스 전자세금계산서 보기 팝업 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 국세청 승인번호
    NTSConfirmNum = "201809194100020300000cd5"

    url = htTaxinvoiceService.getPopUpURL(CorpNum, NTSConfirmNum)

    print("URL : %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
