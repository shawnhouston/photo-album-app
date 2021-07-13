import os
import os
import sys
import boto3
import urllib3
#from flask_restful import Api, Resource, reqparse
from flask import Flask, render_template, request, redirect, send_file, url_for
from s3_methods import list_files, download_file, upload_file

app = Flask(__name__)
#parser = reqparse.RequestParser()


@app.route('/')
def entry_point():
    return render_template('index.html')
'''
@app.route('/validatePassword')
def validatePassword():
    parser.add_argument('secret')
    args = parser.parse_args()
    if args['secret'] == ALBUM_PASSWORD :
        print("pwd matched")
        return redirect("/storage")
    else:
        return "Incorrect Password. Please try again"
'''
@app.route("/storage")
def storage():
    contents = list_files(s3, BUCKET)
    return render_template('storage.html', contents=contents)


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
#        f.save(f.filename)
        upload_file(s3, f.filename, BUCKET)

        return redirect("/storage")


@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = download_file(s3, filename, BUCKET)

        return send_file(output)


if __name__ == '__main__':
    urllib3.disable_warnings()
    UPLOAD_FOLDER = "uploads"
    #BUCKET = "obc-test-noobaa-99ad4f8f-8509-4eb2-b73d-ba6a404ada08"
    BUCKET = os.environ['BUCKET_NAME']
    #ALBUM_PASSWORD = os.environ['ALBUM_PASSWORD']
    # export ENDPOINT_URL=https://s3-openshift-storage.apps.ocp42.ceph-s3.com ; export AWS_ACCESS_KEY_ID=ewXH8ErFOXMlfxqqXWoD ; export AWS_SECRET_ACCESS_KEY=2yMWDOTSvYB0BdAJnYW096cR3hmbnCVeyIhQBqfO ; export BUCKET=obc-test-noobaa-99ad4f8f-8509-4eb2-b73d-ba6a404ada08 
    s3 = boto3.client('s3',
        #endpoint_url='https://s3-openshift-storage.apps.ocp42.ceph-s3.com',
        #aws_access_key_id='ewXH8ErFOXMlfxqqXWoD',
        #aws_secret_access_key='2yMWDOTSvYB0BdAJnYW096cR3hmbnCVeyIhQBqfO', 
#        endpoint_url = os.environ['ENDPOINT_URL'],
        endpoint_url = "https://" + os.environ['BUCKET_HOST'],
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],
#        use_ssl=False,
        verify=False
        )
    
    app.static_folder = 'static'    
    app.run(host='0.0.0.0', port=8080, debug=True)

