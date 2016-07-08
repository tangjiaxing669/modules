#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "Jason Tom"

import os
import sys
import pycurl
from collections import defaultdict

class Probe_web:
    def __init__(self):
        '''
        Note: Create pycurl instance
        '''
        self.probe = pycurl.Curl()

    def set_opt(self, URL, CONN_TIMEOUT=5, TIMEOUT=5, NOPROGRESS=1, MAX_REDIRS=5, FORBID_REUSE=1, FRESH_CONN=1, DNS_CACHE_TIMEOUT=60):
        '''
        Note: Set options for probe web URL.
        :param URL: Define probe web's url address.
        :param CONN_TIMEOUT: Define connection URL's timeout.
        :param TIMEOUT: Define request URL's timeout.
        :param NOPROGRESS: Define shield download progress.
        :param MAX_REDIRS: Define max connection number for HTTP redirection.
        :param FORBID_REUSE: Forced disconnect request is completed.
        :param FRESH_CONN: Forced judge of new connections, no cache.
        :param DNS_CACHE_TIMEOUT: Define save DNS info time
        :return: None
        '''
        self._URL = URL
        self.probe.setopt(pycurl.URL, self._URL)
        self.probe.setopt(pycurl.CONNECTTIMEOUT, CONN_TIMEOUT)
        self.probe.setopt(pycurl.TIMEOUT, TIMEOUT)
        self.probe.setopt(pycurl.NOPROGRESS, NOPROGRESS)
        self.probe.setopt(pycurl.MAXREDIRS, MAX_REDIRS)
        self.probe.setopt(pycurl.FORBID_REUSE, FORBID_REUSE)
        self.probe.setopt(pycurl.FRESH_CONNECT, FRESH_CONN)
        self.probe.setopt(pycurl.DNS_CACHE_TIMEOUT, DNS_CACHE_TIMEOUT)
        self.HTTP_HEADER_FILE =  open(sys.path[0] + '/PROBE_HEADER', 'wb')
        self.probe.setopt(pycurl.WRITEHEADER, self.HTTP_HEADER_FILE)
        self.HTTP_DATA_FILE = open(sys.path[0] + '/PROBE_DATA', 'wb')
        self.probe.setopt(pycurl.WRITEDATA, self.HTTP_DATA_FILE)

    def commit(self):
        '''
        Note: Commit pycurl.setopt() information.
        :return: None
        '''
        try:
            self.probe.perform()
        except Exception as e:
            print("connection error: " + str(e))
            self.HTTP_HEADER_FILE.close()
            self.HTTP_DATA_FILE.close()
            sys.exit()

    def get_info(self):
        '''
        Note: Get info for probe web
        :return: dict type
        {
            URL: [ http_code,
                   connect_time,
                   pretransfer_time,
                   starttransfer_time,
                   total_time,
                   namelookup_time,
                   size_download,
                   header_size,
                   speed_download,
                   redirect_time
                 ]
        }

        http_code: Connect URL return http code.
        connect_time: Get the time to establish a connection.
        pretransfer_time: Get from establish a connection to ready transfer times.
        starttransfer_time: Get from establish a connection to begin transfer times.
        total_time: Get time for transfer.
        namelookup_time: Get resolve time for DNS.
        size_download: Get size for download data package.
        header_size: Get size for HTTP header.
        speed_download: Get download speed for average.
        redirect_time: Get redirect the amount of time.#
        '''
        self.probe_web_info = defaultdict(list)
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.HTTP_CODE))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.CONNECT_TIME))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.PRETRANSFER_TIME))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.STARTTRANSFER_TIME))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.TOTAL_TIME))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.NAMELOOKUP_TIME))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.SIZE_DOWNLOAD))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.HEADER_SIZE))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.SPEED_DOWNLOAD))
        self.probe_web_info[self._URL].append(self.probe.getinfo(self.probe.REDIRECT_TIME))
        self.HTTP_HEADER_FILE.close()
        self.HTTP_DATA_FILE.close()
        with open(sys.path[0] + '/PROBE_HEADER', 'rb') as header_info:
            self.probe_web_info[self._URL].append(header_info.read())
        return self.probe_web_info

    def cleanup(self):
        if os.path.isfile(sys.path[0] + '/PROBE_HEADER'):
            os.remove(sys.path[0] + '/PROBE_HEADER')

        if os.path.isfile(sys.path[0] + '/PROBE_DATA'):
            os.remove(sys.path[0] + '/PROBE_DATA')

# if __name__ == '__main__':
#     URL = 'http://www.baidu.com'
#     probe_url = Probe_web()
#     probe_url.set_opt(URL)
#     probe_url.commit()
#     probe_info = probe_url.get_info()
#     print('probe_info = > {0}'.format(probe_info))
#     probe_url.cleanup()