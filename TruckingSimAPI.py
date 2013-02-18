import urllib, urllib2, json

class TruckingSimAPI:
		
	def __init__(self, key):
		self.key = key
	
	def fetch(self, page, query = None):
		# Construct the URL
		url = "http://truckingsim.com/api/" + page + ".php?key=" + self.key
		if query != None:
			equalLoc = query.find("=") + 1 # +1 to account for its own position
			url = url + "&" + query[:equalLoc] + urllib.quote_plus(query[equalLoc]) # So the = isn't encoded aswell
			print url
		try:
			request = urllib2.urlopen(url)
			return json.load(request)
		except urllib2.URLError:
			# Site's down
			return "Error: API could not be reached."
		except ValueError:
			# JSON was empty, so there must be an ERROR:
			return urllib2.urlopen(url).read()
	
	# Search functions
	def search(self, type, query):
		if type = "users":
			page = "searchUsers"
		elif type = "companies":
			page = "searchCompanies"
		return self.fetch(page, "q=" + query)
	
	# Company functions
	def fetchCompany(self, type, query):
		if type = "users":
			page = "searchUsers"
		elif type = "ads":
			page = "companyAd"
		elif type = "finances":
			page = "companyFinances"
		elif type = "contracts":
			page = "companyContracts"
		return self.fetch(page, "company=" + query)
	
	# Misc functions
	def fetchInfo(self, type):
		return self.fetch(type)

	def fetchDistances(self, begin, end):
		return self.fetch("distances", "from=" + begin + "&to=" + end)
