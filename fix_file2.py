import os
import base64

for i, j, k in os.walk('./'):
    pass

for i in k:
    if i[0:7] == '{-sec-}':
        re_name = base64.b64decode(i[7:-4].encode('utf-8'))
        os.rename(i, re_name)
