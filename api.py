from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='AIzaSyA-7-rYaGFHL906uanR6nntBjORNMiynIc')

model = app.models.get('general-v1.3')
image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
print(model.predict([image]))
