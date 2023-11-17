import re
import urllib.request


def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)


def process_file(input_file, output_file):
    with open(input_file, 'r') as f1, open(output_file, 'w') as f2:
        for line in f1:
            if line.startswith('full:'):
                f2.write(line[5:])
            elif line.startswith('regexp:'):
                continue
            else:
                f2.write(line)


def process_ruleset(input_file, output_file):
    with open(input_file, 'r') as f1, open(output_file, 'a') as f2:
        for line in f1:
            pattern = r"'\+?\.?(.*?)'"  # 正则表达式模式，匹配位于单引号中间的子串
            matches = re.findall(pattern, line)
            if matches:
                f2.write(matches[0] + '\n')


if __name__ == '__main__':
    dst_filename = 'proxy-list-smartdns.txt'

    url = 'https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/proxy-list.txt'
    filename = '/tmp/proxy-list.txt'
    download_file(url, filename)
    process_file(filename, dst_filename)

    url = 'https://gist.githubusercontent.com/Hotwill/d04d795b8a72cac7691f24b2fdfaf9b6/raw/my_proxy_ruleset.txt'
    filename = '/tmp/my_proxy_ruleset.txt'
    download_file(url, filename)
    process_ruleset(filename, dst_filename)
