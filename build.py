import os

def main():
    print 'test22'
    os.environ['TEST_ENV'] = 'sp'
    print os.environ['TEST_ENV']

if __name__ == '__main__':
    main()
