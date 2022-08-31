#!/usr/bin/python3
def best_score(m_dict):
    if m_dict and len(m_dict):
        max = list(m_dict.keys())[0]
        for k in m_dict:
            if m_dict[k] > m_dict[max]:
                max = k
        return max
    return None
