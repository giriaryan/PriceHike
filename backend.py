import re
from urllib import request
from  bs4 import BeautifulSoup
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# aip14m 256
aip14m_f = ['aip14m_f','https://www.flipkart.com/apple-iphone-14-midnight-256-gb/p/itmdb32e3c997112']
aip14m_a = ['aip14m_a','https://www.amazon.in/Apple-iPhone-14-128GB-Midnight/dp/B0BDJ6N5D6?th=1']
aip14m_r = ['aip14m_r','https://www.reliancedigital.in/apple-iphone-14-256-gb-midnight/p/493177754']
aip14m_v = ['aip14m_v','https://www.vijaysales.com/apple-iphone-14-256-gb-midnight/21972']

# aip13  128
aip13_f = ['aip13_f','https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0']
aip13_a = ['aip13_a','https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD']
aip13_r = ['aip13_r','https://www.reliancedigital.in/apple-iphone-13-128-gb-midnight-black-/p/491997699']
aip13_v = ['aip13_v','https://www.vijaysales.com/apple-iphone-13-128-gb-storage-midnight/17459']

# aip12  128
aip12_f = ['aip12_f','https://www.flipkart.com/apple-iphone-12-black-128-gb/p/itmf1f0a58f1ecd7']
aip12_a = ['aip12_a','https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5WD9D6']
aip12_r = ['aip12_r','https://www.reliancedigital.in/apple-iphone-12-128-gb-black/p/491901533']
aip12_v = ['aip12_v','https://www.vijaysales.com/apple-iphone-12-128-gb-black/14681']

# op9pr]
op9pr_f = ['op9pr_f','https://www.flipkart.com/oneplus-9-pro-5g-morning-mist-128-gb/p/itm3892a7120e77b']
op9pr_a = ['op9pr_a','https://www.amazon.in/Test-Exclusive_2020_1166-Multi-3GB-Storage/dp/B089MS7D9K']
op9pr_r = ['op9pr_r','https://www.reliancedigital.in/oneplus-9-pro-128-gb-8-gb-ram-morning-mist-mobile-phone/p/491947275']
op9pr_v = ['op9pr_v','https://www.vijaysales.com/mobiles-and-tablets/model/buy-oneplus-9-pro-mobile-phone']

# opnce2
opnce2_f = ['opnce2_f','https://www.flipkart.com/oneplus-nord-ce-2-5g-gray-mirror-128-gb/p/itm2a9883679c57c']
opnce2_a = ['opnce2_a','https://www.amazon.in/OnePlus-Nord-Mirror-128GB-Storage/dp/B09RGBYBND']
opnce2_r = ['opnce2_r','https://www.reliancedigital.in/oneplus-nord-ce-2-5g-128-gb-6-gb-ram-blue-mobile-phone/p/492664465']
opnce2_v = ['opnce2_v','https://www.vijaysales.com/oneplus-nord-ce-2-5g-6-gb-ram-128-gb-rom-bahama-blue/19268']

# op10t
op10t_f = ['op10t_f','https://www.flipkart.com/oneplus-10-pro-5g-volcanic-black-128-gb/p/itmcd1af0daf0394']
op10t_a = ['op10t_a','https://www.amazon.in/OnePlus-Volcanic-Black-128GB-Storage/dp/B09V2P9C3S']
op10t_r = ['op10t_r','https://www.reliancedigital.in/oneplus-10-pro-128-gb-ram-8-gb-ram-volcanic-black-mobile-phone/p/492849811']
op10t_v = ['op10t_v','https://www.vijaysales.com/oneplus-10-pro-5g-8-gb-ram-128-gb-rom-volcanic-black/19753']

# sgzf4
sgzf4_f = ['sgzf4_f','https://www.flipkart.com/samsung-galaxy-z-flip4-5g-graphite-128-gb/p/itm11000771a7590']
sgzf4_a = ['sgzf4_a','https://www.amazon.in/Samsung-Galaxy-Graphite-Storage-Without/dp/B0B8ZBLZZQ']
sgzf4_r = ['sgzf4_r','https://www.reliancedigital.in/samsung-galaxy-z-flip4-5g-128-gb-8-gb-ram-graphite-mobile-phone/p/493177493']
sgzf4_v = ['sgzf4-v','https://www.vijaysales.com/samsung-galaxy-z-flip-4-8-gb-ram-128-gb-rom-graphite/21699']

# sm535g
sm535g_f = ['sm535g_f','https://www.flipkart.com/samsung-m53-5g-mystique-green-128-gb/p/itm5a9079ecadda0']
sm535g_a = ['sm535g_a','https://www.amazon.in/Samsung-Mystique-Storage-Purchased-Separately/dp/B09XJ36Q27']
sm535g_r = ['sm535g_r','https://www.reliancedigital.in/samsung-galaxy-m53-5g-128-gb-8-gb-ram-mystique-green-mobile-phone/p/492850536']
sm535g_v = ['sm535g_v','https://www.vijaysales.com/samsung-galaxy-m53-5g-8-gb-ram-128-gb-rom-green/20815']
 
# sgs22u
sgs22u_f = ['sgs22u_f','https://www.flipkart.com/samsung-galaxy-s22-ultra-5g-burgundy-256-gb/p/itm4a36ce5b68e8b']
sgs22u_a = ['sgs22u_a','https://www.amazon.in/Samsung-Burgundy-Storage-Additional-Exchange/dp/B09SH7FDKT']
sgs22u_r = ['sgs22u_r','https://www.reliancedigital.in/samsung-s22-ultra-5g-256-gb-12-gb-ram-burgundy-mobile-phone/p/492849213']
sgs22u_v = ['sgs22u_v','https://www.vijaysales.com/samsung-galaxy-s22-ultra-12-gb-ram-256-gb-rom-dark-red/19291']

