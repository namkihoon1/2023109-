import pickle
import os

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = sum(s)
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def search(lst, n):
    if n not in lst:
        return None
    return lst.index(n)

def save_scores(scores):
    with open('score.bin', 'wb') as file:
        pickle.dump(scores, file)

def load_scores():
    if os.path.exists('score.bin'):
        with open('score.bin', 'rb') as file:
            return pickle.load(file)
    return None

print('[점수 입력]')
scores = input_scores()

print('\n[점수 출력]')
print('개인점수:', end=' ')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}')

save_scores(scores)

print('\n[파일읽기]')
loaded_scores = load_scores()
if loaded_scores is not None:
    print('\n[점수 출력]')
    print('개인점수:', end=' ')
    show_scores(loaded_scores)
    avg = get_average(loaded_scores)
    print(f'평균: {avg:.1f}')
