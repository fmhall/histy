#!/usr/bin/env python
from argparse import ArgumentParser
import fileinput
from typing import Optional, Dict
from datetime import datetime, timedelta
import re


MATCH = r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d'
MAX_WIDTH = 70


def process_line(line: str) -> Optional[datetime]:
    result = re.search(MATCH, line)
    if result:
        timestamp = result.group()
        t = datetime.fromisoformat(timestamp)
        return t
    return None


def generate_histogram(hist: Dict) -> None:
    maximum = 1
    for value in hist.values():
        if value > maximum:
            maximum = value

    print("Histogram:")
    for timestamp, count in hist.items():
        hash_count = int(count / maximum * float(MAX_WIDTH))
        print(timestamp.isoformat(), " : ", "#" * hash_count, count)


def get_parser():
    parser = ArgumentParser(description="CLI tool for creating histograms from ISO timestamped logs")
    parser.add_argument('--bucket_time_s', '-b', help='bucket duration in seconds', type=int)
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    return parser


def histy(args):
    bucket_time_s = args['bucket_time_s']
    lines = fileinput.input(files=args['files'] if len(args['files']) > 0 else ('-',))
    hist = dict()
    bucket_start = process_line(next(lines))
    bucket_end = bucket_start + timedelta(seconds=bucket_time_s)
    for line in lines:
        time_stamp = process_line(line)
        if time_stamp:
            while time_stamp > bucket_end:
                hist[bucket_start] = hist.get(bucket_start, 0)
                bucket_start = bucket_end
                bucket_end += timedelta(seconds=bucket_time_s)
            hist[bucket_start] = hist.get(bucket_start, 0) + 1
    return hist


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if not args['bucket_time_s']:
        parser.print_help()
        return

    hist = histy(args)
    generate_histogram(hist)


if __name__ == '__main__':
    command_line_runner()