# x11i
x11i_f = ['x11i_f','https://www.flipkart.com/xiaomi-11i-5g-pacific-pearl-128-gb/p/itm64ae12c24445b']
x11i_a = ['x11i_a','https://www.amazon.in/Xiaomi-Pacific-Pearl-128GB-Storage/dp/B09QD34G5W']
x11i_r = ['x11i_r','https://www.reliancedigital.in/xiaomi-11i-5g-128-gb-6-gb-ram-pacific-pearl-mobile-phone/p/492574891']
x11i_v = ['x11i_v','https://www.vijaysales.com/xiaomi-11i-6-gb-ram-128-gb-rom-pacific-pearl/18575']

# x11prplus5g
x11prplus5g_f = ['x11prplus5g_f','https://www.flipkart.com/redmi-note-11-pro-plus-5g-phantom-white-128-gb/p/itmd029928dc2e7e?pid=MOBGDD7K823GNF4D&lid=LSTMOBGDD7K823GNF4DFZBCV3&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=color']
x11prplus5g_a = ['x11prplus5g_a','https://www.amazon.in/Redmi-Phantom-Additional-Exchange-Included/dp/B09T2VXJRH']
x11prplus5g_r = ['x11prplus5g_r','https://www.reliancedigital.in/redmi-note-11-pro-plus-5g-128-gb-6-gb-ram-phantom-white-mobile-phone/p/492849641']
x11prplus5g_v = ['x11prplus5g_v','https://www.vijaysales.com/redmi-note-11-pro-5g-6-gb-ram-128-gb-rom-phantom-white/19992']

# x12pr5g
x12pr5g_f = ['x12pr5g_f','https://www.flipkart.com/xiaomi-12-pro-5g-opera-mauve-256-gb/p/itm4e017bacc4e75']
x12pr5g_a = ['x12pr5g_a','https://www.amazon.in/Xiaomi-Storage-Snapdragon-Flagship-Cameras/dp/B09XB8WTXN']
x12pr5g_r = ['x12pr5g_r','https://www.reliancedigital.in/xiaomi-12-pro-5g-256gb-8gb-ram-opera-mauve-mobile-phone/p/492850155']
x12pr5g_v = ['x12pr5g_v','https://www.vijaysales.com/xiaomi-12-pro-5g-8-gb-ram-256-gb-rom-opera-mauve/20078']

# Laptop

# HP Pavillion Gaming (hppg)
hppg_f = ['hppg_f','https://www.flipkart.com/hp-pavilion-ryzen-5-hexa-core-amd-r5-5600h-8-gb-512-gb-ssd-windows-10-4-graphics-nvidia-geforce-gtx-1650-144-hz-15-ec2004ax-gaming-laptop/p/itm98c94bbf9bc20?pid=COMG5GZXPWMGTNWS&lid=LSTCOMG5GZXPWMGTNWSQE9WVW&marketplace=FLIPKART&store=6bo%2Fb5g&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=6fa71cb7-45b8-4525-8801-4dc2259ed3dd.COMG5GZXPWMGTNWS.SEARCH&ppt=dynamic&ppn=productListView&ssid=e4ty3fhu800000001664692152565']
hppg_a = ['hppg_a','https://www.amazon.in/HP-Pavilion-Processor-Graphics-15-ec2150AX/dp/B09MF8KMRW?th=1']
hppg_r = ['hppg_r','https://www.reliancedigital.in/hp-15-ec2008ax-pavilion-gaming-laptop-amd-ryzen-5-5600h-8gb-512gb-ssd-4gb-nvidia-geforce-gtx-1650-graphics-windows-10-mso-fhd-39-62-cm-15-6-inch-/p/491997441?gclid=EAIaIQobChMI2fGM3_XA-gIVD5NmAh2OfQgzEAQYAyABEgIFevD_BwE']
hppg_v = ['hppg_v','https://www.vijaysales.com/hp-pavilion-gaming-15-ec2008ax-amd-ryzen-5-5600h-processor-8-gb-ram-512-gb-ssd-15-6-fhd-display-4-gb-nvidia-graphics-win-10-mso/17206']

# HP Pavillion (hpp)
hpp_f = ['hpp_f','https://www.flipkart.com/hp-pavilion-core-i5-11th-gen-16-gb-512-gb-ssd-windows-11-home-14-dv1002tu-thin-light-laptop/p/itm0c76b79955b2e?pid=COMG87FPKUHZS4ZM&lid=LSTCOMG87FPKUHZS4ZMNSJLPB&marketplace=FLIPKART&q=hp+pavillion+15+i5+16gb&store=search.flipkart.com&srno=s_1_3&otracker=search&otracker1=search&fm=organic&iid=3d94d679-8c57-412c-80af-79389858403a.COMG87FPKUHZS4ZM.SEARCH&ppt=dynamic&ppn=productListView&ssid=ip95tdq5w00000001664692474128&qH=d9b7c81eda5e14ce']
hpp_a = ['hpp_a','https://www.amazon.in/HP-Pavilion-Micro-Edge-Graphics-14-dv2014TU/dp/B0B1M9HYBT']
hpp_r = ['hpp_r','https://www.reliancedigital.in/hp-pavilion-x360-14-ek0078tu-convertible-laptop-12th-gen-intel-core-i5-1235u-16gb-512gb-ssd-iris-xe-graphics-windows-11-home-mso-fhd-35-6-cm-14-inch-space-blue/p/493177050']
hpp_v = ['hpp_v','https://www.vijaysales.com/hp-pavilion-14-dv2014tu-laptop-12th-gen-core-i5-16gb-ram-512-gb-ssd-14-inch-35-6-cm-display-intel-iris-xe-graphics-windows-11-mso/20806']

