#!/usr/bin/python3
def simple_delete(m_dict, k=""):
    if k in m_dict:
        del m_dict[k]
    return m_dict
