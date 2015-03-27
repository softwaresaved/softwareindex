import numpy as np
import matplotlib.pyplot as plt
from handlers import test_handler
from handlers import stackoverflow_handler

handlerlist = [test_handler.test_handler(), stackoverflow_handler.stackoverflow_handler()]
software = ['itksnap','tetgen','python','mrbayes','micromanager']
results = []

for handlerid in range(len(handlerlist)):
	localresults = []
	for softwareid in range(len(software)):
		handler = handlerlist[handlerid]
		localresults.append(handler.get_score(software[softwareid]))
	results.append(localresults)
#plot

print(results)


for i in range(len(handlerlist)):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	ind = np.arange(len(software))                # the x locations for the groups
	width = 0.35                      # the width of the bars

	rects = ax.bar(ind, results[i], width)

	# axes and labels
	ax.set_ylabel('Scores')
	xTickMarks = software
	ax.set_xticks(ind+width)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=45, fontsize=10)
	plt.savefig("scoresWithHandlerNumber"+str(i+1))
