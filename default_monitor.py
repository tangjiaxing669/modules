#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "Jason Tom"

import sys
from datetime import datetime
from collections import defaultdict
import psutil

class DefaultMonitor():
    '''
    method: cpu_per_info,
            cpu_stats_info,
            cpu_times_per_all_info,
            cpu_times_per_single_info,
            dick_usage_info,
            disk_io_count_all_info,
            disk_io_count_single_info,
            disk_part_info,
            get_pids,
            mem_info,
            net_connect_info,
            net_if_addr_info,
            net_if_stat_info,
            net_io_count_all_info,
            net_io_count_single_info,
            pid_info,
            swap_info,
            system_boot_time_info,
            user_info,
            zombies_info
    '''
    def __init__(self):
        pass

    def cpu_times_per_all_info(self):
        '''
        Note: Get details of the entire CPU.
        cpu_times_per_all_dict:
        :return: dict type
        {
            'user':value,
            'nice':value,
            'system':value,
            'idle':value,
            'iowait':value,
            'irq':'value,
            'softirq':value,
            'steal':value,
            'guest':value,
            'guest_nice':value
        }
        '''
        cpu_times_per_all_dict = dict()
        cpu_times_per = psutil.cpu_times_percent(interval=1, percpu=False)
        cpu_times_per_all_dict['user'] = cpu_times_per.user
        cpu_times_per_all_dict['nice'] = cpu_times_per.nice
        cpu_times_per_all_dict['system'] = cpu_times_per.system
        cpu_times_per_all_dict['idle'] = cpu_times_per.idle
        cpu_times_per_all_dict['iowait'] = cpu_times_per.iowait
        cpu_times_per_all_dict['irq'] = cpu_times_per.irq
        cpu_times_per_all_dict['softirq'] = cpu_times_per.softirq
        cpu_times_per_all_dict['steal'] = cpu_times_per.steal
        cpu_times_per_all_dict['guest'] = cpu_times_per.guest
        cpu_times_per_all_dict['guest_nice'] = cpu_times_per.guest_nice
        return cpu_times_per_all_dict

    def cpu_times_per_single_info(self):
        '''
        Note: Get details of the single CPU
        cpu_times_per_single_dict:
        :return:  dict type
        {
            'cpu_0':[user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice],
            'cpu_1':[user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice],
            'cpu_2':[user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice],
            'cpu_3':[user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice]
            ......
        }
        '''
        cpu_times_per_single_dict = defaultdict(list)
        cpu_times_per_single = psutil.cpu_times_percent(interval=1, percpu=True)
        j = 0
        for i in cpu_times_per_single:
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.user)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.nice)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.system)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.idle)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.iowait)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.irq)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.softirq)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.steal)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.guest)
            cpu_times_per_single_dict['cpu_' + str(j)].append(i.guest_nice)
            j += 1
        return cpu_times_per_single_dict

    def cpu_per_info(self):
        '''
        Note: The percentage of single CPU.
        cpu_per_dict
        :return: dict type
        {cpu_per_list : [value]}
        '''
        cpu_per_dict = dict()
        cpu_per_dict['cpu_per_list'] = psutil.cpu_percent(interval=1, percpu=True)
        return cpu_per_dict

    def cpu_stats_info(self):
        '''
        Note: Get stats of CPU
        cpu_stats_dict:
        :return: dict type
        {
            'ctx_switches': value,
            'interrupts': value,
            'soft_interrupts': value,
            'syscalls':value
        }
        '''
        cpu_stats_dict = dict()
        cpu_stats = psutil.cpu_stats()
        cpu_stats_dict['ctx_switches'] = cpu_stats.ctx_switches
        cpu_stats_dict['interrupts'] = cpu_stats.interrupts
        cpu_stats_dict['soft_interrupts'] = cpu_stats.soft_interrupts
        cpu_stats_dict['syscalls'] = cpu_stats.syscalls
        return cpu_stats_dict

    def mem_info(self):
        '''
        Note: Get memory of system.
        mem_info_dict:
        :return: dict type
        {
            'total':value,
            'available':value,
            'percent':value,
            'used':value,
            'free':value,
            'active':value,
            'inactive':value,
            'buffers':value,
            'cached':value,
            'shared':value
        }
        '''
        mem_info_dict = dict()
        vir_mem_info = psutil.virtual_memory()
        mem_info_dict['total'] = vir_mem_info.total
        mem_info_dict['available'] = vir_mem_info.available
        mem_info_dict['percent'] = vir_mem_info.percent
        mem_info_dict['used'] = vir_mem_info.used
        mem_info_dict['free'] = vir_mem_info.free
        mem_info_dict['active'] = vir_mem_info.active
        mem_info_dict['inactive'] = vir_mem_info.inactive
        mem_info_dict['buffers'] = vir_mem_info.buffers
        mem_info_dict['cached'] = vir_mem_info.cached
        mem_info_dict['shared'] = vir_mem_info.shared
        return mem_info_dict

    def swap_info(self):
        '''
        Note: Get memory of swap.
        swap_info_dict:
        :return: dict type
        {
            'total':value,
            'used':value,
            'free':value,
            'percent':value,
            'sin':value,
            'sout':value
        }
        '''
        swap_info_dict = dict()
        swap_info_dict['total'] = psutil.swap_memory().total
        swap_info_dict['used'] = psutil.swap_memory().used
        swap_info_dict['free'] = psutil.swap_memory().free
        swap_info_dict['percent'] = psutil.swap_memory().percent
        swap_info_dict['sin'] = psutil.swap_memory().sin
        swap_info_dict['sout'] = psutil.swap_memory().sout
        return swap_info_dict

    def disk_part_info(self):
        '''
        Note: Get mount info for system partition.
        disk_part_dict:
        :return: dict type
        {device: [mountpoint, fstype, opts]}
        '''
        disk_part_dict = defaultdict(list)
        disk_part = psutil.disk_partitions()
        for i in disk_part:
            disk_part_dict[i.device].append(i.mountpoint)
            disk_part_dict[i.device].append(i.fstype)
            disk_part_dict[i.device].append(i.opts)
        return disk_part_dict

    def disk_usage_info(self):
        '''
        Note: Get dist usage for system mountpoint.
        disk_usage_dict
        :return: dict type
        {
            mountpoint: [total, used, free, percent]
            ......
        }
        '''
        disk_usage_dict = defaultdict(list)
        disk_usage = psutil.disk_partitions()
        for i in disk_usage:
            disk_usage_dict[i.device].append(psutil.disk_usage(i.mountpoint).total)
            disk_usage_dict[i.device].append(psutil.disk_usage(i.mountpoint).used)
            disk_usage_dict[i.device].append(psutil.disk_usage(i.mountpoint).free)
            disk_usage_dict[i.device].append(psutil.disk_usage(i.mountpoint).percent)
        return disk_usage_dict

    def disk_io_count_all_info(self):
        '''
        Note: Get dick IO of all
        disk_io_count_all_dict
        :return: dick type
        {
        'read_count':value,
        'write_count':value,
        'read_bytes':value,
        'write_bytes':value,
        'read_time':value,
        'write_time':value,
        'read_merged_count':value,
        'write_merged_count':value,
        'busy_time':value
        }
        '''
        disk_io_count_all_dict = dict()
        disk_io_count_all = psutil.disk_io_counters()
        disk_io_count_all_dict['read_count'] = disk_io_count_all.read_count
        disk_io_count_all_dict['write_count'] = disk_io_count_all.write_count
        disk_io_count_all_dict['read_bytes'] = disk_io_count_all.read_bytes
        disk_io_count_all_dict['write_bytes'] = disk_io_count_all.write_bytes
        disk_io_count_all_dict['read_time'] = disk_io_count_all.read_time
        disk_io_count_all_dict['write_time'] = disk_io_count_all.write_time
        disk_io_count_all_dict['read_merged_count'] = disk_io_count_all.read_merged_count
        disk_io_count_all_dict['write_merged_count'] = disk_io_count_all.write_merged_count
        disk_io_count_all_dict['busy_time'] = disk_io_count_all.busy_time
        return disk_io_count_all_dict

    def disk_io_count_single_info(self):
        '''
        Note: Get IO for single partition.
        disk_io_count_single_dict:
        :return: dict type
        {
            device:[real_count, write_count, read_bytes, write_bytes, read_time, write_time, read_merged_count, write_merged_count, busy_time]
            ......
        }
        '''
        disk_io_count_single_dict = defaultdict(list)
        disk_io_count_single = psutil.disk_io_counters(perdisk=True)
        for i in disk_io_count_single:
            disk_io_count_single_dict[i].append(disk_io_count_single[i].read_count)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].write_count)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].read_bytes)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].write_bytes)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].read_time)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].write_time)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].read_merged_count)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].write_merged_count)
            disk_io_count_single_dict[i].append(disk_io_count_single[i].busy_time)
        return disk_io_count_single_dict

    def net_io_count_all_info(self):
        '''
        Note: Get net IO for all.
        net_io_count_all_dict:
        :return: dict type
        {
            'bytes_sent':value,
            'bytes_recv':value,
            'packets_sent':value,
            'packets_recv':value,
            'errin':value,
            'errout':value,
            'dropin':value,
            'dropout':value
        }
        '''
        net_io_count_all_dict = dict()
        net_io_count_all = psutil.net_io_counters()
        net_io_count_all_dict['bytes_sent'] = net_io_count_all.bytes_sent
        net_io_count_all_dict['bytes_recv'] = net_io_count_all.bytes_recv
        net_io_count_all_dict['packets_sent'] = net_io_count_all.packets_sent
        net_io_count_all_dict['packets_recv'] = net_io_count_all.packets_recv
        net_io_count_all_dict['errin'] = net_io_count_all.errin
        net_io_count_all_dict['errout'] = net_io_count_all.errout
        net_io_count_all_dict['dropin'] = net_io_count_all.dropin
        net_io_count_all_dict['dropout'] = net_io_count_all.dropout
        return net_io_count_all_dict

    def net_io_count_single_info(self):
        '''
        Note: Get net IO for single nic.
        net_io_count_single_dict:
        :return: dict type
        {
            nic_name: [bytes_sent, bytes_recv, packets_sent, packets_recv, errin, errout, dropin, dropout]
            ......
        }
        '''
        net_io_count_single_dict = defaultdict(list)
        net_io_count_single = psutil.net_io_counters(pernic=True)
        for i in net_io_count_single:
            net_io_count_single_dict[i].append(net_io_count_single[i].bytes_sent)
            net_io_count_single_dict[i].append(net_io_count_single[i].bytes_recv)
            net_io_count_single_dict[i].append(net_io_count_single[i].packets_sent)
            net_io_count_single_dict[i].append(net_io_count_single[i].packets_recv)
            net_io_count_single_dict[i].append(net_io_count_single[i].errin)
            net_io_count_single_dict[i].append(net_io_count_single[i].errout)
            net_io_count_single_dict[i].append(net_io_count_single[i].dropin)
            net_io_count_single_dict[i].append(net_io_count_single[i].dropout)
        return net_io_count_single_dict

    def net_if_addr_info(self):
        '''
        Note: Get info for single nic.
        net_if_addrs_dict:
        :return: dict type
        {
            nic_name:{
                        nic_family: [address, netmask, broadcast, ptp]
                        ......
                     },
            nic_name:{
                        nic_family: [address, netmask, broadcast, ptp]
                        ......
                     }
            ......
        }
        '''
        net_if_addrs_dict = defaultdict(list)
        net_if_addrs = psutil.net_if_addrs()
        for i in net_if_addrs:
            net_if_addrs_dict[i] = defaultdict(list)
            for j in net_if_addrs[i]:
                net_if_addrs_dict[i][j.family].append(j.address)
                net_if_addrs_dict[i][j.family].append(j.netmask)
                net_if_addrs_dict[i][j.family].append(j.broadcast)
                net_if_addrs_dict[i][j.family].append(j.ptp)
        return net_if_addrs_dict

    def net_if_stat_info(self):
        '''
        Note: Get nic info.
        net_if_stat_dict:
        :return: dict type
        {
            nic_name: [isup, duplex, speed, mtu]
            ......
        }
        '''
        net_if_stat_dict = defaultdict(list)
        net_if_stat = psutil.net_if_stats()
        for i in net_if_stat:
            net_if_stat_dict[i].append(net_if_stat[i].isup)
            net_if_stat_dict[i].append(net_if_stat[i].duplex)
            net_if_stat_dict[i].append(net_if_stat[i].speed)
            net_if_stat_dict[i].append(net_if_stat[i].mtu)
        return net_if_stat_dict

    def net_connect_info(self):
        '''
        Note: Get system network connections.
        net_connect_dict:
        :return: dict type
        {
            'fd':values,
            'family':values,
            'type':values,
            'laddr':values,     # It's tuple
            'raddr':values,     # It's tuple
            'status':values,
            'pid':values
        }
        '''
        flag = 0
        net_connect_dict = defaultdict(list)
        net_connect = psutil.net_connections()
        for i in net_connect:
            net_connect_dict[flag].append(i.fd)
            net_connect_dict[flag].append(i.family)
            net_connect_dict[flag].append(i.type)
            net_connect_dict[flag].append(i.laddr)
            net_connect_dict[flag].append(i.raddr)
            net_connect_dict[flag].append(i.status)
            net_connect_dict[flag].append(i.pid)
            flag += 1
        return net_connect_dict

    def user_info(self):
        '''
        Note: Get user info for login.
        user_info_dict:
        :return: dict type
        {
            login_terminal: [username, host, started]
            ......
        }
        '''
        user_info_dict = defaultdict(list)
        user_judge = psutil.users()
        for i in user_judge:
            user_info_dict[i.terminal].append(i.name)
            user_info_dict[i.terminal].append(i.host)
            user_info_dict[i.terminal].append(datetime.fromtimestamp(i.started).strftime("%Y-%m-%d %H:%M:%S"))
        return user_info_dict

    def system_boot_time_info(self):
        '''
        Note: Get uptime for system.
        system_boot_time_dict:
        :return: dict type
        {
            'system_boot_time': value
        }
        '''
        system_boot_time_dict = dict()
        system_boot_time = psutil.boot_time()
        system_boot_time_dict['system_boot_time'] = datetime.fromtimestamp(system_boot_time).strftime("%Y-%m-%d %H:%M:%S")
        return system_boot_time_dict

    def get_pids(self):
        '''
        Note: Get system process pid.
        :return: list type
        [pids......]
        '''
        return psutil.pids()

    def pid_info(self, pid=None):
        '''
        Note: Get info for a pid
        :param pid: a pid number
        :return: dict type
        {
            'p_name':value,
            'p_exe':value,
            'p_cwd':value,
            'p_status':value,
            'p_create_time':value,
            'puids':[real, effective, saved],
            'pgids':[real, effective, saved],
            'cpu_times':[user, system, children_user, children_system],
            'p_cpu_affinity':[value, ...],
            'p_mem_per':value,
            'p_io_counters':[read_count, write_count, read_bytes, write_bytes],
            'p_connections':value,
            'p_num_threads':value
        }
        '''
        if not isinstance(pid, int):
            raise Exception('Do not have process for this pid {!r}.'.format(pid))
        pid_info_dict = defaultdict(list)
        try:
            p = psutil.Process(pid)
        except psutil.NoSuchProcess as err:
            print(err)
            sys.exit()
        p_uids = p.uids()
        p_gids = p.gids()
        p_cpu_times = p.cpu_times()
        p_io_counter = p.io_counters()
        pid_info_dict['p_name'] = p.name()
        pid_info_dict['p_exe'] = p.exe()
        try:
            pid_info_dict['p_cwd'] = p.cwd()
        except psutil.NoSuchProcess:
            pid_info_dict['p_cwd'] = "None"
        pid_info_dict['p_status'] = p.status()
        pid_info_dict['p_create_time'] = datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
        pid_info_dict['puids'].append(p_uids.real)
        pid_info_dict['puids'].append(p_uids.effective)
        pid_info_dict['puids'].append(p_uids.saved)
        pid_info_dict['pgids'].append(p_gids.real)
        pid_info_dict['pgids'].append(p_gids.effective)
        pid_info_dict['pgids'].append(p_gids.saved)
        pid_info_dict['cpu_times'].append(p_cpu_times.user)
        pid_info_dict['cpu_times'].append(p_cpu_times.system)
        pid_info_dict['cpu_times'].append(p_cpu_times.children_user)
        pid_info_dict['cpu_times'].append(p_cpu_times.children_system)
        pid_info_dict['p_cpu_affinity'] = p.cpu_affinity()
        pid_info_dict['p_mem_per'] = p.memory_percent()
        pid_info_dict['p_io_counters'].append(p_io_counter.read_count)
        pid_info_dict['p_io_counters'].append(p_io_counter.write_count)
        pid_info_dict['p_io_counters'].append(p_io_counter.read_bytes)
        pid_info_dict['p_io_counters'].append(p_io_counter.write_bytes)
        pid_info_dict['p_connections'] = p.connections()
        pid_info_dict['p_num_threads'] = p.num_threads()
        return pid_info_dict

    def zombies_info(self):
        '''
        Note: Get zombie process for system.
        zombies
        :return: list type
        [zombie_process_num, ...]
        '''
        zombies = dict()
        for p in psutil.process_iter():
            try:
                if p.status() == psutil.STATUS_ZOMBIE:
                    zombies[p.pid] = p.name()
            except psutil.NoSuchProcess as err:
                print(err)
                sys.exit()
        return zombies
