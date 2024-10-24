import psutil
from datetime import datetime
import pandas as pd
import numpy as np
import argparse
import time
import os


def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024


def get_processes_info():
    # the list the contain all process dictionaries
    processes_p = []
    for process in psutil.process_iter():
        if process.name() == 'fityk.exe':  # fityk already has to be launched for this to work
            # get all process info in one shot
            with process.oneshot():
                # get the process id
                pid = process.pid
                if pid == 0:
                    # System Idle Process for Windows NT, useless to see anyways
                    continue
                # get the CPU usage percentage
                cpu_usage = process.cpu_percent()

                try:
                    # get the memory usage in bytes
                    memory_usage = process.memory_full_info().uss
                except psutil.AccessDenied:
                    memory_usage = 0
                # total process read and written bytes
                io_counters = process.io_counters()
                read_bytes = io_counters.read_bytes
                write_bytes = io_counters.write_bytes

            processes_p.append({
                'pid': pid, 'cpu_usage': cpu_usage, 'memory_usage': memory_usage, 'read_bytes': read_bytes, 'write_bytes': write_bytes,
            })
    return processes_p


def construct_dataframe(processes_p, sort_by_p, descending_p, columns_p):
    # convert to pandas dataframe
    df_p = pd.DataFrame(processes_p)
    # set the process id as index of a process
    df_p.set_index('pid', inplace=True)
    # sort rows by the column passed as argument
    df_p.sort_values(sort_by_p, inplace=True, ascending=not descending_p)
    # pretty printing bytes
    df_p['memory_usage'] = df_p['memory_usage'].apply(get_size)
    df_p['write_bytes'] = df_p['write_bytes'].apply(get_size)
    df_p['read_bytes'] = df_p['read_bytes'].apply(get_size)
    # convert to proper date format
    df_p['create_time'] = df_p['create_time'].apply(datetime.strftime, args=("%Y-%m-%d %H:%M:%S",))
    # reorder and define used columns
    df_p = df_p[columns_p.split(",")]
    return df_p


def create_parser_object():
    parser_p = argparse.ArgumentParser(description="Process Viewer & Monitor")
    parser_p.add_argument("-c", "--columns", help="""Columns to show,
                                                    available are name,create_time,cores,cpu_usage,status,nice,memory_usage,read_bytes,write_bytes,n_threads,username.
                                                    Default is name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,cores.""",
                          default="name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,cores")
    parser_p.add_argument("-s", "--sort-by", dest="sort_by", help="Column to sort by, default is memory_usage .",
                          default="memory_usage")
    parser_p.add_argument("--descending", action="store_true", help="Whether to sort in descending order.")
    parser_p.add_argument("-n", help="Number of processes to show, will show all if 0 is specified, default is 25 .",
                          default=25)
    parser_p.add_argument("-u", "--live-update", action="store_true",
                          help="Whether to keep the program on and updating process information each second",
                          default="-u")
    return parser_p


def parse_arguments(parser_p):
    # parse arguments
    args_p = parser_p.parse_args()
    columns_p = args_p.columns
    sort_by_p = args_p.sort_by
    descending_p = args_p.descending
    n_p = int(args_p.n)
    live_update_p = args_p.live_update
    return columns_p, sort_by_p, descending_p, n_p, live_update_p


def init_sma_10():
    counter_p = 0
    average_array_p = np.asarray([100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    return counter_p, average_array_p


def init_sma_3():
    counter_p = 0
    average_array_p = np.asarray([100, 100, 100])
    return counter_p, average_array_p


def is_fityk_cpu_usage_non_zero(average_array_p, counter_p, live_update_p, sort_by_p, descending_p, columns_p, n_p):
    counter_max = 3
    while live_update_p:
        # get all process info
        processes_p = get_processes_info()
        df_p = construct_dataframe(processes_p, sort_by_p, descending_p, columns_p)
        # clear the screen depending on your OS
        os.system("cls") if "nt" in os.name else os.system("clear")
        if n_p == 0:
            pass
        elif n_p > 0:
            average_array_p[(counter_p % counter_max)] = float(df_p.cpu_usage)
            sma_value_p = average_array_p.mean()
            # print(sma_value_p)
            counter_p += 1
            if counter_p == counter_max:
                counter_p = 0
            if sma_value_p <= 50.0:  # if you use less than 1% cpu on average over 10 checks, stop
                live_update_p = False
                return live_update_p


def monitor_fityk_process():
    # create the parser object
    parser_p = create_parser_object()
    # parse arguments
    columns_p, sort_by_p, descending_p, n_p, live_update_p = parse_arguments(parser_p)
    # initialize counter and array for determining 10 point moving average
    counter_p, average_array_p = init_sma_3()
    # check the process usage of fityk to see if the sma10(cpu_usage) <= 1.0
    is_cpu_usage_nonzero_p = is_fityk_cpu_usage_non_zero(average_array_p, counter_p, live_update_p, sort_by_p, descending_p, columns_p, n_p)
    return is_cpu_usage_nonzero_p


def monitor_fityk_process_V2():
    cpu_usage = 100
    is_fityk_running = False
    for proc in psutil.process_iter():
        if proc.name() == 'fityk.exe':
            # pid = proc.pid
            while cpu_usage > 20:
                cpu_usage = proc.cpu_percent(0.1)
                # print(cpu_usage)
    return is_fityk_running


if __name__ == "__main__":
    monitor_fityk_process_V2()