import sys
sys.path.append('..')

from SdpBody import SdpBody

s_body = file('0001.sip').read()
body = SdpBody(s_body)
print str(body)
