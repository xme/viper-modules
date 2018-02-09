# -*- coding: utf-8 -*-
#
# Submit files to a ReversingLabs A1000 appliance
#
# Author: Xavier Mertens <xavier@rootshell.be>
# Copyright: GPLv3 (http://gplv3.fsf.org)
# Fell free to use the code, but please share the changes you've made
#
# Todo
# -
#


from io import BytesIO
import logging
import json

try:
    import requests
    HAVE_REQUESTS = True
except ImportError:
    HAVE_REQUESTS = False

from viper.common.abstracts import Module
from viper.core.session import __sessions__
from viper.core.config import __config__

log = logging.getLogger('viper')

cfg = __config__
cfg.parse_http_client(cfg.a1000)


class A1000(Module):
    cmd = 'a1000'
    description = 'Submit files and retrieve reports from a ReversingLabs A1000 appliance'
    authors = ['Xavier Mertens <xavier@rootshell.be>']

    def __init__(self):
        super(A1000, self).__init__()
        self.parser.add_argument('-s', '--submit', action='store_true', help='Submit file to A1000')
        self.parser.add_argument('-c', '--classification', action='store_true', help='Get classification of current file from A1000')

    def run(self):

        super(A1000, self).run()
        if self.args is None:
            return

        if not HAVE_REQUESTS:
            self.log('error', "Missing dependency, install requests (`pip install requests`)
            return

        if not __sessions__.is_set():
            self.log('error', "No open session")
            return

        if self.args.submit:
            try:
                file = { 'file': BytesIO(__sessions__.current.file.data)}
		data = { 'filename': __sessions__.current.file.name,
                         'tags': 'viper' }

                response = requests.post(
                              '%s/%s' % (cfg.a1000.base_url, '/api/uploads/'),
                              data=data,
                              files=file,
                              headers={'Authorization': 'Token %s' % cfg.a1000.token})
                response = response.json()

                if response['code'] != 201:
                    self.log('error', response['message'])
                    return
                if response['code'] == 201:
                    self.log('info', 'Successfully submitted to A1000, task ID: ' + str(response['detail']['id']))
                    return

            except Exception as e:
                self.log('error', "Failed performing request: {0}".format(e))
                return

        if self.args.classification:
            try:
                response = requests.get(
                              '%s/api/samples/%s/ticloud/' % (cfg.a1000.base_url, __sessions__.current.file.sha1),
                              headers={'Authorization': 'Token %s' % cfg.a1000.token})
		status = response.status_code
                response = response.json()

                if status == 404:
                    self.log('info', 'Sample not found')
                    return
                if status == 200:
                    self.log('info', 'Classification')
                    self.log('item', 'Threat status : %s' % response['threat_status'])
                    self.log('item', 'Threat name   : %s' % response['threat_name'])
                    self.log('item', 'Trust factor  : %d' % response['trust_factor'])
                    self.log('item', 'Threat level  : %d' % response['threat_level'])
                    self.log('item', 'First seen    : %s' % response['first_seen'])
                    self.log('item', 'Last seen     : %s' % response['last_seen'])
                    return

            except Exception as e:
                self.log('error', "Failed performing request: {0}".format(e))
                return
