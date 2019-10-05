from colorama import Fore
import requests
import urllib3

class checker(object):

    def check(self,filename):
        url="https://www.zalando.it/api/mobile/v3/user/login.json"
        mail = "mail" #mail
        pwd = "pwd" #pwd
        try:
            liner=filename.split('\n',1)[0]
            r = requests.Session() 
            r.headers = {'Content-Type': 'application/json', 'Host': 'www.zalando.it', 'x-device-platform': 'ios', 'x-uuid': '99739728-AE73-4D1D-A9EF-DE8939F5A81B', 'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'zalando/4.43.2 (iPhone; iOS 12.0.1; Scale/2.00)', 'X-Zalando-Mobile-App': '3580f92a4bafb890i', 'x-app-version': '4.43.2', 'X-Advertising-Id': '6E7B11C4-495E-41D3-92FA-8C503D7AFD1A', 'X-Sales-Channel': 'ebf57ebf-e26d-4ebd-8009-6ad519073d2a', 'X-Logged-In': 'false'}
            r.json = = {"deviceLanguage":"it","appdomainId":"15","appVersion":"4.43.2","ts":"1559045756218","password":pwd,"uuid":"99739728-AE73-4D1D-A9EF-DE8939F5A81B","devicePlatform":"ios","email":email,"sig":"a407b83f8e8b1601ee3986ed0b2df6823722374f"}
            banned = '"successful":false'
            result = r.post(url,proxies={'http':'http://'+liner},timeout=(3.05,27))
            if banned in ressult:
                print(Fore.RED+'Error Banned',e)
                return 
        except requests.exceptions.ConnectionError as e:
            print(Fore.RED+'Error',e)
            return e
        except requests.exceptions.ConnectTimeout as e:
            print(Fore.RED+'ERROR! Connection timeout',e)
            return e
        except requests.exceptions.HTTPError as e:
            print(Fore.RED+'Error code',e.code)
            return e.code
        except requests.exceptions.Timeout as e:
            print(Fore.RED+'Error! Connection Timeout!',e)
            return e
        except urllib3.exceptions.ProxySchemeUnknown as e:
            print(Fore.RED+'ERROR',e)
            return e
