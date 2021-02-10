import numpy as np
import matplotlib.pyplot as plt

#데이터
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#그래프
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos") #cos함수는 점선으로
plt.xlabel("x") #x축 이름
plt.ylabel("y") #y축 이름
plt.title('sin & cos')  #제목
plt.legend()    #그래프 범례 추가
plt.show()