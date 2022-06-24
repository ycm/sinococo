BIN_ALT = {
    '雨|⻗': '雨',
    '卜|⺊': '⺊',
    '阜|⻖': '⻖',
    '阜|阝': '⻖',
    '玉|⺩': '玉',
    '疋|⺪': '疋',
    '人|𠆢': '人',
    '竹|⺮': '竹',
    '竹|𥫗': '竹',
    '罒|⺲': '罒',
    '羊|⺶': '羊',
    '肉|⺼': '肉',
    '𦫳|⻀': '艸',
    '足|⻊': '足',
    '邑|⻏': '⻏',
}

def make_bin_alt_replacements(s):
    for k, v in BIN_ALT.items():
        s = s.replace(k, v)
        s = s.replace(k[::-1], v)
    return s   