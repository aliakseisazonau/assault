import click
import json
import sys
from .http import assault
from .stats import Results
from typing import TextIO

@click.command()
@click.option("--requests", '-r', default=500, help="Number of requests")
@click.option("--concurrency", '-c', default=1, help="Number of concurrent requests")
@click.option("--json-file", '-j', default=None, help="Path to output JSON file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    output_file = None
    if json_file:
        try:
            output_file = open(json_file, 'w')
        except:
            print(f"Unable to open file {json_file}")
            sys.exit(1)
    total_time, request_dicts = assault(url, requests, concurrency)
    results = Results(total_time, request_dicts)
    display(results, output_file)

def display(results: Results, json_file: TextIO):
    if json_file:
        json.dump(
            {
                "successful_requests": results.successful_requests(),
                "slowest": results.slowest(),
                "fastest": results.fastest(),
                "total_time": results.total_time,
                "requests_per_minute": results.requests_per_minute(),
                "requests_per_second": results.requests_per_second(),    
            },
            json_file,
        )
        json_file.close()
        print("......Done")
    else:
        print("......Done")
        print("---- Results ----")
        print(f"Successful requests      \t{results.successful_requests()}")
        print(f"Slowest requests         \t{results.slowest()}")
        print(f"Fastest requests         \t{results.fastest()}")
        print(f"Total time               \t{results.total_time}")
        print(f"Requests Per minute      \t{results.requests_per_minute()}")
        print(f"Requests Per second      \t{results.requests_per_second()}")