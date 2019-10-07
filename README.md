# AioQrtag

download:
```
 git clone git+https://github.com/dark0ghost/AioQrtag.git
 ```
 
use:
```python
from AioQrtg import qrtag

#async 
async def start():
 async with aiohttp.ClientSession() as session:
  f= qrtag.QrTag(session)
   with open("file.jpg", "wb") as file:
        file.write(await qr.create(data=message.text))
#sync
f = qrtag.QrTag()
 with open("file.jpg", "wb") as file:
        file.write(qr.sync_call(data="google.com",size=4,form="jpg"))

  

```
 