# Apple Macbook Pro (amp)
amp_f = ['amp_f','https://www.flipkart.com/apple-2020-macbook-pro-m1-8-gb-512-gb-ssd-mac-os-big-sur-myd92hn-a/p/itmbe44ce71a4225?pid=COMFXEKMBJNDSE6N&lid=LSTCOMFXEKMBJNDSE6NSZTMA0&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&iid=695a8202-0534-4428-8a73-6f291186b2c8.COMFXEKMBJNDSE6N.SEARCH&ssid=y3mjp7s9cg0000001664692536131']
amp_a = ['amp_a','https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5VSQNG']
amp_r = ['amp_r','https://www.reliancedigital.in/apple-myd82hna-macbook-pro-apple-m1-chip-8gb-256gb-ssd-macos-big-sur-retina-33-78-cm-13-3-inch-/p/491946467']
amp_v = ['amp_v','https://www.vijaysales.com/apple-myd82hn-a-macbook-pro-apple-m1-chip-8gb-ram-256-gb-ssd-13-3-33-78-cm-display-integrated-graphics-mac-os-big-sur-space-grey/15041']

# Apple Macbook Air (ama)
ama_f = ['ama_f','https://www.flipkart.com/apple-2020-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn93hn-a/p/itmb53580bb51a7e']
ama_a = ['ama_a','https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5XSG8Z/ref=sr_1_1_sspa?crid=2Q7NBVQA5QAWB&keywords=apple+macbook+air&qid=1664692796&qu=eyJxc2MiOiI0LjA5IiwicXNhIjoiMy4xOSIsInFzcCI6IjAuODEifQ%3D%3D&sprefix=apple+macbook+ai%2Caps%2C278&sr=8-1-spons&psc=1']
ama_r = ['ama_r','https://www.reliancedigital.in/apple-mgn63hna-macbook-air-apple-m1-chip-8gb-256gb-ssd-macos-big-sur-retina-33-78-cm-13-3-inch-/p/491946461']
ama_v = ['ama_v','https://www.vijaysales.com/apple-mgn63hn-a-macbook-air-apple-m1-chip-8gb-ram-256gb-ssd-13-3-33-78-cm-display-integrated-graphics-mac-os-big-sur-space-grey/15034']

# DELL inspiron (di)
di_f = ['di_f','https://www.flipkart.com/dell-inspiron-core-i5-11th-gen-16-gb-512-gb-ssd-windows-11-home-5410-2-1-laptop/p/itm73b71e2dbb41c?pid=COMG9ETA9GRZQ9XY&lid=LSTCOMG9ETA9GRZQ9XYIORM3I&marketplace=FLIPKART&q=dell+14+inspiron+&store=6bo%2Fb5g&srno=s_1_6&otracker=search&otracker1=search&fm=organic&iid=f8fc46d9-1dea-4325-bdaf-235f7de4f727.COMG9ETA9GRZQ9XY.SEARCH&ppt=pp&ppn=pp&ssid=e1iy06dfi80000001664693033195&qH=60399fbf7409dabf']
di_a = ['di_a','https://www.amazon.in/Dell-Inspiron-i5-1155G7-GEFORCE-D560595WIN9S/dp/B09F3Q93T1/ref=sr_1_2_sspa?crid=OYAMDYSKTKQQ&keywords=dell+inspiron+5410&qid=1664693150&qu=eyJxc2MiOiI0Ljk4IiwicXNhIjoiNC42NCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=dell+inspiron+5410%2Caps%2C206&sr=8-2-spons&psc=1&smid=A1XQ7OTKA85S11&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSTNSTFFNWEFPV1lQJmVuY3J5cHRlZElkPUEwNTM3MDUzM0c3VDg5SEVXQVRYNSZlbmNyeXB0ZWRBZElkPUEwMDQ1MDEzMkxYN1BWUzFFVTNYRSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=']
di_r = ['di_r','https://www.reliancedigital.in/dell-5410-inspiron-14-2-in-1-convertible-laptop-11th-intel-core-i5-1155g7-16gb-512gb-ssd-intel-uhd-graphics-windows-11-mso-fhd-35-56-cm-14-inch-/p/492575082']
di_v = ['di_v','https://www.vijaysales.com/dell-inspiron-14-5410-d560631win9s-laptop-11th-gen-core-i5-8-gb-ram-512gb-ssd-14-inch-35-56-cm-display-nvidia-2gb-graphics-windows-11-mso/19477']

# DELL G15 5520 (dg15)
dg15_f = ['dg15_f','https://www.flipkart.com/dell-g15-core-i7-12th-gen-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-3060-g15-5520-gaming-laptop/p/itm640139151b5eb?pid=COMGDJJYGC5HHVDS&lid=LSTCOMGDJJYGC5HHVDSBQGBSK&marketplace=FLIPKART&q=dell+5520+12th+gen+16gb&store=6bo&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=43cca6cf-3709-48f2-a82b-dd48de6030f9.COMGDJJYGC5HHVDS.SEARCH&ppt=sp&ppn=sp&ssid=rcl1kgm2c00000001664693379189&qH=1ea340b6f093a28f']
dg15_a = ['dg15_a','https://www.amazon.in/Dell-Windows-Gaming-Laptop-i7-12700H/dp/B09XXNKLBF/ref=sr_1_3?crid=1IMOGIW0M58UM&keywords=dell+5520+12th+gen+16gb&qid=1664693365&qu=eyJxc2MiOiIwLjk4IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&s=computers&sprefix=delll+5520+12th+gen+16g%2Ccomputers%2C182&sr=1-3']
dg15_r = ['dg15_r','https://www.reliancedigital.in/dell-5520-g15-gaming-laptop-12th-gen-intel-core-i7-12700h-16gb-512gb-ssd-6-gb-nvidia-geforce-rtx-3060-graphics-windows-11-mso-fhd-39-62-cm-15-6-inch-/p/492850230']
dg15_v = ['dg15_v','https://www.vijaysales.com/dell-g15-5520-d560823win9b-gaming-laptop-12th-gen-intel-core-i7-16-gb-ram-512-gb-ssd-15-6-inches-39-61-display-4-gb-nvidia-graphics-win-11/20600']

