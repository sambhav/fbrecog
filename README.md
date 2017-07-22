# fbrecog
An unofficial python wrapper for the Facebook face recognition endpoint
### fbrecog is a python wrapper that uses Facebook's face recognition to recognize faces in pictures. 
## How-To:

1. Install fbrecog from pip 
`pip install fbrecog`
2. Now simply import the recognize method from fbrecog module
`from fbrecog import recognize`
3. The recognize method takes 4 input args and returns an array of recognitions.
4. To get the access token simply go to https://developers.facebook.com/tools/explorer and get a user access token with *user_photos*, *publish_actions* and *user_posts* permissions.
5. Get your Facebook cookie and fb_dtsg token as follows:

  * Go to your Facebook profile.

 * Open chrome dev tools by `Right Click > Inspect`

 * Upload any picture. As it gets uploaded monitor the Network tab for 'dpr?' endpoint.

 * Click on it. Scroll down to *Request Header*. Copy the entire cookie string.

 * Scroll further down to *Form Data*. Copy the value of fb_dtsg parameter.

6. Call the recognize method with the following parameters.

```python
from fbrecog import FBRecog
path = '1.jpg' # Insert your image file path here
path2 = '2.jpg' # Insert your image file path here
access_token = '#######' # Insert your access token obtained from Graph API explorer here
cookie = '###' # Insert your cookie string here
fb_dtsg = '###' # Insert the fb_dtsg parameter obtained from Form Data here.
# Instantiate the recog class
recog = FBRecog(access_token, cookies, fb_dtsg)
# Recog class can be used multiple times with different paths
print(recog.recognize(path))
print(recog.recognize(path2))
```
## Please star this repo if it helped :)

![star](http://i.imgur.com/Uhx7FOA.png)