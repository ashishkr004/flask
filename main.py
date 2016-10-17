import webapp2
import jinja2
import os
import json
from sets import  Set
import session_handler 
import urllib
import jinja2
import os
import json
from google.appengine.api import urlfetch
# import cloudDbHandler as dbhandler



jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'template')))
class Main(session_handler.BaseSessionHandler):
	def get(self):
		loggedInStatus=self.session.get('loggedIn',False)
		if loggedInStatus==True:
  			userDetails={
  				'userName':self.session['name'],
  				'userMobile':self.session['mobile'],
  				'userEmail':self.session['email']
  			}
			home = jinja_environment.get_template('phir.html')
			self.response.write(home.render(userDetails))
			pass
		else:
			home = jinja_environment.get_template('index.html')
			self.response.write(home.render())
			pass

class How(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('ca.html')
		self.response.write(home.render())
		pass

class adminPanel(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('admin.html')
		self.response.write(home.render())
		pass
		    
class eventInfo(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('eventinfo.html')
		self.response.write(home.render())
		pass

class clubInfo(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('clubinfo.html')
		self.response.write(home.render())
		pass

class AdminUpdate(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('AdminUpdate.html')
		self.response.write(home.render())
		pass

class managerUpdate(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('managerUpdate.html')
		self.response.write(home.render())
		pass 

class second(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('second.html')
		self.response.write(home.render())
		pass

class admin(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('admin.html')
		self.response.write(home.render())
		pass  

class go(session_handler.BaseSessionHandler):
	def get(self):
		value={
				'valBollywood':self.request.get('bollywood'),
				'valChill':self.request.get('chill'),
				'valRock':self.request.get('rock'),
				'valTrance':self.request.get('trance'),
				'valLive':self.request.get('live'),
				'valHouse':self.request.get('house'),
				'valSufi':self.request.get('sufi'),
				'valBass':self.request.get('bass'),
				'valKaraoke':self.request.get('karaoke'),
				'valJazz':self.request.get('jazz'),
				'valDateTime':self.request.get('datetime'),
				'valPlace':self.request.get('place')
		}
		home = jinja_environment.get_template('go.html')
		self.response.write(home.render(value))
		pass  
class phir(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('phir.html')
		self.response.write(home.render())
		pass

class user(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('userlogin.html')
		self.response.write(home.render())
		pass

class admin1(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('admin1.html')
		self.response.write(home.render())
		pass

class artistinfo(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('artistinfo.html')
		self.response.write(home.render())
		pass
class placeinfo(session_handler.BaseSessionHandler):
	def get(self):
		home = jinja_environment.get_template('placeinfo.html')
		self.response.write(home.render())
		pass

class login(session_handler.BaseSessionHandler):
    def post(self):
        url = 'http://catalyst.moovo-967.appspot.com/api/user/login/'
        form_fields = "{\n\"mobile\": \""+self.request.get('login_username')+"\",\n\"password\": \""+self.request.get('password')+"\"\n}"
        result = urlfetch.fetch(url=url,
        payload=form_fields,
        method=urlfetch.POST,
        follow_redirects=False,
        headers={'Content-Type': 'text/plain'}) 
        response = json.loads(result.content)
        if response['success'] == True:
            if response['datasets']['Message'] == 'Login Successful':
                self.session['name'] = response['datasets']['name']
                self.session['mobile'] = response['datasets']['mobile']
                self.session['email'] = response['datasets']['email']
                self.session['loggedIn'] = True
                self.redirect('/loggedIn')
                pass
            elif  response['datasets']['Message'] == 'wrong password':
                self.session['loggedIn'] = False
                self.session['isLoginError'] = True
                self.session['loginError'] = 'Wrong Password'
                self.redirect('/')
                pass
            elif  response['datasets']['Message'] == 'mobile number does not exist':
                self.session['loggedIn'] = False
                self.session['isLoginError'] = True
                self.session['loginError'] = 'mobile number does not exist'
                self.redirect('/')
                pass
        else:
            self.session['loggedIn'] = False
            self.session['isLoginError'] = True
            self.session['loginError'] = 'Unknown Error'
            self.redirect('/')            
            pass

class signup(session_handler.BaseSessionHandler):
    def post(self):
        url = 'http://catalyst.moovo-967.appspot.com/api/user/signup/'
        form_fields = "{\n\"mobile\": \""+self.request.get('phonenum')+"\",\n\"name\": \""+self.request.get('username')+"\",\n\"email\": \""+self.request.get('email')+"\",\n\"password\": \""+self.request.get('pass')+"\"\n}"
        result = urlfetch.fetch(url=url,
        payload=form_fields,
        method=urlfetch.POST,
        follow_redirects=False,
        headers={'Content-Type': 'text/plain'}) 
        response = json.loads(result.content)
        if response['success'] == True:
            if response['datasets'] == 'user added':
                self.session['name'] = self.request.get('username')
                self.session['mobile'] = self.request.get('phonenum')
                self.session['email'] = self.request.get('email')
                self.session['loggedIn'] = True
                self.redirect('/loggedIn')
                pass
            elif  response['datasets'] == 'user already exist':
                self.session['loggedIn'] = False
                self.session['isLoginError'] = True
                self.session['loginError'] = 'user already exist'
                self.redirect('/')
                pass
            elif  response['datasets']['Message'] == 'try again':
                self.session['loggedIn'] = False
                self.session['isLoginError'] = True
                self.session['loginError'] = 'network error'
                self.redirect('/')
                pass
        else:
            self.session['loggedIn'] = False
            self.session['isLoginError'] = True
            self.session['loginError'] = 'Unknown Error'
            self.redirect('/')            
            pass

class loggedIn(session_handler.BaseSessionHandler):
	def get(self):
  		loggedInStatus=self.session.get('loggedIn',False)
  		if loggedInStatus==True:
  			userDetails={
  				'userName':self.session['name'],
  				'userMobile':self.session['mobile'],
  				'userEmail':self.session['email']
  			}
			home = jinja_environment.get_template('phir.html')
			self.response.write(home.render(userDetails))
			pass
		else:
			home = jinja_environment.get_template('index.html')
			self.response.write(home.render())
			pass
        

class logout(session_handler.BaseSessionHandler):
    def get(self):
        self.session['loggedIn'] = False
        self.redirect('/')  


app = webapp2.WSGIApplication([
	('/',Main),
	('/adminPanel',adminPanel),
	('/how',How),
	('/eventInfo',eventInfo),
	('/clubInfo',clubInfo),
	('/AdminUpdate',AdminUpdate),
	('/managerUpdate',managerUpdate),
	('/second',second),
	('/go',go),
	('/phir',phir),
	('/user',user),
	('/admin1',admin1),
	('/artistinfo',artistinfo),
	('/placeinfo',placeinfo),
	('/login',login),
	('/signup',signup),
	('/loggedIn',loggedIn)
], debug=True,
config = session_handler.myconfig_dict)
