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
홈택스연동 인증관리를 위한 URL을 반환합니다.
 - 인증방식에는 부서사용자/공인인증서 인증 방식이 있습니다.
 - 반환된 URL은 보안정책에 따라 30초의 유효시간을 갖습니다.
 - https://docs.popbill.com/httaxinvoice/python/api#GetCertificatePopUpURL
'''

try:
    print("=" * 15 + " 홈택스연동 인증관리 팝업 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    url = htTaxinvoiceService.getCertificatePopUpURL(CorpNum)

    print("URL : %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
