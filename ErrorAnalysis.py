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
def plotAnewFigure ( xString, yString, xCol,yCol,hueCol,fileString, InputArray):

	prSetting()
	legend_properties = {'weight':'bold', 'size': 24}
#	palette="muted"
#	palette="gray"
#	palette="tab20"
	col_list = [ "slate", "cool grey"]
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
	plt.yscale('log')
#	plt.legend(loc='upper left',fontsize=34)
#	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=24)
	plt.legend(loc='upper right', prop=legend_properties)
	fig=sns_plot.get_figure()
	fig.savefig(fileString,bbox_inches='tight')
	return
prSetting()
#---------------------
directory= "ErrorAnalysis/Quantization"
os.makedirs("ErrorAnalysis/AbSInputFigs", exist_ok=True)
os.makedirs("ErrorAnalysis/AbSOutputFigs", exist_ok=True)
os.makedirs("ErrorAnalysis/RelOutFigs", exist_ok=True)
for filename in os.listdir(directory):
	if filename.endswith(".csv") : 
		CSVQuantName=os.path.join(directory, filename)
		CSVOLSBName=os.path.join('ErrorAnalysis/OLSB', filename)
		print(CSVQuantName)		
		print(CSVOLSBName)
		x1 = pd.read_csv(CSVQuantName,skiprows=6, delim_whitespace=True)
		x1.drop(x1.index[0], inplace=True)
		x2 = pd.read_csv(CSVOLSBName,skiprows=6, delim_whitespace=True)
		x2.drop(x2.index[0], inplace=True)
		x=x1.append(x2, ignore_index=True)
		x=x.iloc[1::2]
		print(x1.columns.values)
		print(x2.columns.values)
		print(x1.shape)
		print(x2.shape)
		print(x.shape)

		print(len(x['Method']))
		figureName="ErrorAnalysis/AbSInputFigs/"+filename[:-4]+".pdf"
		print(figureName)
		plotAnewFigure ( xString="Bit-Width", yString="Max Absolute Error",xCol="fileNamingArg",yCol="MAxAbsErrInput",hueCol="Method", fileString=figureName,InputArray=x)
#---------------------------
		figureName="ErrorAnalysis/RelOutFigs/"+filename[:-4]+".pdf"
		print(figureName)
		plotAnewFigure ( xString="Bit-Width", yString="Relative Error",xCol="fileNamingArg",yCol="AverageRelativeError",hueCol="Method", fileString=figureName,InputArray=x)
#-------------------------
		figureName="ErrorAnalysis/AbSOutputFigs/"+filename[:-4]+".pdf"
		print(figureName)
		plotAnewFigure ( xString="Bit-Width", yString="Max Absolute Error",xCol="fileNamingArg",yCol="MaxAbsErrorOutput",hueCol="Method", fileString=figureName,InputArray=x)
	else:
		continue
