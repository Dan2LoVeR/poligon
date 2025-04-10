import matplotlib.pyplot as plt
import mplcyberpunk
from datetime import datetime
import time
import numpy as np

timestamp = time.time()
now_day = datetime.today() #сегодняшняя дата
start_day = datetime.strptime('2025-03-13', '%Y-%m-%d') #дата начала работы
work_day = np.busday_count(start_day.strftime('%Y-%m-%d'), now_day.strftime('%Y-%m-%d'))
now = datetime.now()

target = datetime(now.year, now.month, now.day, 17, 30, 0)

diff = target - now

plt.style.use('cyberpunk')
ax = plt.subplot()
x = 1 + np.arange(1)
ax.bar(x,247, width=0.35, label='год')
ax.bar(x,work_day,width=0.35, label='рабочие дни' )
label = f'проработано {str(work_day)} дней, до конца рабобечего дня осталось {diff}'
plt.title(label)
plt.show()









