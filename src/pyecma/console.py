from pyecma.semantics import EcmaSemantics
from pyecma.parser import EcmaParser



def run():
    parser = EcmaParser()
    out=parser.parse('1+(2*4)+(3)*3+222*(((4)))', 'expression', semantics=EcmaSemantics())
    import pdb; pdb.set_trace()
    print(out())


def old_run():
    import argparse
    import sys
    from pyecma.parser import main
    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in EcmaParser.rule_list():
                print(r)
            print()
            sys.exit(0)
    parser = argparse.ArgumentParser(description="Simple parser for Ecma.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(args.file, args.startrule, trace=args.trace)