# Introduction

The purpose of this APP is to demonstrate, what it takes for a developer to interact with OpenShift Container Storage Object Bucket Claim feature and consume Object Storage as a persistent layer.


# Deployment

- Deploy the App
  - `` oc apply -f photo_album_app_on_OCS_OBC.yaml ``

```
$ oc apply -f photo_album_app_on_OCS_OBC.yaml
objectbucketclaim.objectbucket.io/photo-album created
imagestream.image.openshift.io/photo-album created
deploymentconfig.apps.openshift.io/photo-album created
service/photo-album created
route.route.openshift.io/photo-album created
```

This should create an OBC and other stuff needed for the app itself like POD,SVC,ROUTE. Together with OBC, you will also get new secrets and config maps created. The important resources could be listed as
- `` oc get po,svc,route,obc,secret,cm``

At this point your app is ready to be accessed externally. Grab the URL and browse it

- A simple landing page of the app will appear
![](http://gitlab.libvirt8/shouston/openshift-photo-album-app/raw/master/Image-2.jpg)
- When you enter the album, you can upload or view your photos
![](http://gitlab.libvirt8/shouston/openshift-photo-album-app/raw/master/Image-3.png)
- Finally looks like 
![](http://gitlab.libvirt8/shouston/openshift-photo-album-app/raw/master/image-4.jpg)





