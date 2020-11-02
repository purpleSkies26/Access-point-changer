# Access-point-changer
Changes your access point through automated selenium/webdriver

So technically naisipan ko tong gawing 2/3 days ago kasi wala ako magawa.
This set up was specifically made for huawei B315-936 router so conflicts will be enocuntered with the links
Take note: Script was developed in Linux environment kaya baka maka encounter kayo ng error sa Windows.

Requirements:
    Python - altlis ung supported ung pc nio
    Selenium -  Pede niyo to idownload through "pip install slelenium"
    firefox - yan lang muna #wala akong chrome driver, 
    
Report kung may mga errors directly sa github ko, since beta pa to working naman saken kasi para sa router ko talaga yan.

Instructions:
  1. If pareho tayo ng router tsaka globe ang sim mo, pssible easy run lang to.
   
  2. Double check mo ung link1 tsaka link2 sa file kasi iba iba ung links depende sa router.
    
    PS: 
      Make sure to specify your driver path para di kayo magkanda error error
      
      Dalawa ung link kasi may na encounter akong issue na nagrerefresh si website adn nawawala sa DOm ung element kaya nageeror si Selenium, 
      if may marunong sa inyo mag ayos, pede rin. 
    
  3.Make sure na tama ung inputs niyo, ung user at password , malalaman lang if mali if hindi nag go through yung link 2 kasi redirected yun sa homepage.
    pede niyo ayusin through a loop with assert function pag nag password error.
    
  4. Please any improvements on the code will be helpful, mag fork lang kayo.
  
Additional Information:
  Production mode - anak headleas yung firedox, ibig sabihin walang magpopop-up na browser, silent browser kumabaga
  Debuggging mode - gagamitin ung default Firefox

Usage:
    "python apnchange.py"


