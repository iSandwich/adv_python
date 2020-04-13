from datetime import datetime
# print(datetime.now())

def file_path_decor(path):
    def log_decor(old_func):
        def new_func(*args, **kwargs):
            result = old_func(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as logs:
                logs.write(f'Timestamp: {datetime.now()}\n')
                logs.write(f'Function name: {old_func.__name__}\n')
                logs.write(f'Args: {args}, {kwargs}\n')
                logs.write(f'Return: {str(result)}\n')
                logs.write('\n')
            return result
        return new_func
    return log_decor

if __name__ == '__main__':
    trigger = input('Please type in the file name (without .txt): ')
    if not trigger:
        file_path = 'log.txt'
    else:
        file_path = f'{trigger}.txt'

    @file_path_decor(file_path)
    def printer(x):
        textline = f'Yes, this is {x}.'
        return textline

    print(printer(f'{file_path}'))