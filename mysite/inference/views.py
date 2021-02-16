from django.http import HttpResponse
#import cv2

def index(request):
    return HttpResponse('''
    <form action="upload.php" method="post" enctype="multipart/form-data">
        Select image to upload:
        <input type="file" name="fileToUpload" id="fileToUpload"/>
        <input type="submit" value="Upload Image" name="submit"/>
    </form>''')

def load_model(path):
    pass