# Asus ROG G15 (arg15)
arg15_f = ['arg15_f','https://www.flipkart.com/asus-rog-zephyrus-g15-ryzen-9-octa-core-amd-r9-6900hs-16-gb-1-tb-ssd-windows-11-home-8-gb-graphics-nvidia-geforce-rtx-3070-ti-240-hz-ga503rw-ln067ws-gaming-laptop/p/itmf85f93675eadd?pid=COMGFWCYZ3GYT3WZ&lid=LSTCOMGFWCYZ3GYT3WZCJN5AD&marketplace=FLIPKART&q=asus+rog+g15&store=search.flipkart.com&srno=s_1_5&otracker=search&otracker1=search&fm=organic&iid=30ba1bd0-89c6-4c33-8daf-39faf26f98f8.COMGFWCYZ3GYT3WZ.SEARCH&ppt=pp&ppn=pp&ssid=xvid4tvas00000001664694632084&qH=1aa8a6fa4971dd6b']
arg15_a = ['arg15_a','https://www.amazon.in/ASUS-Zephyrus-6900HS-Windows-GA503RW-LN066WS/dp/B0B6PRLPMW/ref=sr_1_11?crid=1JGU0VFFE4HQS&keywords=asus%2Brog%2Bg15&qid=1664694709&qu=eyJxc2MiOiI1LjY2IiwicXNhIjoiNS4wOCIsInFzcCI6IjAuMDAifQ%3D%3D&s=computers&sprefix=asus%2Brog%2Bg15%2Ccomputers%2C226&sr=1-11&th=1']
arg15_r = ['arg15_r','https://www.reliancedigital.in/asus-rog-zephyrus-g15-gaming-laptop-amd-ryzen-9-6900hs-16-gb-ram-1-tb-ssd-8-gb-rtx-3070-ti-graphics-windows-11-home-mso-qhd-39-62-cm-15-6-inch-/p/492850916']
arg15_v = ['arg15_v','https://www.vijaysales.com/asus-rog-zephyrus-g15-ga503rw-ln067ws-laptop-amd-ryzen-9-6900hs-16-gb-ram-1-tb-ssd-15-6-inch-39-62-cm-display-8-gb-rtx-graphics-win-11-mso/21516']

# Asus Vivobook K15 (avk15)
avk15_f = ['avk15_f','https://www.flipkart.com/asus-vivobook-k15-oled-2022-core-i5-11th-gen-16-gb-1-tb-hdd-256-gb-ssd-windows-11-home-k513ea-l523ws-thin-light-laptop/p/itm391804c2ca1cd']
avk15_a = ['avk15_f','https://www.amazon.in/ASUS-VivoBook-i5-1135G7-15-6-inch-K513EA-L512TS/dp/B098F7RXYR?th=1']
avk15_r = ['avk15_f','https://www.reliancedigital.in/asus-l513ws-vivobook-k15-laptop-11th-gen-intel-core-i5-1135g7-16gb-512-gb-sdd-intel-iris-xe-graphics-windows-11-oled-39-6-cm-15-6-inch-/p/492850311']
avk15_v = ['avk15_f','https://www.vijaysales.com/asus-vivobook-k15-k513ea-l513ws-oled-laptop-11th-gen-core-i5-16gb-ram-512-gb-ssd-15-6-inch-39-62-cm-display-intel-graphics-win-11-mso/20778']

# Lenovo Ideapad 3 (li3)
li3_f = ['li3_f','https://www.flipkart.com/lenovo-ideapad-3-core-i3-11th-gen-8-gb-512-gb-ssd-windows-11-home-82h801l7in-82h802fjin-82h802l3in-82h801lhin-thin-light-laptop/p/itm0e009f57a591b?pid=COMG9VHHG6Q3RRJX&lid=LSTCOMG9VHHG6Q3RRJXQHPK6Q&marketplace=FLIPKART&q=lenevo+ideapad+3+i3+11th&store=6bo%2Fb5g&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=73ddd09a-d599-4045-a386-669350380c6e.COMG9VHHG6Q3RRJX.SEARCH&ppt=sp&ppn=sp&ssid=zm5fkvyrds0000001664695163865&qH=b2b459bae7bdd235']
li3_a = ['li3_a','https://www.amazon.in/Lenovo-IdeaPad-Warranty-Platinum-81X800LGIN/dp/B0B2RBP83P/ref=sr_1_4?crid=1GOEATBKKT5YB&keywords=lenovo%2Bideapad%2B3&qid=1664695138&qu=eyJxc2MiOiI1LjA1IiwicXNhIjoiNC44MSIsInFzcCI6IjMuNTkifQ%3D%3D&s=computers&sprefix=lenovo%2Bideapad%2B%2Ccomputers%2C230&sr=1-4&th=1']
li3_r = ['li3_r','https://www.reliancedigital.in/lenovo-l2in-ideapad-3-laptop-11th-gen-intel-core-i3-1115g4-8gb-256gb-ssd-intel-uhd-graphics-windows-11-mso-full-hd-39-62-cm-15-6-inch-/p/492574725']
li3_v = ['li3_v','https://www.vijaysales.com/lenovo-ideapad-3-15iml05-laptop-10th-gen-core-i3-processor-8-gb-ram-1-tb-hdd-15-6-fhd-ips-display-intel-uhd-graphics-win-10-mso/16991']

