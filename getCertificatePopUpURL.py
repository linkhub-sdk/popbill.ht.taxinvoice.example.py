# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService,PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + "홈택스 공인인증서 등록 팝업 URL" + "=" * 15)
    '''
        팝빌에 로그인 하지 않고 홈택스 공인인증서를 등록할 수 있는 팝업 URL을 반환합니다.
        * 보안정책에 의해 응답된 URL은 30초의 만료시간을 갖습니다.
    '''
    
    url = htTaxinvoiceService.getCertificatePopUpURL(testValue.testCorpNum,testValue.testUserID)

    print("URL : %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
