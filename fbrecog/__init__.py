from facepy import GraphAPI
import requests
import json


def recognize(path,access_token,cookies,fb_dtsg):
	""" 
	Face recognition using Facebook's recognize method
		Args:
			path : file path of the photo to be processed
			access_token : Facebook user access token
			cookies : Facebook cookies
			fb_dtsg : special Facebook token required for face recognition
		Returns:
			arr : array of recognitions with the name of recognized people and the certainity of each recognition
	"""

	URL = "https://www.facebook.com/photos/tagging/recognition/?dpr=1"
	
	graph = GraphAPI(access_token)
	
	#Uploading the picture to Facebook	
	post_id = graph.post( path = 'me/photos', source = open(path, 'rb'))['id']
	headers = {
			'x_fb_background_state': '1',
			'origin': 'https://www.facebook.com',
			'accept-encoding': 'gzip, deflate, lzma',
			'accept-language': 'en-US,en;q=0.8',
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2723.2 Safari/537.36',			'content-type': 'application/x-www-form-urlencoded',
			'accept': '*/*',
			'referer': 'https://www.facebook.com/',
			'cookie': cookies,
			'dnt': '1',

	}
	
	arr = []
	payload = ""
	
	#Since the POST sometimes returns a blank array, retrying until a payload is obtained
	while not payload:
		data = 'recognition_project=composer_facerec&photos[0]='+post_id+'&target&is_page=false&include_unrecognized_faceboxes=false&include_face_crop_src=true&include_recognized_user_profile_picture=true&include_low_confidence_recognitions=true&__a=1&fb_dtsg='+fb_dtsg
		req = requests.post(URL,data = data,headers=headers)
		payload =  json.loads(req.text.replace('for (;;);',''))['payload']
		if payload:
			break
	
	for recog in payload[0]['faceboxes']:
		name = recog['recognitions']
		if name:
			arr.append({'name':name[0]['user']['name'] , 'certainity' : name[0]['certainty']})
	
	#Deleting the uploaded picture
	graph.delete(path = post_id)

	return arr