# Lenovo Legion 5 Pro (ll5p)
ll5p_f = ['ll5p_f','https://www.flipkart.com/lenovo-legion-5-pro-core-i7-11th-gen-16-gb-1-tb-ssd-windows-11-home-6-gb-graphics-nvidia-geforce-rtx-3060-16ith6h-gaming-laptop/p/itm4f84bb97cb59c?pid=COMG72M96UVEZU2G&lid=LSTCOMG72M96UVEZU2G80WNXC&marketplace=FLIPKART&q=lenevo+legion+5+pro+11th+gen&store=search.flipkart.com&srno=s_1_23&otracker=search&otracker1=search&fm=Search&iid=35226fe6-7adc-44c7-9d98-f672333aa73c.COMG72M96UVEZU2G.SEARCH&ppt=sp&ppn=sp&ssid=g9ckf74hhs0000001664696635715&qH=53a8dd68359e58d0']
ll5p_a = ['ll5p_a','https://www.amazon.in/Lenovo-Legion5-11th-Intel-40-64cm/dp/B09GTXTCCK/ref=sr_1_5?crid=6BJ7SRIL4NVE&keywords=lenovo%2Blegion%2Bpro%2B11th%2Bgen%2Bi7%2Brtx%2B3060&qid=1664696697&s=computers&sprefix=lenovo%2Blegion%2Bpro%2B11th%2Bgen%2Bi7%2Brtx%2B30%2Ccomputers%2C184&sr=1-5&th=1']
ll5p_r = ['ll5p_r','https://www.reliancedigital.in/lenovo-5lin-legion-5-pro-gaming-laptop-11th-gen-intel-core-i7-11800h-32-gb-1tb-ssd-8-gb-nvidia-geforce-rtx-3070-graphics-windows-11-mso-wqxga-40-64-cm-16-inch-/p/492850704']
ll5p_v = ['ll5p_v','https://www.vijaysales.com/lenovo-legion-5-pro-lenovo-11th-ci7-16g-gaming-laptop-11th-gen-intel-core-i7-16-gb-ram-1-tb-ssd-16-qhd-display-6gb-nvidia-graphics-win-11/17693']

# Noise Colorfit Icon Buzz (ncib)
ncib_f = ['ncib_f','https://www.flipkart.com/noise-icon-buzz-bt-calling-1-69-display-ai-voice-assistance-built-in-games-smartwatch/p/itm8e2dc3457a808']
ncib_a = ['ncib_a','https://www.amazon.in/Noise-ColorFit-Bluetooth-Assistance-Monitors/dp/B09KS1RNWS?th=1']
ncib_r = ['ncib_r','https://www.reliancedigital.in/noise-colorfit-icon-buzz-smart-watch-silver-grey/p/492575339']
ncib_v = ['ncib_v','https://www.vijaysales.com/noise-colorfit-icon-plus-bluetooth-calling-smart-watch-with-100-cloud-based-watch-faces-9-sports-modes-silver-grey/21224']

# Boat Xtend (bx)
bx_f = ['bx_f','https://www.flipkart.com/boat-extend-smartwatch/p/itm0a47b4dad4074']
bx_a = ['bx_a','https://www.amazon.in/boAt-Smartwatch-Multiple-Monitoring-Resistance/dp/B096VF5YYF?th=1']
bx_r = ['bx_r','https://www.reliancedigital.in/boat-watch-xtend-rtl-4-29-cm-1-69-inch-smartwatch-with-built-in-alexa-voice-assistant-pitch-black/p/491998422']
bx_v = ['bx_v','https://www.vijaysales.com/boat-xtend-rtl-smartwatch-with-built-in-alexa-real-time-stress-monitoring-24-7-heart-rate-monitor-sandy-cream/17280']

# OnePlus Nord Buds (onb)
onb_f = ['onb_f','https://www.flipkart.com/oneplus-nord-buds-bluetooth-headset/p/itmb538cc617782c?pid=ACCGDGPDGEY3EXG8&lid=LSTACCGDGPDGEY3EXG8T3GJMF&marketplace=FLIPKART&q=oneplus+nord+buds&store=0pm%2Ffcn&spotlightTagId=BestsellerId_0pm%2Ffcn&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=0ee53e4b-60f7-4604-935a-027a939ec5af.ACCGDGPDGEY3EXG8.SEARCH&ppt=sp&ppn=sp&ssid=xq8up48ccw0000001664697408172&qH=4560f18211166333']
onb_a = ['onb_a','https://www.amazon.in/OnePlus-Wireless-Earbuds-Titanium-Playback/dp/B09ZHPN8W5/ref=sr_1_3?crid=12K4530HKVXNA&keywords=oneplus%2Bnord%2Bbuds&qid=1664697420&qu=eyJxc2MiOiIyLjU3IiwicXNhIjoiMS44NSIsInFzcCI6IjEuNTUifQ%3D%3D&s=electronics&sprefix=oneplus%2Bnord%2Bbud%2Celectronics%2C274&sr=1-3&th=1']
onb_r = ['onb_r','https://www.reliancedigital.in/oneplus-nord-buds-wireless-earbuds-with-4-mics-and-ai-noise-reduction-black-slate/p/492912670']
onb_v = ['onb_v','https://www.vijaysales.com/oneplus-nord-buds-with-ai-noise-cancellation-for-calls-dolby-atmos-support-ip55-dust-and-water-resistance-earbuds-black-slate/20209']

