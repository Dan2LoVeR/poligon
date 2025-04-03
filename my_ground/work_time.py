import matplotlib.pyplot as plt
import mplcyberpunk
from datetime import datetime
import numpy as np

now_day = datetime.today() #сегодняшняя дата
start_day = datetime.strptime('2025-03-13', '%Y-%m-%d') #дата начала работы
work_day = np.busday_count(start_day.strftime('%Y-%m-%d'), now_day.strftime('%Y-%m-%d'))
print(work_day)

plt.style.use('cyberpunk')
ax = plt.subplot()
x = 1 + np.arange(2)
ax.bar(x ,[work_day, 366], width=1)
label = 'проработано '+ str(work_day)+ ' дней'
ax.set_title(label)
plt.show()









