import argparse
import sys

import utils


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', required=True, help='Token file location')
    parser.add_argument('--credentials', required=True, help='File with application credentials location')
    parser.add_argument('--scope', action='append', help='Access permissions to ask')
    parsed = parser.parse_args(args)
    if not parsed.scope:
        parsed.scope = ['https://www.googleapis.com/auth/gmail.send',
                        'https://www.googleapis.com/auth/calendar.readonly']
        print("No scope has been selected, asking permissions for email sending and calendar read only access")
    return parsed


def main():
    parsed = parse_args(sys.argv[1:])
    return utils.get_creds(parsed.token, parsed.credentials, parsed.scope)


if __name__ == "__main__":
    main()