# Boat Airdopes 131 (ba131)
ba131_f = ['ba131_f','https://www.flipkart.com/boat-airdopes-131-pro-11mm-drivers-45hrs-playback-asap-charge-quad-mic-enx-bluetooth-headset/p/itmb8dea5750714c?pid=ACCGDQMA9QHE6D5C&lid=LSTACCGDQMA9QHE6D5CYHF8B4&marketplace=FLIPKART&q=boat+airdopes+121v2tws&store=0pm%2Ffcn%2F821%2Fa7x%2F2si&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na&fm=Search&iid=9f355bd7-6721-49b2-bddf-d3bc15a42386.ACCGDQMA9QHE6D5C.SEARCH&ppt=sp&ppn=sp&ssid=3pcrlgc2800000001664697529409&qH=72d57a221b0df391']
ba131_a = ['ba131_a','https://www.amazon.in/boAt-Airdopes-121-Signature-Indicator/dp/B09YRYCWF8/ref=sr_1_4?crid=FUARG3VT2AF8&keywords=boat+airdopes+131+pro&qid=1664697569&qu=eyJxc2MiOiI0LjcwIiwicXNhIjoiMy45OSIsInFzcCI6IjMuMzEifQ%3D%3D&s=electronics&sprefix=boat+airdopes+131+p%2Celectronics%2C220&sr=1-4']
ba131_r = ['ba131_r','https://www.reliancedigital.in/boat-airdopes-131-true-wireless-earbuds-with-insta-wake-n-pair-technology-viper-green/p/493285605']
ba131_v = ['ba131_v','https://www.vijaysales.com/search/boat-airdopes']

# Boat Stone 352 (bs352)
bs352_f = ['bs352_f','https://www.flipkart.com/boat-stone-350-10-w-bluetooth-speaker/p/itmba477fc3ec7ae?pid=ACCFVWMHBGUNFG97&lid=LSTACCFVWMHBGUNFG97WDIOR1&marketplace=FLIPKART&q=boat+stone+352&store=0pm%2F0o7&spotlightTagId=BestsellerId_0pm%2F0o7&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=a680a920-b498-416c-bf34-788cb7c510d3.ACCFVWMHBGUNFG97.SEARCH&ppt=sp&ppn=sp&ssid=xt7hd0e4n40000001664697683343&qH=680a3ae3fc3f44d1']
bs352_a = ['bs352_a','https://www.amazon.in/boAt-Bluetooth-Resistance-Playtime-Multi-Compatibility/dp/B09TDK97JM/ref=sr_1_1?crid=293EX4M34NIUB&keywords=boat%2Bstone%2B350&qid=1664697705&qu=eyJxc2MiOiI1LjQzIiwicXNhIjoiNC42MCIsInFzcCI6IjQuMTcifQ%3D%3D&s=electronics&sprefix=boat%2Bstone%2B350%2Celectronics%2C238&sr=1-1&th=1']
bs352_r = ['bs352_r','https://www.reliancedigital.in/boat-stone-350-bluetooth-speaker-with-up-to-12-hours-of-playtime-black/p/492579289']
bs352_v = ['bs352_v','https://www.vijaysales.com/boat-stone-350-with-ipx7-splash-water-resistance-up-to-12h-nonstop-playtime-bluetooth-v5-0-edr-black/20111']

# Boat Stone 193 (bs193)
bs193_f = ['bs193_f','https://www.flipkart.com/boat-stone-190f-5-w-bluetooth-speaker/p/itm546fd8702e92f?pid=ACCFZKRPQFEBR6RF&lid=LSTACCFZKRPQFEBR6RFCF6AMG&marketplace=FLIPKART&q=boat+grenade&store=0pm%2F0o7&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=6798a241-2bf3-45f3-8cb2-2d9588690254.ACCFZKRPQFEBR6RF.SEARCH&ppt=sp&ppn=sp&qH=26854bac9e9759d2']
bs193_a = ['bs193_a','https://www.amazon.in/Stone-190-Bluetooth-Resistance-Lightweight/dp/B08447BPKQ/ref=sr_1_1?crid=2NHUKCRWSGT65&keywords=boat+stone+193&qid=1664697954&qu=eyJxc2MiOiIzLjk1IiwicXNhIjoiMy4zOSIsInFzcCI6IjIuMzIifQ%3D%3D&s=electronics&sprefix=boat+stone+19%2Celectronics%2C190&sr=1-1']
bs193_r = ['bs193_r','https://www.reliancedigital.in/boat-stone-193-bluetooth-multimedia-speaker-black/p/491897966']
bs193_v = ['bs193_v','https://www.vijaysales.com/boat-stone-193-portable-bluetooth-speaker-with-ipx7-water-and-dust-resistance-quick-wireless-connectivity-powerful-800-mah-battery-black/14146']


#Flipkart Data

f1 = aip14m_f
f2 = aip13_f
f3 = aip12_f
f4 = op9pr_f
f5 = opnce2_f
f6 = op10t_f
f7 = sgzf4_f
f8 = sm535g_f
f9 = sgs22u_f
f10 = x11i_f
f11 = x11prplus5g_f
f12 = x12pr5g_f
f13 = hppg_f
f14 = hpp_f
f15 = amp_f
f16 = ama_f
f17 = di_f
f18 = dg15_f
f19 = arg15_f
f20 = avk15_f
f21 = li3_f
f22 = ll5p_f
f23 = ncib_f
f24 = bx_f
f25 = onb_f
f26 = ba131_f
f27 = bs352_f
f28 = bs193_f

