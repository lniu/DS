#!/usr/bin/python
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pprint
import sys
from apiclient.discovery import build


import httplib2
from oauth2client.client import SignedJwtAssertionCredentials
service_account_name = '977260187266-p9roi75i6k186si7mrlpmc7fc6qav62g@developer.gserviceaccount.com'
privatekey_file = 'privatekey.txt'

credentials = SignedJwtAssertionCredentials(
          service_account_name,
          file(privatekey_file, 'rb').read(),
          ' '.join([
              'https://www.googleapis.com/auth/prediction',
              'https://www.googleapis.com/auth/devstorage.read_only',
          ])).authorize(httplib2.Http())





# For this example, the API key is provided as a command-line argument.
#api_key = sys.argv[1]

# The apiclient.discovery.build() function returns an instance of an API service
# object that can be used to make API calls. The object is constructed with
# methods specific to the books API. The arguments provided are:
#   name of the API ('books')
#   version of the API you are using ('v1')
#   API key
service = build('prediction', 'v1.6')

# The books API has a volumes().list() method that is used to list books
# given search criteria. Arguments provided are:
#   volumes source ('public')
#   search query ('android')
# The method returns an apiclient.http.HttpRequest object that encapsulates
# all information needed to make the request, but it does not call the API.
request = service.trainedmodels().predict(project='CarPrice', id='977260187266',body={
																		'input':
																		{
																			'csvInstance':
																			[
																				30000,"Buick","Century","Sedan 4D","Sedan",6,3.1,4,1,1,1
																			],
																		},
																		})

# The execute() function on the HttpRequest object actually calls the API.
# It returns a Python object built from the JSON response. You can print this
# object or refer to the Books API documentation to determine its structure.
response = request.execute(credentials)
pprint.pprint(response)

# Accessing the response like a dict object with an 'items' key returns a list
# of item objects (books). The item object is a dict object with a 'volumeInfo'
# key. The volumeInfo object is a dict with keys 'title' and 'authors'.
print 'Found %d as price:' % len(response["outputvalue"])
#for book in response.get('items', []):
  #print 'Title: %s, Authors: %s' % (
    #book['volumeInfo']['title'],
    #book['volumeInfo']['authors'])