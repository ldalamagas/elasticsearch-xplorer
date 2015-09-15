#!/usr/bin/python
import argparse
import pprint
from elasticsearch import Elasticsearch

__author__ = 'lefteris'


def create_argument_parser():
    p = argparse.ArgumentParser(description="ElasticSearch Explorer")
    p.add_argument('--port', '-p', default=9200, help="Connect to the given host")
    p.add_argument('--host', '-d', default="localhost", help="Connect to the given port")
    p.add_argument('--list-indices', '-l', default=False, help="List the indices available", action="store_true")
    p.add_argument('--list-index', '-i', help="List available data for the given index")
    p.add_argument('--pretty-print', default=False, help="Connect to the given host", action="store_true")
    p.add_argument('--ssl', "-s", default=False, help="Enable ssl", action="store_true")
    p.add_argument('--ssl-certificates', "-c", help="Path to ssl certificates")
    p.add_argument('--debug', default=False, help="Enable debugging features", action="store_true")
    return p


def print_result(content):
    if arguments.pretty_print:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(content)
    else:
        print(content)


def show_indices():
    es = Elasticsearch([hosts])
    aliases = es.indices.get_aliases()
    for alias in aliases:
        print(alias)


def show_index(index):
    es = Elasticsearch([hosts])
    query = {
        "query": {
            "match_all": {}
        }
    }

    content = es.search(index=index, body=query)
    print_result(content)


if __name__ == '__main__':
    argument_parser = create_argument_parser()
    arguments = argument_parser.parse_args()

    hosts = {
        "host": arguments.host,
        "port": arguments.port
    }

    if arguments.list_indices:
        show_indices()

    if arguments.list_index:
        show_index(arguments.list_index)