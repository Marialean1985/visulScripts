import numpy as inp
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import os
import math
import itertools


def prSetting(  ):
	plt.clf()
	plt.xticks(weight='bold',rotation=30)
	plt.yticks(weight='bold')
	plt.tick_params(labelsize=18)
	#plt.figure(figsize=(3.1, 3))
	plt.tight_layout()
	sns.set(color_codes=True)
	sns.set_context("paper",font_scale=1.5, rc={"lines.linewidth": 1.5})
	sns.set_style("whitegrid")
	sns.set_style({'axes.edgecolor': 'black'})
	sns.set_style({'axes.linewidth': 1.0})
	return
def plotAnewFigure ( xString, yString, xCol,yCol,hueCol,fileString, InputArray):

	prSetting()
	legend_properties = {'weight':'bold', 'size': 24}
#	palette="muted"
#	palette="gray"
#	palette="tab20"
	col_list = [ "slate","silver","dark grey","cool grey"]
#	sns.palplot(sns.xkcd_palette(col_list))
	col_list_palette = sns.xkcd_palette(col_list)
#	sns.set_palette(col_list_palette)
	sns_plot= sns.barplot(x=xCol, y=yCol, hue=hueCol,ci=None, palette=col_list_palette,data=InputArray)
	sns_plot.set_xlabel(xString,fontsize=20, weight='bold')
	sns_plot.set_ylabel(yString,fontsize=20,weight='bold')
	sns.set_style("whitegrid")
	sns_plot.spines['top'].set_visible(True)
	sns_plot.spines['right'].set_visible(True)
	sns_plot.spines['bottom'].set_linewidth(1.0)
	sns_plot.spines['left'].set_linewidth(1.0)
	sns_plot.spines['right'].set_linewidth(1.0)
	sns_plot.spines['bottom'].set_linewidth(1.0)
	sns_plot.spines['bottom'].set_color('black')
	sns_plot.spines['top'].set_color('black')
	sns_plot.spines['left'].set_color('black')
	sns_plot.spines['right'].set_color('black')
#	hatches = itertools.cycle(['/', '\\', '+', '||', 'x', '*', 'o', 'O', '.'])
#	for i, bar in enumerate(sns_plot.patches):
#		if i % 4 == 0:
#			hatch = next(hatches)
#		bar.set_hatch(hatch)
#	plt.yscale('log')
#	plt.legend(loc='upper left',fontsize=34)
#	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=24)
	plt.legend(loc='best', prop=legend_properties)
	fig=sns_plot.get_figure()
	fig.savefig(fileString,bbox_inches='tight')
	return
prSetting()
#---------------------
visualDf=pd.DataFrame()
fileNamMap={'Alex.csv':'convolutionAlexnet.csv','Blackscholes.csv':'blackscholes.csv','FFT.csv':'fft.csv','Inversek2j.csv':'inversek2j.csv','Sobel.csv':'convolutionSobel.csv','VGG.csv':'convolutionVgg.csv', 'Jmeint.csv':'jmeint.csv'}

AppNamMap={'Alex.csv':'AlexNet','Blackscholes.csv':'Blackscholes','FFT.csv':'FFT','Inversek2j.csv':'Inversek2j','Sobel.csv':'Sobel','VGG.csv':'VGG', 'Jmeint.csv':'Jmeint'}
figureName="SamplingAnalysis/SamplingAnalysis.pdf"
directory= "SamplingAnalysis/Quantization"
for filename in os.listdir(directory):
	if filename.endswith(".csv")  and filename !="Kmeans.csv" : 
		CSVQuantName=os.path.join(directory, filename)
		
		print(filename)
		x1 = pd.read_csv(CSVQuantName,skiprows=6, delim_whitespace=True)
		x1.drop(x1.index[0], inplace=True)
#               x1=x1.iloc[1::2]
		x1['Application']=AppNamMap[filename]		
		visualDf=visualDf.append(x1, ignore_index=True)
#		print(len(x['Method']))
		

	else:

		continue

plotAnewFigure ( xString="Applications", yString="Outlier rate",xCol="fileNamingArg",yCol="outlierRate",hueCol="Application", fileString=figureName,InputArray=visualDf)
