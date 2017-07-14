import numpy as inp
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import os



def prSetting(  ):
	plt.clf()
	plt.xticks(weight='bold')
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
def plotAnewFigure ( xString, yString, xCol,yCol,fileString, InputArray,hueCol=None):

	prSetting()
	legend_properties = {'weight':'bold', 'size': 24}
#	palette="muted"
#	palette="gray"
#	palette="tab20"
	col_list = [ "slate"]
#	sns.palplot(sns.xkcd_palette(col_list))
	col_list_palette = sns.xkcd_palette(col_list)
#	sns.set_palette(col_list_palette)
#	sns_plot= sns.barplot(x=xCol, y=yCol, hue=hueCol,ci=None, palette=col_list_palette,data=InputArray)
	sns_plot= sns.pointplot(x=xCol, y=yCol, hue=hueCol, ci=95,data=InputArray, linestyles=["-"], join=True,color='black')
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
#	plt.yscale('log')
#	plt.legend(loc='upper left',fontsize=34)
#	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=24)
	plt.legend(loc='upper right', prop=legend_properties)
	fig=sns_plot.get_figure()
	fig.savefig(fileString,bbox_inches='tight')
	return
prSetting()
#---------------------
directory= "PerformanceAndEnergyAnalysis"
os.makedirs("PerformanceAndEnergyAnalysis/PerformanceFigs", exist_ok=True)
os.makedirs("PerformanceAndEnergyAnalysis/EnergyFigs", exist_ok=True)
for filename in os.listdir(directory):
	if filename.endswith(".csv") : 
		CSVQuantName=os.path.join(directory, filename)
		print(CSVQuantName)		
		x1 = pd.read_csv(CSVQuantName,skiprows=0, delim_whitespace=True)
		x1=x1.iloc[1::2]
		print(x1.columns.values)
		print(x1.shape)
		cols_to_norm = ['runtime']
#		x1[cols_to_norm] = x1[cols_to_norm].apply(lambda p:(1-(p/ p[15]))*100)
		x1[cols_to_norm] = x1[cols_to_norm].apply(lambda p:( p[15]/p))
		x=x1
		figureName="PerformanceAndEnergyAnalysis/PerformanceFigs/"+filename[:-4]+".pdf"
		print(figureName)
		plotAnewFigure ( xString="Bit-Width", yString="Performance Improvement",xCol="configNumber",yCol="runtime", fileString=figureName,InputArray=x)
#---------------------------
		figureName="PerformanceAndEnergyAnalysis/EnergyFigs/"+filename[:-4]+".pdf"
		cols_to_norm = ['Penergy']
#		x1[cols_to_norm] = x1[cols_to_norm].apply(lambda p: (1-(p/ p.max()))*100)
		x1[cols_to_norm] = x1[cols_to_norm].apply(lambda p: (1-(p/ p[15]))*100)
		x=x1
		print(figureName)
		plotAnewFigure ( xString="Bit-Width", yString="Energy Reduction",xCol="configNumber",yCol="Penergy", fileString=figureName,InputArray=x)
#-------------------------

	else:
		continue
