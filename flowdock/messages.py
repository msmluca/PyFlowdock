# coding: utf-8
import requests
import json
from re import match, IGNORECASE

MESSAGES_API_URL = "https://api.flowdock.com/messages"

EMAIL = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
ALPHANUMERIC_UNDERSCORES_WHITESPACE = r'^[a-z0-9_ ]+$'


# "flow_token": "cbc4d9ca8000ad74058724084f929fff",
#   "event": "activity",
#   "author": {
#     "name": "Marty",
#     "avatar": "https://avatars.githubusercontent.com/u/3017123?v=3"
#   },
#   "title": "updated ticket",
#   "external_thread_id": "1234567",
#   "thread": {
#     "title": "Polish the flux capacitor",
#     "body": "The flux capacitor has been in storage for more than 30 years and it needs to be spick and span for the re-launch.",
#     "status": {
#       "color": "green",
#       "value": "open"
#     }
#   }


class MessageAPI(object):
	API_URL = MESSAGES_API_URL

	def __init__(self, flow_token, author, thread_title, thread_body, thread_id, avatar = None):
		self.msg = {'flow_token':flow_token}
		self.msg['event'] = 'activity'

		author = {'name':author, 'avatar' :avatar}
		self.msg['author'] = author

		self.msg['external_thread_id'] = thread_id
		thread = {'title':thread_title, 'body':thread_body}
		self.msg['thread'] = thread

	def __repr__(self):
		return "%s(%s) instance at %s" % (self.__class__.__name__, self.flow_api_token, hex(id(self)))

	def post(self, title):
		new_msg = self.msg.copy()
		new_msg.update({'title':title})

		print(json.dumps(new_msg))
		print(self.API_URL)
		
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

		response = requests.post(self.API_URL, data=json.dumps(new_msg), headers = headers,)
		if not response.ok:
			response.raise_for_status()
		return True


if __name__ == "__main__":
	# Initialize tasks and results object
	inbox = MessageAPI('cbc4d9ca8000ad74058724084f929fff', author='luca', avatar = "https://avatars.githubusercontent.com/u/3017123?v=3",
	 thread_title = 'FTP file download', 
		thread_body='Status of file download', thread_id='jfkdjskafjadskf')
# With required params only
	print(inbox.post('File updated'))