#Amazon Data
a1 = aip14m_a
a2 = aip13_a
a3 = aip12_a
a4 = op9pr_a
a5 = opnce2_a
a6 = op10t_a
a7 = sgzf4_a
a8 = sm535g_a
a9 = sgs22u_a
a10 = x11i_a
a11 = x11prplus5g_a
a12 = x12pr5g_a
a13 = hppg_a
a14 = hpp_a
a15 = amp_a
a16 = ama_a
a17 = di_a
a18 = dg15_a
a19 = arg15_a
a20 = avk15_a
a21 = li3_a
a22 = ll5p_a
a23 = ncib_a
a24 = bx_a
a25 = onb_a
a26 = ba131_a
a27 = bs352_a
a28 = bs193_a

#Amazon Reference Data

a_ref1  = ['a_ref1','https://www.pricebefore.com/iphone-14-256gb-midnight-p725159.html']
a_ref2  = ['a_ref2','https://www.pricebefore.com/apple-iphone-13-128gb-midnight-p649238.html']
a_ref3  = ['a_ref3','https://www.pricebefore.com/new-apple-iphone-12-128gb-black-p564928.html']
a_ref4  = ['a_ref4','https://www.pricebefore.com/oneplus-9-pro-5g-morning-mist-8gb-ram-128gb-storage-p579389.html']
a_ref5  = ['a_ref5','https://www.pricebefore.com/oneplus-nord-ce-2-5g-gray-mirror-6gb-ram-128gb-p668214.html']
a_ref6  = ['a_ref1','https://www.pricebefore.com/oneplus-10-pro-5g-volcanic-black-8gb-ram-128gb-storage-p678372.html']
a_ref7  = ['a_ref1','https://www.pricebefore.com/samsung-galaxy-z-flip4-5g-graphite-8gb-ram-128gb-storage-p728986.html']
a_ref8  = ['a_ref1','https://www.pricebefore.com/samsung-galaxy-m53-5g-mystique-green-8gb-128gb-storage-travel-p684856.html']
a_ref9  = ['a_ref1','https://www.pricebefore.com/samsung-galaxy-s22-ultra-5g-burgundy-12gb-256gb-storage-cost-p668740.html']
a_ref10 = ['a_ref1','https://www.pricebefore.com/xiaomi-11i-5g-pacific-pearl-6gb-ram-128gb-storage-p691485.html']
a_ref11 = ['a_ref1','https://www.pricebefore.com/redmi-note-11-pro-5g-phantom-white-6gb-ram-128gb-p675102.html']
a_ref12 = ['a_ref1','https://www.pricebefore.com/xiaomi-12-pro-5g-opera-mauve-8gb-ram-256gb-storage-p685447.html']
a_ref13 = ['a_ref1','https://www.pricebefore.com/hp-pavilion-gaming-amd-ryzen-5-5600h-39-6-cm-p651464.html']
a_ref14 = ['a_ref1','https://www.pricebefore.com/hp-pavilion-14-12th-gen-intel-core-i5-16gb-sdram-p692895.html']
a_ref15 = ['a_ref1','https://www.pricebefore.com/new-apple-macbook-pro-apple-m1-chip-13-inch-8gb-p544163.html']
a_ref16 = ['a_ref1','https://www.pricebefore.com/new-apple-macbook-air-apple-m1-chip-13-inch-8gb-p555366.html']
a_ref17 = ['a_ref1','https://www.pricebefore.com/dell-14-2021-i5-1155g7-2in1-touch-screen-laptop-8gb-p631930.html']
a_ref18 = ['a_ref1','https://www.pricebefore.com/dell-new-g15-5520-gaming-laptop-intel-i7-12700h-16gb-p682815.html']
a_ref19 = ['a_ref1','https://www.pricebefore.com/asus-rog-zephyrus-g15-2022-15-6-39-62-cms-p706478.html']
a_ref20 = ['a_ref1','https://www.pricebefore.com/asus-vivobook-k15-oled-intel-core-i5-1135g7-11th-gen-p630253.html']
a_ref21 = ['a_ref1','https://www.pricebefore.com/lenovo-ideapad-slim-3-11th-gen-intel-core-i3-15-p700205.html']
a_ref22 = ['a_ref1','https://www.pricebefore.com/lenovo-legion5-pro-11th-gen-intel-core-i7-16-40-p639111.html']
a_ref23 = ['a_ref1','https://www.pricebefore.com/noise-colorfit-icon-buzz-bluetooth-calling-smart-watch-voice-assistance-p662607.html']
a_ref24 = ['a_ref1','https://www.pricebefore.com/boat-watch-xtend-alexa-built-14-sports-modes-automatic-motion-p607644.html']
a_ref25 = ['a_ref1','https://www.pricebefore.com/oneplus-nord-buds-true-wireless-earbuds-12-4mm-titanium-drivers-m1695.html']
a_ref26 = ['a_ref1','https://www.pricebefore.com/boat-newly-launched-airdopes-121-pro-true-wireless-earbuds-boat-m45262.html']
a_ref27 = ['a_ref1','https://www.pricebefore.com/boat-stone-352-bluetooth-speaker-10w-rms-stereo-sound-ipx7-m88035.html']
a_ref28 = ['a_ref1','https://www.pricebefore.com/boat-stone-190-5-watt-truly-wireless-bluetooth-portable-speaker-m186063.html']

#Reliance Data

r1 = aip14m_r
r2 = aip13_r
r3 = aip12_r
r4 = op9pr_r
r5 = opnce2_r
r6 = op10t_r
r7 = sgzf4_r
r8 = sm535g_r
r9 = sgs22u_r
r10 = x11i_r
r11 = x11prplus5g_r
r12 = x12pr5g_r
r13 = hppg_r
r14 = hpp_r
r15 = amp_r
r16 = ama_r
r17 = di_r
r18 = dg15_r
r19 = arg15_r
r20 = avk15_r
r21 = li3_r
r22 = ll5p_r
r23 = ncib_r
r24 = bx_r
r25 = onb_r
r26 = ba131_r
r27 = bs352_r
r28 = bs193_r

