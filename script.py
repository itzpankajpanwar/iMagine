from flask import Flask , render_template ,request
import os
import matplotlib.pyplot as plt
from style_transfer import *
import style_transfer


app = Flask(__name__)
UPLOAD_FOLDER = './static/image/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
style =""
@app.route("/")
def home():
	return render_template("index.html")




@app.route("/success", methods=['POST'])

def upload_file():
			content = request.files['file']
			style = request.form.get('style')
			content.save(os.path.join(app.config['UPLOAD_FOLDER'], 'content.jpg'))
			#load in content and style image
			content = load_image('./static/image/upload/content.jpg') #+content.filename)
		 	#Resize style to match content, makes code easier
			style = load_image('./static/image/s'+ style+'.jpg', shape=content.shape[-2:])
			vgg = model()
			print("-------------------------------------------------------------------")
			target = stylize(content,style,vgg)
			print("-------------------------------------------------------------------")
			x = im_convert(target)
			print("-------------------------------------------------------------------")
			plt.imsave('./static/image/upload/target.png',x)
			print("-------------------------------------------------------------------")
			return render_template('success.html')

							

if __name__ =="__main__":
	app.run(debug=True)
