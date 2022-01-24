import sys
sys.path.append('..') #부모 디렉터리의 파일을 가져올 수 있도록 생성
from dataset import spiral
import matplotlib.pyplot as plt

x, t = spiral.load_data()
print('x', x.shape)
print('y', t.shape)

# 데이터점 플롯
N = 100  #데이터 개수
CLS_NUM = 3  #데이터 클라스 개수
markers = ['o', 'x', '^']  #3개의 클라스 마커
for i in range(CLS_NUM):
    plt.scatter(x[i*N:(i+1)*N, 0], x[i*N:(i+1)*N, 1], s=40, marker=markers[i])
plt.show()
plt.savefig('show_spiral_dataset.png')