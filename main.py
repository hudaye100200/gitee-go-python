import datetime
import requests

print('Hello World!')
print('Time is ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))

def main():
    resp = requests.get('https://gitee.com/mktime')
    print(resp)

if __name__ == '__main__':
    main()