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
    print("=" * 15 + "상세정보 확인" + "=" * 15)
    '''
        전자세금계산서 1건에 대한 상세정보를 조회합니다.
        응답 항목은 "[연동매뉴얼 > 4.1.2 GetTaxinvoice 응답전문 구성]" 을 참조하시면
        보다 자세한 내용을 확인할 수 있습니다.
    '''

    # 전자세금계산서 국세청승인번호
    NTSConfirmNum = "201607274100002900000209"

    taxinvoice = htTaxinvoiceService.getTaxinvoice(testValue.testCorpNum, NTSConfirmNum, testValue.testUserID)

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
