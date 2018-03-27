# -*- coding: utf-8 -*-
import smtplib
import time

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


EMAIL_HOST_USER = 'xuyanwei@xxxx.com'
DIAOYU="This is a fishing letter!"
from_addr = 'xuyanwei@xxxx.com'
to_addr = 'xuyanwei@xxxx.com'
_addr = ''
smtp_server = '10.10.10.227'


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def main():
	server = None
	while True:
		try:
			msg = MIMEText(DIAOYU, 'plain', 'utf-8')	
			msg['From'] = _format_addr('SPARKLE <%s>' % from_addr)
			msg['To'] = _format_addr('xuyanwei <%s>' % to_addr)
			msg['Subject'] = Header('Fishing', 'utf-8').encode()
			server = smtplib.SMTP(smtp_server, 25)
			status = server.sendmail(from_addr, [to_addr], msg.as_string())
		except Exception, e:
			raise e
		finally:
			if server is not None:
				server.quit()
		time.sleep(10)
		break

if __name__=="__main__":
	main()