#Vijaysales Data

v1 = aip14m_v
v2 = aip13_v
v3 = aip12_v
v4 = op9pr_v
v5 = opnce2_v
v6 = op10t_v
v7 = sgzf4_v
v8 = sm535g_v
v9 = sgs22u_v
v10 = x11i_v
v11 = x11prplus5g_v
v12 = x12pr5g_v
v13 = hppg_v
v14 = hpp_v
v15 = amp_v
v16 = ama_v
v17 = di_v
v18 = dg15_v
v19 = arg15_v
v20 = avk15_v
v21 = li3_v
v22 = ll5p_v
v23 = ncib_v
v24 = bx_v
v25 = onb_v
v26 = ba131_v
v27 = bs352_v
v28 = bs193_v


dataExcel_name = []
dataExcel_price = []
dataExcel_url = []
dataExcel_source = []

def flipkart(f):
    url = f[1]
    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')
    price = content.find('div',{'class': '_30jeq3 _16Jk6d'}).text
    name = content.find('span',{'class': 'B_NuCI'}).text
    price = price.replace("₹", "").replace(",", "")
    price = int(price)
    const_name = f[0].replace("_f", "")


    doc_ref = db.collection(u'PriceDate').document(f[0])
    doc_ref.set({
        u'product_name': name,
        u'product_price': price,
        u'product_url': url,
        u'const_name': const_name,
        u'product_source':'flipkart',
    })

    print("hogaya kam")
    print(f[0])



f_data_trial = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28]
for x in f_data_trial:
    flipkart(x)


def amazon(a):
    url = a[1]


    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')    
    price = content.find('span',{'class': 'price-final js-product-price'}).text
    name = content.find('h1',{'style': 'font-size:138.5%'}).text
    price = price.replace("₹", "").replace(",", "")
    price = int(price)
    const_name = a[0].replace("_a", "")

    
    doc_ref = db.collection(u'PriceDate').document(a[0])
    doc_ref.set({
        u'product_name': name,
        u'product_price': price,
        u'product_url': url,
        u'const_name': const_name,
        u'product_source':'amazon',
    })

a_numbers = [a_ref1, a_ref2, a_ref3, a_ref4, a_ref5, a_ref6, a_ref7, a_ref8, a_ref9, a_ref10, a_ref11, a_ref12, a_ref13, a_ref14, a_ref15, a_ref16, a_ref17, a_ref18, a_ref19, a_ref20, a_ref21, a_ref22, a_ref23, a_ref24, a_ref25, a_ref26, a_ref27, a_ref28]

for a_number in a_numbers:
    amazon(a_number)


r_numbers = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r25, r26, r27, r28]

def reliance(r):
    url = (r[1])
    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')
    price = content.find('span',{'class': 'pdp__offerPrice'}).text
    try:
         name = content.find('h1', {'class': 'pdp__title mb__20'}).text
    except:
         name = content.find('h1', {'pdp__title mb__8'}).text
    # name = content.find('h1', {'class': 'pdp__title mb__20'}).text
    price = price.replace("₹", "").replace(",", "")
    price = price[0:len(price)-3]
    price = int(price)
    const_name = r[0].replace("_r", "")

    doc_ref = db.collection(u'PriceDate').document(r[0])
    doc_ref.set({
        u'product_name': name,
        u'product_price': price,
        u'product_url': url,
        u'const_name': const_name,
        u'product_source':'amazon',
    })

    print(name)
    print(r[0])

for r_index in r_numbers:
    reliance(r_index)

v_numbers = [v1, v4, v7, v8, v9 ,v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28]


def vijaysales(v):
    url = (v[1])
    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')
    try:
        price_raw = content.find('div',{'class': 'priceMRP'}).text
    except:
        try:
            price_raw = content.find('div',{'class': 'Dynamic-Bucket-vsp dvpricepdlft'}).text
        except:
            try:
                price_raw = content.find('div',{'class': 'Dynamic-Bucket-vsp dvpricepdlft'}).text
            except:
                price_raw = '₹1,199'
    try:
        name = content.find('h1', {'id': 'ContentPlaceHolder1_h1ProductTitle'}).text
    except:
        try:
            name = content.find('h2', {'class': 'Dynamic-Bucket-ProductName'}).text
        except:
            name = 'boAt Airdopes 138 Truely Wireless Buds with 13 mm Dynamic Drivers, Bluetooth v5.0, boAt Signature Sound (Active Black)'

    sep = 'VSP'
    stripped = price_raw.split(sep, 1)[0]
    x = re.findall("[0-9]", stripped)
    pricefinal="".join(x)

    if pricefinal == '':
        sep = 'MRP'
        stripped = price_raw.split(sep, 1)[0]
        x = re.findall("[0-9]", stripped)
        pricefinal="".join(x)

    if pricefinal=='':
        sep = 'Inclusive'
        stripped = price_raw.split(sep, 1)[0]
        x = re.findall("[0-9]", stripped)
        pricefinal="".join(x)

    price = int(pricefinal)
    const_name = v[0].replace("_v", "")
    print(v[0])
    print(price)
    doc_ref = db.collection(u'PriceDate').document(v[0])
    doc_ref.set({
        u'product_name': name,
        u'product_price': price,
        u'product_url': url,
        u'const_name': const_name,
        u'product_source':'Vijay Sales',
    })

    
for v_index in v_numbers:
    vijaysales(v_index)