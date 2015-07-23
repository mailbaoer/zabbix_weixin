#!/usr/bin/python
# -*-coding:utf-8-*-

import sys;
import urllib;
import urllib2;
import json;
import commands;
import socket;
reload(sys)
sys.setdefaultencoding('utf-8')

# global variables

GATEWAY    = 'https://qyapi.weixin.qq.com/cgi-bin/'
CORPID     = ''
CORPSECRET = ''

def send_weixin(argv):
  url  = ''.join([GATEWAY, 'gettoken?corpid=', CORPID, '&corpsecret=', CORPSECRET])
  req  = urllib2.Request(url)
  res  = urllib2.urlopen(req).read()
  hjson= json.loads(res)

  # need to catch exceptions

  access_token=hjson['access_token']

  url = ''.join([GATEWAY, 'message/send?access_token=', access_token])
  data={
    'touser': '@all',
    'msgtype': 'news',
    'agentid': '0',
    'news': {
      'articles':[
        {
          'title': '主机：'+argv[2]+'报警',
          'description': '详情：'+argv[3]
        }]
     }
  }
  jdata = json.dumps(data,ensure_ascii=False)
  req   = urllib2.Request(url)
  req.add_header('Content-Type', 'application/json')
  res   = urllib2.urlopen(req,jdata)
  res   = res_data.read()
  hjson = json.loads(res)

  # need to catch exceptions

send_weixin(sys.argv)