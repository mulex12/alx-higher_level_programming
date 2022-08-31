#!/usr/bin/python3
def print_sorted_dictionary(m_dict):
    [print("{}: {}".format(k, m_dict[k])) for k in sorted(m_dict)]
