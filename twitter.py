class twitter():
    class Installer:
        def __init__(self):
            try:
                def title():
                    import os
                    os.system(
                        'title TPCT Twitter BOT V.1' if os.name == 'nt' else '\x1b]2; TPCT Twitter BOT V.1 \x07')

                title()

                def cls():
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')

                cls()
                self.coder = """
       _____ ____   ____ _____   _____          _____   ____   ___ _____
      |_   _|  _ \ / ___|_   _| |_   _|_      _|_   _| | __ ) / _ \_   _|
        | | | |_) | |     | |     | | \ \ /\ / / | |   |  _ \| | | || |
        | | |  __/| |___  | |     | |  \ V  V /  | |   | |_) | |_| || |
        |_| |_|    \____| |_|     |_|   \_/\_/   |_|   |____/ \___/ |_|
              My FB => https://www.facebook.com/taylor.ackerley.9
                     My Github => https://github.com/TPCT         """
                print(self.coder)
                if self.network_checker():
                    self.Admin_Rights()
                    self.Import_Checker()
                    self.PhantomJs()
                else:
                    import os
                    print('[-] Network Is Not Connected. System will exit')
                    os._exit(1)
                pass
            except KeyboardInterrupt:
                import os
                os._exit(1)
            except:
                pass

        def network_checker(self):
            import requests
            try:
                response = requests.get('https://www.google.com')
                return True
            except requests.exceptions.ConnectionError:
                return False
            except KeyboardInterrupt:
                import os
                os._exit(1)
            except:
                pass

        def Admin_Rights(self):
            import os, sys, platform
            try:
                if str(platform.system()).lower().startswith('linux'):
                    open('/etc/Mod', 'w+')
                    os.unlink('/etc/Mod')
                elif str(platform.system()).lower().startswith('windows'):
                    open('c:/Mod', 'w+')
                    os.unlink('c:/Mod')
                else:
                    open('/etc/Mod', 'w+')
                    os.unlink('/etc/Mod')
            except KeyboardInterrupt as e:
                os._exit(1)
            except Exception as e:
                e = e.args
                if e[0] == 13:
                    print('[+] Sorry You Need To Use Script As Admin Script Will Exit')
                    os._exit(1)
                else:
                    pass

        def Import_Checker(self):
            try:
                try:
                    __import__('imp').find_module('requests')
                except ImportError:
                    import pip
                    pip.main(['install', 'requests'])
                    pass
                except Exception as e:
                    pass
                try:
                    __import__('imp').find_module('pickle')
                except ImportError:
                    import pip
                    pip.main(['install', 'pickle'])
                    pass
                except Exception as e:
                    pass
                try:
                    __import__('imp').find_module('selenium')
                except ImportError:
                    import pip
                    pip.main(['install', 'selenium'])
                    pass
                except Exception as e:
                    pass
            except KeyboardInterrupt:
                import os
                os._exit(1)
            except Exception as e:
                print('[+] something went error => '+ e.args)
                import os
                os._exit(1)

        def PhantomJs(self):
            import os, zipfile, requests, platform, sys, tarfile
            try:
                if str(platform.system()).lower().startswith('windows'):
                    exists = False
                    print('[+] Checking Phantomjs. Waiting')
                    for file in os.listdir("c:\\"):
                        if (file.lower().startswith('phantomjs')) and os.path.isdir('c:\\' + file):
                            exists = True
                            self.path = 'c:\\' + file + '\\bin\phantomjs'
                            break
                        else:
                            exists = False
                            pass
                    if exists:
                        print('[+] Checking Phantomjs. Exists')
                        pass
                    elif os.path.exists('c:\phantomjs-win.zip'):
                        with zipfile.ZipFile('c:\phantomjs-win.zip', 'r') as zp:
                            print('[+] Extracting PhantomJs. Started')
                            zp.extractall("c:\\")
                            zp.close()
                            print('[+] Extracting PhantomJs. Done')
                            for file in os.listdir("c:\\"):
                                if (file.lower().startswith('phantomjs')) and os.path.isdir('c:\\' + file):
                                    self.path = 'c:\\' + file + '\\bin\phantomjs'
                                    break
                                else:
                                    pass
                        pass
                    else:
                        print("[+] Phantomjs doesn't exist, Program will Download it")
                        with open('c:\phantomjs-win.zip', 'wb') as file:
                            print("[+] Phantomjs Downloading. Started")
                            data = requests.get(
                                'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip')
                            length = data.headers.get('content-length')
                            if length is None:
                                file.write(data.content)
                            else:
                                dl = 0
                                length = int(length)
                                for M in data.iter_content():
                                    dl += len(M)
                                    file.write(M)
                                    done = int(50 * dl / length)
                                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                                    sys.stdout.flush()
                                    print("[+] Phantomjs Downloading. Done")
                                    pass
                        with zipfile.ZipFile('c:\phantomjs-win.zip', 'r') as zp:
                            print('[+] Extracting PhantomJs. Started')
                            zp.extractall("c:\\")
                            print('[+] Extracting PhantomJs. Done')
                            for file in os.listdir("c:\\"):
                                if (file.lower().startswith('phantomjs')) and os.path.isdir('c:\\' + file):
                                    self.path = 'c:\\' + file + '\\bin\phantomjs.exe'
                                    break
                                else:
                                    pass
                        pass
                        pass
                elif str(platform.system()).lower().startswith('linux'):
                    exists = False
                    print('[+] Checking Phantomjs. Waiting')
                    for file in os.listdir("\\usr\\share\\bin"):
                        if (file.lower().startswith('phantomjs')) and os.path.isdir('\\usr\share\\bin\\' + file):
                            exists = True
                            self.path = '\\usr\share\\bin\\' + file + '\\bin\phantomjs'
                            break
                        else:
                            exists = False
                            pass
                    if exists:
                        print('[+] Checking Phantomjs. Exists')
                        pass
                    elif os.path.exists('\\usr\share\\bin\phantomjs-Linux.tar.bz2'):
                        with tarfile.open('\\usr\share\\bin\phantomjs-Linux.tar.bz2', 'r:bz2') as tar:
                            print('[+] Extracting PhantomJs. Started')
                            tar.extractall('\\usr\share\\bin\\')
                            tar.close()
                            for file in os.listdir("\\usr\\share\\bin"):
                                if (file.lower().startswith('phantomjs')) and os.path.isdir(
                                                '\\usr\share\\bin\\' + file):
                                    self.path = '\\usr\share\\bin\\' + file + '\\bin\phantomjs'
                                    break
                                else:
                                    pass
                            print('[+] Extracting PhantomJs. Done')
                        pass
                    else:
                        print("[+] Phantomjs doesn't exist, Program will Download it")
                        with open('\\usr\share\\bin\phantomjs-Linux.tar.bz2', 'wb') as file:
                            print("[+] Phantomjs Downloading. Started")
                            data = requests.get(
                                'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2')
                            length = data.headers.get('content-length')
                            if length is None:
                                file.write(data.content)
                            else:
                                dl = 0
                                length = int(length)
                                for M in data.iter_content():
                                    dl += len(M)
                                    file.write(M)
                                    done = int(50 * dl / length)
                                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                                    sys.stdout.flush()
                                    print("[+] Phantomjs Downloading. Done")
                                    pass
                            with tarfile.open('\\usr\share\\bin\phantomjs-Linux.tar.bz2', 'r:bz2') as tar:
                                print('[+] Extracting PhantomJs. Started')
                                tar.extractall('\\usr\share\\bin\\')
                                tar.close()
                                for file in os.listdir("\\usr\\share\\bin"):
                                    if (file.lower().startswith('phantomjs')) and os.path.isdir(
                                                    '\\usr\share\\bin\\' + file):
                                        self.path = '\\usr\share\\bin\\' + file + '\\bin\phantomjs'
                                        break
                                    else:
                                        pass
                                print('[+] Extracting PhantomJs. Done')
                            pass
                        pass
                    pass
                else:
                    print("[+] sorry mac os Can't be handled. system will exit")
                    os._exit(1)
                    pass
            except KeyboardInterrupt:
                import os
                os._exit(1)
            except Exception as e:
                print('[-] something went wrong => '+e.args)

    class main:
        def __init__(self):
            try:
                self.coder = """
       _____ ____   ____ _____   _____          _____   ____   ___ _____
      |_   _|  _ \ / ___|_   _| |_   _|_      _|_   _| | __ ) / _ \_   _|
        | | | |_) | |     | |     | | \ \ /\ / / | |   |  _ \| | | || |
        | | |  __/| |___  | |     | |  \ V  V /  | |   | |_) | |_| || |
        |_| |_|    \____| |_|     |_|   \_/\_/   |_|   |____/ \___/ |_|
                My FB => https://www.facebook.com/taylor.ackerley.9
                        My Github => https://github.com/TPCT
                          """
                self.dic = None
                def title():
                    import os
                    os.system(
                        'title TPCT Twitter BOT V.1' if os.name == 'nt' else '\x1b]2; TPCT Twitter BOT V.1 \x07')
                title()
                def cls():
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                cls()
                def loc():
                    import os, platform
                    if str(platform.system()).lower().startswith('windows'):
                        for file in os.listdir("c:\\"):
                            if (file.lower().startswith('phantomjs')) and os.path.isdir('c:\\' + file):
                                return 'c:\\' + file + '\\bin\phantomjs'
                            else:
                                pass
                    elif str(platform.system()).lower().startswith('linux'):
                        for file in os.listdir("\\usr\share\\bin\\"):
                            if (file.lower().startswith('phantomjs')) and os.path.isdir('\\usr\share\\bin\\' + file):
                                return '\\usr\share\\bin\\' + file + '\\bin\phantomjs'
                            else:
                                pass
                    else:
                        os._exit(1)
                self.pjs = loc()
                self.tweet = ''
                self.Start()
                pass
            except KeyboardInterrupt:
                import os
                os._exit(1)
            except Exception as e:
                print('[-] something went wrong => '+e.args)

        def readersplitter(self, path):
            self.dic = {}
            import os, time
            try:
                if os.path.isfile(path):
                    with open(path, 'r') as file:
                        for line in file.readlines():
                            try:
                                self.dic[line.split(':')[0]] = line.split(':')[1]
                            except:
                                pass
                        pass
                pass
            except KeyboardInterrupt:
                os._exit(1)
            except Exception as e:
                print('[-] something went wrong => '+e.args)

        def twitter(self):
            try:
                for (ac, pw) in self.dic.items():
                    from selenium import webdriver
                    browser = webdriver.PhantomJS(self.pjs)
                    browser.get('http://m.twitter.com/login')
                    browser.find_element_by_id('session[username_or_email]').send_keys(ac)
                    browser.find_element_by_id('session[password]').send_keys(pw)
                    try:
                        browser.find_element_by_class_name('message')
                        print('[+][Failed] Invalid Username or Password. [' + (ac + ':' + pw).rstrip() + ']')
                        continue
                    except KeyboardInterrupt:
                        import os
                        os._exit(1)
                    except:
                        browser.get('https://m.twitter.com/compose/tweet')
                        browser.find_element_by_name('tweet[text]').send_keys(self.tweet)
                        browser.find_element_by_name('commit').click()
                        print('[+][Done] Tweeted [' + (ac + ':' + pw).rstrip() + ']')
                    pass
            except KeyboardInterrupt:
                import os
                os._exit(1)
            except Exception as e:
                print('[-] something went wrong => '+e.args)

        def Start(self):
            import os, time
            try:
                while True:
                    def cls():
                        os.system('cls' if os.name == 'nt' else 'clear')
                    cls()
                    print(self.coder)
                    path = input('[+] Please Enter Acc:Pass list Path => ')
                    if os.path.isfile(path):
                        tweet = input('[+] Please Enter Tweet To Share => ')
                        if str(tweet).strip().__len__() > 0:
                            self.readersplitter(path)
                            self.tweet = tweet
                            self.twitter()
                            print('[+] Done. This Script Will be resumed after 10 secs.')
                            time.sleep(10)
                        else:
                            print('[-] Please Enter Valid Tweet To Share => ')
                            time.sleep(1)
                            continue
                    else:
                        print('[-] Please Enter Valid Path To Continue => ')
                        time.sleep(1)
                        continue
                pass
            except KeyboardInterrupt as e:
                os._exit(1)
            except Exception as e:
                print('[-] something went wrong => '+e.args)

    def __init__(self):
        self.Installer()
        self.main()


twitter()
