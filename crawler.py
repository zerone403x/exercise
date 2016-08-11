import urllib2

def fetch(url):
	#add http proxy
	proxy_config = 'http://%s:%s@%s' % ('xzhao031','ZXF403%!@','135.247.130.16:8080')
	proxy_support = urllib2.ProxyHandler({'http':proxy_config})
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	
	#create a http request package
	http_header = {'User-Agent': 'Chrome'}
	http_request = urllib2.Request(url, None, http_header)
	
	print "Start downloading data..."
	http_response = urllib2.urlopen(http_request)
	print "Finish downloading data..."
	
	print http_response.code
	
	print http_response.info()
	
	print "---------Data----------"
	print http_response.read()
	
	#raw_input(".........")
	
if __name__ == "__main__":
	fetch("http://zhuanlan.zhihu.com/bigertech")
	
#proxy 
#135.251.33.15:8080
#135.251.0.190:8080
#135.251.33.31:8080
#135.251.44.61:8080
#135.247.130.16:8080