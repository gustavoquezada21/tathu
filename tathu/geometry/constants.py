#
# This file is part of TATHU - Tracking and Analysis of Thunderstorms.
# Copyright (C) 2022 INPE.
#
# TATHU - Tracking and Analysis of Thunderstorms is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

from osgeo import ogr

# Geometry
EXAMPLE_GEOMETRY = ogr.CreateGeometryFromWkt('POLYGON((-87.7066264194337 14.5002961500494,-87.6886589047003 14.5002961500494,-87.6886589047003 14.4463968410661,-87.5808538163001 14.4463968410661,-87.5808538163001 14.4643632773939,-87.5269512721001 14.4643632773939,-87.5269512721001 14.4463968410661,-87.4730487279 14.4463968410661,-87.4730487279 14.4284304047384,-87.4191461836999 14.4284304047384,-87.4191461836999 14.4104639684107,-87.3832111542332 14.4104639684107,-87.3832111542332 14.3924975320829,-87.3652436394998 14.3924975320829,-87.3652436394998 14.3745310957552,-87.3293086100331 14.3745310957552,-87.3293086100331 14.3924975320829,-87.3113410952997 14.3924975320829,-87.3113410952997 14.4104639684107,-87.2394710363663 14.4104639684107,-87.2394710363663 14.320631786772,-87.2574385510996 14.320631786772,-87.2574385510996 14.3026653504442,-87.2215035216329 14.3026653504442,-87.2215035216329 14.2846989141165,-87.2035360068995 14.2846989141165,-87.2035360068995 14.2667324777887,-87.2215035216329 14.2667324777887,-87.2215035216329 14.2128331688055,-87.1496334626995 14.2128331688055,-87.1496334626995 14.248766041461,-87.1316659479661 14.248766041461,-87.1316659479661 14.2667324777887,-87.1136984332327 14.2667324777887,-87.1136984332327 14.3385982230997,-87.1316659479661 14.3385982230997,-87.1316659479661 14.3565646594274,-87.1496334626995 14.3565646594274,-87.1496334626995 14.3745310957552,-87.1676009774328 14.3745310957552,-87.1676009774328 14.4643632773939,-87.1496334626995 14.4643632773939,-87.1496334626995 14.5002961500494,-87.077763403766 14.5002961500494,-87.077763403766 14.4643632773939,-87.0957309184994 14.4643632773939,-87.0957309184994 14.4104639684107,-87.1136984332327 14.4104639684107,-87.1136984332327 14.3745310957552,-87.077763403766 14.3745310957552,-87.077763403766 14.3565646594274,-86.9879258300992 14.3565646594274,-86.9879258300992 14.3745310957552,-86.9699583153658 14.3745310957552,-86.9699583153658 14.3924975320829,-86.9519908006325 14.3924975320829,-86.9519908006325 14.4284304047384,-86.8621532269657 14.4284304047384,-86.8621532269657 14.4104639684107,-86.8441857122323 14.4104639684107,-86.8441857122323 14.3385982230997,-86.8621532269657 14.3385982230997,-86.8621532269657 14.320631786772,-86.880120741699 14.320631786772,-86.880120741699 14.3026653504442,-86.9519908006325 14.3026653504442,-86.9519908006325 14.320631786772,-86.9879258300992 14.320631786772,-86.9879258300992 14.3026653504442,-87.0058933448325 14.3026653504442,-87.0238608595659 14.3026653504442,-87.0238608595659 14.2846989141165,-87.0418283742993 14.2846989141165,-87.077763403766 14.2846989141165,-87.077763403766 14.2667324777887,-87.0957309184994 14.2667324777887,-87.0957309184994 14.248766041461,-87.1136984332327 14.248766041461,-87.1136984332327 14.2128331688055,-87.1316659479661 14.2128331688055,-87.1316659479661 14.1948667324778,-87.1496334626995 14.1948667324778,-87.1496334626995 14.1769002961501,-87.1676009774328 14.1769002961501,-87.1855684921662 14.1769002961501,-87.1855684921662 14.0511352418559,-87.2035360068995 14.0511352418559,-87.2035360068995 14.0152023692004,-87.2215035216329 14.0152023692004,-87.2215035216329 13.9972359328727,-87.2035360068995 13.9972359328727,-87.2035360068995 13.9792694965449,-87.1676009774328 13.9792694965449,-87.1676009774328 13.9972359328727,-87.1496334626995 13.9972359328727,-87.1496334626995 14.0152023692004,-87.0957309184994 14.0152023692004,-87.0957309184994 13.9972359328727,-87.077763403766 13.9972359328727,-87.077763403766 13.9433366238894,-87.0238608595659 13.9433366238894,-87.0238608595659 13.9613030602172,-86.9699583153658 13.9613030602172,-86.9519908006325 13.9613030602172,-86.9519908006325 13.9972359328727,-86.9340232858991 13.9972359328727,-86.9340232858991 14.0152023692004,-86.9160557711657 14.0152023692004,-86.8980882564324 14.0152023692004,-86.8980882564324 14.0511352418559,-86.880120741699 14.0511352418559,-86.880120741699 14.0870681145114,-86.8621532269657 14.0870681145114,-86.8621532269657 14.1230009871668,-86.8441857122323 14.1230009871668,-86.8441857122323 14.1589338598223,-86.8262181974989 14.1589338598223,-86.8262181974989 14.1769002961501,-86.8082506827656 14.1769002961501,-86.8082506827656 14.1948667324778,-86.7004455943654 14.1948667324778,-86.682478079632 14.1948667324778,-86.682478079632 14.2307996051333,-86.6645105648987 14.2307996051333,-86.6645105648987 14.248766041461,-86.6465430501653 14.248766041461,-86.6465430501653 14.3026653504442,-86.5926405059652 14.3026653504442,-86.5746729912319 14.3026653504442,-86.5746729912319 14.320631786772,-86.5567054764985 14.320631786772,-86.5567054764985 14.3385982230997,-86.5387379617651 14.3385982230997,-86.5387379617651 14.3565646594274,-86.5207704470318 14.3565646594274,-86.5028029322984 14.3565646594274,-86.5028029322984 14.3745310957552,-86.4668679028317 14.3745310957552,-86.4489003880983 14.3745310957552,-86.4489003880983 14.3924975320829,-86.3770303291649 14.3924975320829,-86.3770303291649 14.3745310957552,-86.3410952996982 14.3745310957552,-86.3410952996982 14.3565646594274,-86.3590628144315 14.3565646594274,-86.3590628144315 14.2846989141165,-86.2871927554981 14.2846989141165,-86.2871927554981 14.248766041461,-86.2692252407647 14.248766041461,-86.2692252407647 14.2667324777887,-86.2512577260313 14.2667324777887,-86.2512577260313 14.2846989141165,-86.233290211298 14.2846989141165,-86.233290211298 14.2667324777887,-86.1973551818313 14.2667324777887,-86.1973551818313 14.1230009871668,-86.2153226965646 14.1230009871668,-86.2153226965646 14.0691016781836,-86.1973551818313 14.0691016781836,-86.1973551818313 14.0511352418559,-86.1793876670979 14.0511352418559,-86.1793876670979 14.0152023692004,-86.1973551818313 14.0152023692004,-86.3410952996982 14.0152023692004,-86.3410952996982 14.0331688055281,-86.4129653586316 14.0331688055281,-86.4129653586316 13.9792694965449,-86.430932873365 13.9792694965449,-86.430932873365 13.9433366238894,-86.4489003880983 13.9433366238894,-86.4489003880983 13.9253701875617,-86.4668679028317 13.9253701875617,-86.4668679028317 13.8894373149062,-86.4848354175651 13.8894373149062,-86.4848354175651 13.8714708785785,-86.5028029322984 13.8714708785785,-86.5028029322984 13.8535044422507,-86.5207704470318 13.8535044422507,-86.5387379617651 13.8535044422507,-86.5387379617651 13.835538005923,-86.5567054764985 13.835538005923,-86.5746729912319 13.835538005923,-86.5746729912319 13.8175715695953,-86.5926405059652 13.8175715695953,-86.5926405059652 13.7996051332675,-86.5746729912319 13.7996051332675,-86.5746729912319 13.763672260612,-86.5567054764985 13.763672260612,-86.5567054764985 13.7457058242843,-86.5387379617651 13.7457058242843,-86.5387379617651 13.7277393879566,-86.5567054764985 13.7277393879566,-86.5746729912319 13.7277393879566,-86.5746729912319 13.7097729516288,-86.5926405059652 13.7097729516288,-86.5926405059652 13.6558736426456,-86.6106080206986 13.6558736426456,-86.6285755354319 13.6558736426456,-86.6285755354319 13.6738400789733,-86.6465430501653 13.6738400789733,-86.6465430501653 13.6558736426456,-86.6645105648987 13.6558736426456,-86.6645105648987 13.6379072063179,-86.682478079632 13.6379072063179,-86.682478079632 13.5660414610069,-86.6465430501653 13.5660414610069,-86.6465430501653 13.5840078973347,-86.6106080206986 13.5840078973347,-86.6106080206986 13.5660414610069,-86.5926405059652 13.5660414610069,-86.5746729912319 13.5660414610069,-86.5746729912319 13.6019743336624,-86.5567054764985 13.6019743336624,-86.5567054764985 13.6199407699901,-86.5028029322984 13.6199407699901,-86.4848354175651 13.6199407699901,-86.4848354175651 13.6558736426456,-86.4668679028317 13.6558736426456,-86.4489003880983 13.6558736426456,-86.4489003880983 13.6918065153011,-86.430932873365 13.6918065153011,-86.430932873365 13.7097729516288,-86.4129653586316 13.7097729516288,-86.3949978438982 13.7097729516288,-86.3949978438982 13.7277393879566,-86.3770303291649 13.7277393879566,-86.3770303291649 13.7457058242843,-86.3590628144315 13.7457058242843,-86.3590628144315 13.763672260612,-86.3231277849648 13.763672260612,-86.3231277849648 13.7457058242843,-86.2871927554981 13.7457058242843,-86.2871927554981 13.6918065153011,-86.2692252407647 13.6918065153011,-86.2692252407647 13.6199407699901,-86.2871927554981 13.6199407699901,-86.2871927554981 13.6019743336624,-86.3051602702314 13.6019743336624,-86.3051602702314 13.5840078973347,-86.3231277849648 13.5840078973347,-86.3231277849648 13.5660414610069,-86.3410952996982 13.5660414610069,-86.4129653586316 13.5660414610069,-86.4129653586316 13.5301085883514,-86.430932873365 13.5301085883514,-86.430932873365 13.5121421520237,-86.3770303291649 13.5121421520237,-86.3770303291649 13.494175715696,-86.3949978438982 13.494175715696,-86.3949978438982 13.4762092793682,-86.4129653586316 13.4762092793682,-86.4129653586316 13.4402764067127,-86.430932873365 13.4402764067127,-86.430932873365 13.3863770977295,-86.4489003880983 13.3863770977295,-86.4489003880983 13.3324777887463,-86.4668679028317 13.3324777887463,-86.4668679028317 13.3145113524186,-86.4848354175651 13.3145113524186,-86.5028029322984 13.3145113524186,-86.5028029322984 13.2965449160908,-86.5207704470318 13.2965449160908,-86.5207704470318 13.2606120434353,-86.5387379617651 13.2606120434353,-86.5387379617651 13.2426456071076,-86.5567054764985 13.2426456071076,-86.5567054764985 13.2067127344521,-86.5746729912319 13.2067127344521,-86.5746729912319 13.0629812438302,-86.5926405059652 13.0629812438302,-86.5926405059652 13.0270483711747,-86.6106080206986 13.0270483711747,-86.7004455943654 13.0270483711747,-86.7004455943654 13.009081934847,-86.7184131090987 13.009081934847,-86.7184131090987 12.9911154985193,-86.7363806238321 12.9911154985193,-86.7363806238321 12.9731490621915,-86.7543481385655 12.9731490621915,-86.8262181974989 12.9731490621915,-86.8262181974989 12.9551826258638,-86.8441857122323 12.9551826258638,-86.8621532269657 12.9551826258638,-86.8621532269657 12.937216189536,-86.880120741699 12.937216189536,-86.880120741699 12.9012833168806,-86.8621532269657 12.9012833168806,-86.8621532269657 12.8653504442251,-86.880120741699 12.8653504442251,-86.8980882564324 12.8653504442251,-86.8980882564324 12.7934846989141,-86.880120741699 12.7934846989141,-86.880120741699 12.7575518262586,-86.8980882564324 12.7575518262586,-86.8980882564324 12.7216189536032,-86.9160557711657 12.7216189536032,-86.9160557711657 12.7036525172754,-86.9340232858991 12.7036525172754,-86.9340232858991 12.6856860809477,-86.9519908006325 12.6856860809477,-86.9519908006325 12.6317867719645,-86.9699583153658 12.6317867719645,-86.9699583153658 12.5778874629812,-86.9879258300992 12.5778874629812,-86.9879258300992 12.5599210266535,-87.0058933448325 12.5599210266535,-87.0058933448325 12.523988153998,-87.0238608595659 12.523988153998,-87.0238608595659 12.4880552813426,-87.0418283742993 12.4880552813426,-87.0418283742993 12.4700888450148,-87.0597958890326 12.4700888450148,-87.0597958890326 12.4341559723593,-87.077763403766 12.4341559723593,-87.077763403766 12.4161895360316,-87.0957309184994 12.4161895360316,-87.1136984332327 12.4161895360316,-87.1136984332327 12.3982230997039,-87.1316659479661 12.3982230997039,-87.1676009774328 12.3982230997039,-87.1676009774328 12.3802566633761,-87.1855684921662 12.3802566633761,-87.2035360068995 12.3802566633761,-87.2035360068995 12.3622902270484,-87.2215035216329 12.3622902270484,-87.2574385510996 12.3622902270484,-87.2574385510996 12.3443237907206,-87.275406065833 12.3443237907206,-87.2933735805663 12.3443237907206,-87.2933735805663 12.3263573543929,-87.3113410952997 12.3263573543929,-87.3113410952997 12.3083909180652,-87.3293086100331 12.3083909180652,-87.3832111542332 12.3083909180652,-87.3832111542332 12.2904244817374,-87.4011786689665 12.2904244817374,-87.4191461836999 12.2904244817374,-87.4191461836999 12.2724580454097,-87.4371136984332 12.2724580454097,-87.4550812131666 12.2724580454097,-87.4550812131666 12.2544916090819,-87.4910162426333 12.2544916090819,-87.4910162426333 12.2724580454097,-87.5449187868334 12.2724580454097,-87.5449187868334 12.2544916090819,-87.5628863015668 12.2544916090819,-87.5628863015668 12.2365251727542,-87.5808538163001 12.2365251727542,-87.5988213310335 12.2365251727542,-87.5988213310335 12.2185587364265,-87.6167888457669 12.2185587364265,-87.7066264194337 12.2185587364265,-87.7066264194337 12.2005923000987,-87.724593934167 12.2005923000987,-87.724593934167 12.182625863771,-87.7605289636338 12.182625863771,-87.7605289636338 12.2005923000987,-87.8144315078338 12.2005923000987,-87.8144315078338 12.2185587364265,-87.8323990225672 12.2185587364265,-87.8323990225672 12.2365251727542,-87.8503665373006 12.2365251727542,-87.8503665373006 12.2185587364265,-87.8863015667673 12.2185587364265,-87.8863015667673 12.2365251727542,-87.9042690815006 12.2365251727542,-87.9042690815006 12.2544916090819,-87.922236596234 12.2544916090819,-87.922236596234 12.2724580454097,-87.9402041109674 12.2724580454097,-87.9402041109674 12.2904244817374,-88.0120741699008 12.2904244817374,-88.0120741699008 12.3083909180652,-88.0300416846342 12.3083909180652,-88.0300416846342 12.2904244817374,-88.0659767141009 12.2904244817374,-88.0659767141009 12.3083909180652,-88.119879258301 12.3083909180652,-88.119879258301 12.3263573543929,-88.1378467730344 12.3263573543929,-88.1378467730344 12.3083909180652,-88.1917493172344 12.3083909180652,-88.1917493172344 12.3263573543929,-88.2097168319678 12.3263573543929,-88.2097168319678 12.3443237907206,-88.2456518614345 12.3443237907206,-88.2456518614345 12.3083909180652,-88.3534569498347 12.3083909180652,-88.3534569498347 12.3263573543929,-88.4432945235015 12.3263573543929,-88.4432945235015 12.3443237907206,-88.4792295529682 12.3443237907206,-88.4792295529682 12.3622902270484,-88.4971970677016 12.3622902270484,-88.4971970677016 12.3443237907206,-88.5510996119017 12.3443237907206,-88.5510996119017 12.3622902270484,-88.569067126635 12.3622902270484,-88.569067126635 12.4161895360316,-88.5331320971683 12.4161895360316,-88.515164582435 12.4161895360316,-88.515164582435 12.4341559723593,-88.4971970677016 12.4341559723593,-88.4971970677016 12.4700888450148,-88.515164582435 12.4700888450148,-88.515164582435 12.523988153998,-88.4971970677016 12.523988153998,-88.4971970677016 12.5778874629812,-88.515164582435 12.5778874629812,-88.515164582435 12.6677196446199,-88.4971970677016 12.6677196446199,-88.4971970677016 12.7036525172754,-88.515164582435 12.7036525172754,-88.515164582435 12.6856860809477,-88.5331320971683 12.6856860809477,-88.5331320971683 12.7036525172754,-88.5510996119017 12.7036525172754,-88.5510996119017 12.7216189536032,-88.5331320971683 12.7216189536032,-88.5331320971683 12.7395853899309,-88.5510996119017 12.7395853899309,-88.5510996119017 12.7575518262586,-88.569067126635 12.7575518262586,-88.569067126635 12.7934846989141,-88.5870346413684 12.7934846989141,-88.5870346413684 12.8114511352419,-88.6050021561018 12.8114511352419,-88.6050021561018 12.9192497532083,-88.5870346413684 12.9192497532083,-88.5870346413684 13.009081934847,-88.6050021561018 13.009081934847,-88.6050021561018 13.0450148075025,-88.5870346413684 13.0450148075025,-88.5870346413684 13.1528134254689,-88.569067126635 13.1528134254689,-88.569067126635 13.1707798617966,-88.5510996119017 13.1707798617966,-88.5510996119017 13.2606120434353,-88.5331320971683 13.2606120434353,-88.5331320971683 13.3145113524186,-88.515164582435 13.3145113524186,-88.515164582435 13.3324777887463,-88.4971970677016 13.3324777887463,-88.4971970677016 13.350444225074,-88.515164582435 13.350444225074,-88.515164582435 13.3684106614018,-88.5331320971683 13.3684106614018,-88.5331320971683 13.422309970385,-88.515164582435 13.422309970385,-88.515164582435 13.4762092793682,-88.4971970677016 13.4762092793682,-88.4971970677016 13.494175715696,-88.4792295529682 13.494175715696,-88.4792295529682 13.5480750246792,-88.4612620382349 13.5480750246792,-88.4612620382349 13.5660414610069,-88.4432945235015 13.5660414610069,-88.4432945235015 13.5840078973347,-88.4253270087682 13.5840078973347,-88.4253270087682 13.6199407699901,-88.4073594940348 13.6199407699901,-88.4073594940348 13.6918065153011,-88.3893919793014 13.6918065153011,-88.3893919793014 13.7277393879566,-88.3714244645681 13.7277393879566,-88.3714244645681 13.7457058242843,-88.3534569498347 13.7457058242843,-88.3354894351014 13.7457058242843,-88.3354894351014 13.763672260612,-88.2636193761679 13.763672260612,-88.2456518614345 13.763672260612,-88.2456518614345 13.7816386969398,-88.2276843467012 13.7816386969398,-88.2276843467012 13.7996051332675,-88.1737818025011 13.7996051332675,-88.1558142877677 13.7996051332675,-88.1558142877677 13.8175715695953,-88.1378467730344 13.8175715695953,-88.1378467730344 13.8535044422507,-88.119879258301 13.8535044422507,-88.119879258301 13.8714708785785,-88.1019117435676 13.8714708785785,-88.1019117435676 13.9972359328727,-88.119879258301 13.9972359328727,-88.119879258301 14.0152023692004,-88.1378467730344 14.0152023692004,-88.1378467730344 14.0691016781836,-88.119879258301 14.0691016781836,-88.119879258301 14.0870681145114,-88.1019117435676 14.0870681145114,-88.1019117435676 14.1230009871668,-88.0839442288343 14.1230009871668,-88.0839442288343 14.1589338598223,-88.0659767141009 14.1589338598223,-88.0659767141009 14.1948667324778,-88.0480091993676 14.1948667324778,-88.0480091993676 14.2307996051333,-88.0300416846342 14.2307996051333,-88.0300416846342 14.2667324777887,-87.9581716257007 14.2667324777887,-87.9402041109674 14.2667324777887,-87.9402041109674 14.2846989141165,-87.922236596234 14.2846989141165,-87.922236596234 14.320631786772,-87.9402041109674 14.320631786772,-87.9402041109674 14.3385982230997,-87.9581716257007 14.3385982230997,-87.9581716257007 14.3565646594274,-87.9402041109674 14.3565646594274,-87.9402041109674 14.3924975320829,-87.9581716257007 14.3924975320829,-87.9581716257007 14.4104639684107,-87.9402041109674 14.4104639684107,-87.9402041109674 14.4284304047384,-87.922236596234 14.4284304047384,-87.922236596234 14.4463968410661,-87.8863015667673 14.4463968410661,-87.8683340520339 14.4463968410661,-87.8683340520339 14.4643632773939,-87.8323990225672 14.4643632773939,-87.8323990225672 14.4463968410661,-87.8144315078338 14.4463968410661,-87.8144315078338 14.4284304047384,-87.7964639931005 14.4284304047384,-87.7964639931005 14.3924975320829,-87.7784964783671 14.3924975320829,-87.7784964783671 14.4284304047384,-87.7605289636338 14.4284304047384,-87.7605289636338 14.4643632773939,-87.7425614489004 14.4643632773939,-87.7425614489004 14.4823297137216,-87.724593934167 14.4823297137216,-87.7066264194337 14.4823297137216,-87.7066264194337 14.5002961500494),(-86.6645105648987 13.6558736426456,-86.6645105648987 13.6738400789733,-86.682478079632 13.6738400789733,-86.682478079632 13.6558736426456,-86.6645105648987 13.6558736426456),(-86.7543481385655 13.2965449160908,-86.7543481385655 13.2606120434353,-86.6465430501653 13.2606120434353,-86.6465430501653 13.2965449160908,-86.7543481385655 13.2965449160908),(-86.7184131090987 13.3684106614018,-86.7184131090987 13.3324777887463,-86.682478079632 13.3324777887463,-86.682478079632 13.350444225074,-86.6645105648987 13.350444225074,-86.6645105648987 13.4043435340573,-86.682478079632 13.4043435340573,-86.682478079632 13.3863770977295,-86.7004455943654 13.3863770977295,-86.7004455943654 13.3684106614018,-86.7184131090987 13.3684106614018),(-87.0058933448325 13.8535044422507,-87.0058933448325 13.835538005923,-86.9699583153658 13.835538005923,-86.9699583153658 13.8535044422507,-87.0058933448325 13.8535044422507))')
