from postmarker.core import PostmarkClient
postmark = PostmarkClient(server_token='ad09e72a-faa2-4de2-93a4-156c211aad0e')
postmark.emails.send(
  From='ckirkl439@west-mec.org',
  To='ckirkl439@west-mec.org',
  Subject='Postmark test',
  HtmlBody='HTML body goes here'
)