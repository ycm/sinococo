import unicodedata as unic

cjk_ranges = [
    (0x4E00,  0x62FF),
    (0x6300,  0x77FF),
    (0x7800,  0x8CFF),
    (0x8D00,  0x9FCC),
    (0x3400,  0x4DBF),
    (0x20000, 0x215FF),
    (0x21600, 0x230FF),
    (0x23100, 0x245FF),
    (0x24600, 0x260FF),
    (0x26100, 0x275FF),
    (0x27600, 0x290FF),
    (0x29100, 0x2A6DF),
    (0x2A700, 0x2B734),
    (0x2B740, 0x2B81D),
    (0x2B820, 0x2CEAF),
    (0x2CEB0, 0x2EBEF),
    (0x2F800, 0x2FA1F),
    (0x30000, 0x3134A), # cjk ext-g
    (0x31c0,  0x31e3), # cjk strokes
    (0x2E80,  0x2EF3), # cjk radical supplement
    (0x2F00,  0x2fdf), # kangxi radicals
    (0x2FF0,  0x2FFB), #ideographic description block
    (0xF900,  0xFAFF) # cjk compatibility ideographs
]

exclusion_ranges = [
    (0x30A1, 0x30FF), # katakana
    (0x3041, 0x309f), # hiragana
    (0x3000, 0x303F) # cjk symbols/punct
]

pinyins = {'a',  'ai',  'an',  'ang',  'ao',  'ba',  'bai',  'ban',  'bang',  'bao',  'bei',  'ben',  'beng',  'bi',  'bian',  'biao',  'bie',  'bin',  'bing',  'bo',  'bu',  'ca',  'cai',  'can',  'cang',  'cao',  'ce',  'cen',  'ceng',  'cha',  'chai',  'chan',  'chang',  'chao',  'che',  'chen',  'cheng',  'chi',  'chong',  'chou',  'chu',  'chua',  'chuai',  'chuan',  'chuang',  'chui',  'chun',  'chuo',  'ci',  'cong',  'cou',  'cu',  'cuan',  'cui',  'cun',  'cuo',  'da',  'dai',  'dan',  'dang',  'dao',  'de',  'dei',  'den',  'deng',  'di',  'dia',  'dian',  'diao',  'die',  'ding',  'diu',  'dong',  'dou',  'du',  'duan',  'dui',  'dun',  'duo',  'e',  'ei',  'en',  'eng',  'er',  'fa',  'fan',  'fang',  'fei',  'fen',  'feng',  'fo',  'fou',  'fu',  'ga',  'gai',  'gan',  'gang',  'gao',  'ge',  'gei',  'gen',  'geng',  'gong',  'gou',  'gu',  'gua',  'guai',  'guan',  'guang',  'gui',  'gun',  'guo',  'ha',  'hai',  'han',  'hang',  'hao',  'he',  'hei',  'hen',  'heng',  'hong',  'hou',  'hu',  'hua',  'huai',  'huan',  'huang',  'hui',  'hun',  'huo',  'ji',  'jia',  'jian',  'jiang',  'jiao',  'jie',  'jin',  'jing',  'jiong',  'jiu',  'ju',  'juan',  'jue',  'jun',  'ka',  'kai',  'kan',  'kang',  'kao',  'ke',  'kei',  'ken',  'keng',  'kong',  'kou',  'ku',  'kua',  'kuai',  'kuan',  'kuang',  'kui',  'kun',  'kuo',  'la',  'lai',  'lan',  'lang',  'lao',  'le',  'lei',  'leng',  'li',  'lia',  'lian',  'liang',  'liao',  'lie',  'lin',  'ling',  'liu',  'long',  'lou',  'lu',  'luan',  'lun',  'luo',  'lü',  'lüe',  'ma',  'mai',  'man',  'mang',  'mao',  'me',  'mei',  'men',  'meng',  'mi',  'mian',  'miao',  'mie',  'min',  'ming',  'miu',  'mo',  'mou',  'mu',  'na',  'nai',  'nan',  'nang',  'nao',  'ne',  'nei',  'nen',  'neng',  'ni',  'nian',  'niang',  'niao',  'nie',  'nin',  'ning',  'niu',  'nong',  'nou',  'nu',  'nuan',  'nun',  'nuo',  'nü',  'nüe',  'o',  'ou',  'pa',  'pai',  'pan',  'pang',  'pao',  'pei',  'pen',  'peng',  'pi',  'pian',  'piao',  'pie',  'pin',  'ping',  'po',  'pou',  'pu',  'qi',  'qia',  'qian',  'qiang',  'qiao',  'qie',  'qin',  'qing',  'qiong',  'qiu',  'qu',  'quan',  'que',  'qun',  'ran',  'rang',  'rao',  're',  'ren',  'reng',  'ri',  'rong',  'rou',  'ru',  'rua',  'ruan',  'rui',  'run',  'ruo',  'sa',  'sai',  'san',  'sang',  'sao',  'se',  'sen',  'seng',  'sha',  'shai',  'shan',  'shang',  'shao',  'she',  'shei',  'shen',  'sheng',  'shi',  'shou',  'shu',  'shua',  'shuai',  'shuan',  'shuang',  'shui',  'shun',  'shuo',  'si',  'song',  'sou',  'su',  'suan',  'sui',  'sun',  'suo',  'ta',  'tai',  'tan',  'tang',  'tao',  'te',  'tei',  'teng',  'ti',  'tian',  'tiao',  'tie',  'ting',  'tong',  'tou',  'tu',  'tuan',  'tui',  'tun',  'tuo',  'wa',  'wai',  'wan',  'wang',  'wei',  'wen',  'weng',  'wo',  'wu',  'xi',  'xia',  'xian',  'xiang',  'xiao',  'xie',  'xin',  'xing',  'xiong',  'xiu',  'xu',  'xuan',  'xue',  'xun',  'ya',  'yan',  'yang',  'yao',  'ye',  'yi',  'yin',  'ying',  'yong',  'you',  'yu',  'yuan',  'yue',  'yun',  'za',  'zai',  'zan',  'zang',  'zao',  'ze',  'zei',  'zen',  'zeng',  'zha',  'zhai',  'zhan',  'zhang',  'zhao',  'zhe',  'zhei',  'zhen',  'zheng',  'zhi',  'zhong',  'zhou',  'zhu',  'zhua',  'zhuai',  'zhuan',  'zhuang',  'zhui',  'zhun',  'zhuo',  'zi',  'zong',  'zou',  'zu',  'zuan',  'zui',  'zun',  'zuo'}

def is_cjk(char):
    char = ord(char)
    for bottom, top in cjk_ranges:
        if char >= bottom and char <= top:
            return True
    return False

def should_be_excluded(char):
    char = ord(char)
    for bottom, top in exclusion_ranges:
        if bottom <= char <= top:
            return True
    return False

def get_pinyin_splits(pron):
    pron = pron.replace('`', '').replace('"', '').replace("'", '').replace('’', '')
    pron_NFD = unic.normalize('NFD', pron)
    pron_no_tones = ''.join([c for c in pron_NFD if ord(c) < 128 or ord(c) == 776])
    pron_no_tones = unic.normalize('NFC', pron_no_tones)
    valid_splits = []
    for i in range(1, len(pron_no_tones)):
        if pron_no_tones[:i] in pinyins and pron_no_tones[i:] in pinyins:
            valid_splits.append((pron[:i], pron[i:]))
    return valid_splits