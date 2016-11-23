# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

'''
수집된 전자(세금)계산서 1건의 상세정보를 확인합니다.
- 응답항목에 관한 정보는 "[홈택스 전자(세금)계산서 연계 API 연동매뉴얼]
  > 4.1.2. GetTaxinvoice 응답전문 구성" 을 참고하시기 바랍니다.
'''

try:
    print("=" * 15 + " 세금계산서 상세정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 전자세금계산서 국세청승인번호
    NTSConfirmNum = "20161121410002030000079e"

    taxinvoice = htTaxinvoiceService.getTaxinvoice(CorpNum, NTSConfirmNum, UserID)

    for key, value in taxinvoice.__dict__.items():
        if not key.startswith("__"):
            if key == 'detailList' or key == 'addContactList':
                print("%s :" % key)
                i = 1
                for t in value:
                    print("    %d:" % i)
                    for k, v in t.__dict__.items():
                        print("        %s : %s" % (k,v))
                    i += 1
            else:
                print("%s : %s" % (key,value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
