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


if __name__ == '__main__':
    url = 'https://ghproxy.com/https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/proxy-list.txt'
    filename = '/tmp/proxy-list.txt'
    download_file(url, filename)
    process_file(filename, 'proxy-list-smartdns.txt')
