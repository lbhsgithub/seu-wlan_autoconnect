#### 2018.12.25 - 2018.12.30 part-time  
**Reason**：Campus wifi (seu-wlan) needs to log in every starting up, so I want to skip such a troublesome step, and make it just like a common wifi.  
- 12.25 - 12.26
    - know some basic knowledge, like:
        - operation on the browser actually is some information exchange.
        - browsers can easily catch these information above.
        - password is simply encrypted by base64.
    - So I just need to copy information captured by browser and do little modification, then post it via *python*. At last, put this *.py to *startup folder* of Windows.
- 12.28 - 12.29
    - To share this program without knowing others password, I make a GUI to record user's password (already encrypted). 
    - This GUI only appears at the first open, then it will use passward saved in record file to post directly.
- 12.30
    - I add a label "add to startup folder" on GUI but it need administrator rights. 
    - Then I know what is UAC and write it into my program. 