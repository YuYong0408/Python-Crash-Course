from die import Die

import pygal
die_1=Die()
die_2=Die(10)
resuls = []
for roll_num in range(50000):
    result = die_1.roll()+ die_2.roll()
    results.append(reult)


hist = pygal.bar()
hist.title = "sjdfjs;fj;s"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13',
'14','15','16']
hist.x_title ='result'
hist.y_title = 'frequency of result'

hist.add('D6+D10',frequencies)
hist.render_to_file('dice_visual.svg')
