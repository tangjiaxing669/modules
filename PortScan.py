#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "Jason Tom"

import sys
import nmap

class PortScann():
    def __init__(self, hosts):
        '''
        Note: Create nmap instance.
        :param hosts: host list, 192.168.1.0/24 www.google.com 192.168.1.* 192.168.1.10-20
        '''
        self.hosts = hosts
        try:
            self.nm = nmap.PortScanner()
        except nmap.PortScannerError:
            print('Nmap not found', sys.exc_info()[0])
            sys.exit()
        except:
            print('Unexpected error:', sys.exc_info()[0])
            sys.exit()
        try:
            self.nm.scan(hosts)
        except Exception as e:
            print('Scan error:'+str(e))

    def get_scan(self):
        '''
        Note: Judge scanner info.
        :return: dict type
        {
            ip:
                'state':'up',
                'hostname':'localhost',
                'protocols':['tcp'...],
                'port':{
                    22:{
                        'state':'open',
                        'reason':'syn-ack',
                        'name':'ssh',
                        ......
                    },
                    3306:{
                        ......
                    }
                }
            },
            ip:{
                ......
            }
        }
        '''
        scan_dict = dict()
        self.host_list = self.nm.all_hosts()
        for host in self.host_list:
            scan_dict[host] = dict()
            scan_dict[host]['state'] = self.nm[host].state()
            scan_dict[host]['hostname'] = self.nm[host].hostname()
            scan_dict[host]['protocols'] = self.nm[host].all_protocols()
            scan_dict[host]['port'] = dict()
            for protocol in self.nm[host].all_protocols():
                for port in self.nm[host][protocol].keys():
                    scan_dict[host]['port'][port] = self.nm[host][protocol][port]
        return scan_dict


if __name__ == '__main__':
    a = PortScann('www.google.com')
    t1 = a.get_scan()
    print(t1)
