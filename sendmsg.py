import m2ggg_core
import cgi
from google.appengine.api import memcache

def send_msg_continue(key):
	sendinfo=memcache.get('ml_'+key,'msg');
	if sendinfo is not None :
		m2ggg_core.send_more_msg(sendinfo)

form = cgi.FieldStorage()
key = form.getvalue('key')
send_msg_continue(key)	
