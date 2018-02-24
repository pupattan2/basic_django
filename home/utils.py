import requests


def whoapi_check_domain_taken(domain, apikey):
    r = requests.get('https://in.godaddy.com/dpp/find?checkAvail=1&tmskey=&domainToCheck=radical', verify=False)

    if r.status_code == 200:
        data = r.text
        data = data.encode("utf-8")
        if "Your domain is available" in data:
            print "Here"
    else:
        raise Exception('unexpected status code %d' % r.status_code)

if __name__ == "__main__":
    print whoapi_check_domain_taken('pulakpattanayak.com', 'demokey')