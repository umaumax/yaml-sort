#!/usr/bin/env python3

import sys
import yaml
import argparse


def simple_multi_constructor(loader, tag_suffix, node):
    return loader.construct_yaml_map(node)


def genSortedYamlFile(input_filepath, output_filepath, verbose=False):
    with open(input_filepath, mode='r') as input_file:
        # NOTE: for avoiding Secondary Handle:
        # NOTE: (lambda loader, suffix, node: None) -> ignore all
        yaml.add_multi_constructor('!', simple_multi_constructor, Loader=yaml.Loader)
        # SEE: [YAML Ain’t Markup Language \(YAML™\) Version 1\.2]( https://yaml.org/spec/1.2/spec.html#id2782457 )
        # yaml.add_multi_constructor('tag', lambda loader, suffix, node: None)
        yaml.add_multi_constructor('tag', simple_multi_constructor, Loader=yaml.Loader)

        # NOTE: use yaml.Loader not yaml.FullLoader (since FullLoader cannot avoid tags)
        data = yaml.load(input_file, Loader=yaml.Loader)
        if verbose:
            print(data, file=sys.stderr)

        sorted = yaml.dump(data, sort_keys=True)

        with open(output_filepath, mode='w') as output_file:
            output_file.write(sorted)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-filepath', default='/dev/stdout', help='output_filepath')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('input_filepath', help='input file path')
    parser.add_argument('args', nargs='*', help='1st args can overwrite output_filepath')  # any length of args is ok

    args, extra_args = parser.parse_known_args()
    if len(args.args) > 0:
        args.output_filepath = args.args[0]
    genSortedYamlFile(args.input_filepath, args.output_filepath, args.verbose)


if __name__ == '__main__':
    main()
