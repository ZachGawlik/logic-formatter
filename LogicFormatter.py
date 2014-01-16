#!/usr/bin/env python3
'''Format the given file to use the actual symbols for logical connectives.'''

import sys
import re
import os


def enforce_binary_spacing(text, binary_connectives):
    '''Format all binary connectives to have a space before and after.'''
    for conn in binary_connectives:
        no_leading_space_expr = re.compile(r'(?<=\S)'+conn)
        no_trailing_space_expr = re.compile(conn+r'(?=\S)')
        text = no_leading_space_expr.sub(' ' + conn, text) 
        text = no_trailing_space_expr.sub(conn + ' ', text)
    return text


def replace_symbols(text, substitutions):
    '''Replace symbol representations with the actual symbols.'''
    for conn in substitutions:
        expr = re.compile(conn)
        text = expr.sub(substitutions[conn], text)
    return text


def get_original_text(filename):
    '''Return the contents of the unformatted file.'''
    with open(filename) as f:
        return f.read()


def write_to_file(original_filename, text):
    '''Write the formatted text to a new file with the suffix -Formatted.'''
    new_filename = '-Formatted'.join(os.path.splitext(original_filename))
    with open(new_filename, 'w') as f:
        f.writelines(text)


def handle_input():
    '''Exit program if no filename given or filename is invalid.'''
    if len(sys.argv) != 2:
        sys.exit('Usage: {} file-name'.format(sys.argv[0]))
    elif not os.path.exists(sys.argv[1]):
        sys.exit('Error: {} is an invalid filename '.format(sys.argv[1]))


def main():
    handle_input()
    original_filename = sys.argv[1]
    text = get_original_text(original_filename)

    binary_before = [r'/\\', r'\\/', '<>', '=>', '==']
    binary_after =  [   '∧',    '∨', '⊕',  '→',  '≡']
    binary_connectives_dict = dict(zip(binary_before, binary_after))
    all_connectives_dict = binary_connectives_dict.copy()
    all_connectives_dict[r'~'] = '¬'
    
    formatted_text = replace_symbols(text, all_connectives_dict)
    formatted_text = enforce_binary_spacing(formatted_text, binary_after)

    write_to_file(original_filename, formatted_text)


if __name__ == '__main__':
    main()
