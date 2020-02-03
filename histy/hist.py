#!/usr/bin/env python
from argparse import ArgumentParser
import fileinput
from typing import Optional, Dict
from datetime import datetime, timedelta
import re

MATCH = '\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d'
MAX_WIDTH = 100

def process_line(line: str) -> Optional[datetime]:

    result = re.search(MATCH, line)
    if result:
        timestamp = result.group()
        t = datetime.fromisoformat(timestamp)
        return t
    else:
        return None


def generate_histogram(hist: Dict) -> None:
    maximum = 0
    for value in hist.values():
        if value > maximum:
            maximum = value

    print("Histogram:")
    for k, v in hist.items():
        hash_count = int(v / maximum * float(MAX_WIDTH))
        print(k.isoformat(), " : ", "#" * hash_count, v)


def main():
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
    generate_histogram(hist)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--bucket_time_s', '-b', help='bucket duration in seconds')
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    args = parser.parse_args()
    bucket_time_s = int(args.bucket_time_s)
    lines = fileinput.input(files=args.files if len(args.files) > 0 else ('-', ))
    main()

