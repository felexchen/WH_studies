import ROOT
import sys
from optparse import OptionParser
import fnmatch
import array
import numpy as np
from WH_studies.Tools.u_float import u_float as uf

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Global definitions

COLORS = [ROOT.kBlue+1, ROOT.kRed+1, ROOT.kGreen+1, ROOT.kYellow+1, ROOT.kOrange+1, ROOT.kViolet+1]

COMBINATION_STR = []

# Set file paths
SM_WH = ""
for arg in sys.argv:
    if "smwh" in arg.lower():
        SM_WH = "SM_WH/"
SR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/FatJet_pT/" + SM_WH + "g150/root/lin"
CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mCT/FatJet_pT/" + SM_WH + "l200/root/lin"
#for arg in sys.argv:
#    if arg.lower() == "mct":
#        CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mCT/FatJet_pT/" + SM_WH + "l200/root/lin"

VAR = "mct"#"mt_met_lep"
VAR_THRESHOLD = "200"#"150"
#for arg in sys.argv:
#    if arg.lower() == "mct":
#        VAR = "mct"
#        VAR_THRESHOLD = "200"

YEARS = ["2016", "2017", "2018"]
JETS = ["ngoodjets2", "ngoodjets3"]
BTAGS = ["b0", "b1", "b2"]

# This order follows the cxx plotting script
BKG_IDX = 1
SIGNAL_ALL_MASS = 7
SIGNAL_ALL = 8
SIGNAL_700_1 = 9
SIGNAL_650_300 = 10
SIGNAL_225_75 = 11
DATA_IDX = 12
if not ("" == SM_WH):
    # 1 more bkg means every non-bkg shifts down 1
    SIGNAL_ALL_MASS += 1
    SIGNAL_ALL += 1
    SIGNAL_700_1 += 1
    SIGNAL_650_300 += 1
    SIGNAL_225_75 += 1
    DATA_IDX += 1
#IDEXS = [BKG_IDX, SIGNAL_ALL, SIGNAL_700_1, SIGNAL_650_300, SIGNAL_225_75, DATA_IDX]
IDEXS = [BKG_IDX, SIGNAL_ALL_MASS, SIGNAL_ALL]#, DATA_IDX]
N_BKGS_DATA = len(IDEXS)

BINNING = array.array('d', [0,200,1000])
N_BINS = len(BINNING)-1
BINNING_FOR_TH1D = (N_BINS, BINNING)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Function definitions

# Add command line options
def addCmdlineOptions():
    parser = OptionParser()
    parser.add_option("--combineYears", dest = "combineYears", default = False, action = "store_true", help = "Combine 2016, 2017, and 2018??")
    parser.add_option("--combineJets" , dest = "combineJets" , default = False, action = "store_true", help = "Combine 2 and 3 jet selections?")
    parser.add_option("--combineBTags", dest = "combineBTags", default = False, action = "store_true", help = "Combine 0, 1, and 2 b-tagged selections?")
    parser.add_option("--combineBkgs" , dest = "combineBkgs" , default = False, action = "store_true", help = "Combine all backgrounds?")
    parser.add_option("--SMWH"        , dest = "SMWH"        , default = False, action = "store_true", help = "Use root files with SM WH background?")
#    parser.add_option("--variable"    , dest = "variable"    , default = "mt" , action = "store"     , help = "Checking for mT or mCT dependence?")
    return parser.parse_args()

def setCombination(options):
    if options.combineBkgs:
        COMBINATION_STR.append('t#bar{t}, single top, ttV, W + Jets, diboson')
        if not ("" == SM_WH):
            COMBINATION_STR[0]+=', SM WH'
        COMBINATION_STR.append('signal (*,*)')
        COMBINATION_STR.append('signal (700,1), signal (650,300), signal (225,75)')
#        COMBINATION_STR.append('signal (700,1)')
#        COMBINATION_STR.append('signal (650,300)')
#        COMBINATION_STR.append('signal (225,75)')
        COMBINATION_STR.append('data')
    else:
        COMBINATION_STR.append('t#bar{t}, single top, ttV')
        COMBINATION_STR.append('W + jets, diboson')
        COMBINATION_STR.append('signal (*,*)')
        COMBINATION_STR.append('signal (700,1), signal (650,300), signal (225,75)')
#        COMBINATION_STR.append('signal (700,1)')
#        COMBINATION_STR.append('signal (650,300)')
#        COMBINATION_STR.append('signal (225,75)')
        COMBINATION_STR.append('data')


# Get files from directories
def getFiles(options, *argv):
    from os import listdir
    from os.path import isfile, join
    for arg in argv:
        print arg
    allFiles = []
    for path in argv:
        for f in sorted(listdir(path)):
            full = join(path, f)
            if isfile(full):

                # There are four scenarios: comb year or no, comb jets or no

                # if combine years then only add combs
                if options.combineYears:
                    if "yComb" in full:
                        if options.combineJets:
                            if "ngoodjetsge2_ngoodjetsle3" in full:
                                allFiles.append(full)        
                        else:
                            if not "ngoodjetsge2_ngoodjetsle3" in full:
                                allFiles.append(full)
                # if not combine years then only add not combs
                else:
                    if not ("yComb" in full):
                        if options.combineJets:
                            if "ngoodjetsge2_ngoodjetsle3" in full:
                                allFiles.append(full)        
                        else:
                            if not "ngoodjetsge2_ngoodjetsle3" in full:
                                allFiles.append(full)
#                print(f)
    return allFiles

# For oldList = ["a","b"] and selection = ["1","3","4"], newList = ["a*1","b*1","a*3","b*3","a*4","b*4"]
def expandList(oldList, selection):
    newList = []
    for sel in selection:
        for elem in oldList:
            newList.append(elem + "*" + sel)
    return newList

# Figures out how to group files
def generateGrouping(options):
    grouping = [""]
    if not options.combineYears:
        grouping = expandList(grouping, YEARS)
    if not options.combineJets:
        grouping = expandList(grouping, JETS)
#    grouping = expandList(grouping, REGIONS)
    PASS_OR_TOTAL = ["nFat","nHiggsFat"]
    grouping = expandList(grouping, PASS_OR_TOTAL)
    if not options.combineBTags:
        grouping = expandList(grouping, BTAGS)
    for i in range(len(grouping)): 
        grouping[i] += '*'
        print grouping[i]
    return grouping

# Groups files
def groupFiles(allFiles, options):
    fileGroups = []
    grouping = generateGrouping(options)
    for selection in grouping:
        dummyList = []
        for f in allFiles:
            if fnmatch.fnmatch(f, selection):
                dummyList.append(f)
                print(f[80:])
        fileGroups.append(dummyList)
        print("\n")
    return fileGroups, grouping

def generateTitles(grouping):
    titles = ["" for row in range(len(grouping))]
    for row in range(len(titles)):
        if "nFat" in grouping[row]:
            titles[row] += ("Total ")
        else:
            titles[row] += ("Higgs ")
        for year in YEARS:
            if year in grouping[row]:
#                if year == "Comb":
#                    titles[row] += "All Years "
#                    break
                titles[row] += (year + " ")
                break
        for jets in JETS:
            if jets in grouping[row]:
                titles[row] += (jets[-1] + " jets ")
                break
        for b in BTAGS:
            if b in grouping[row]:
                if '1' in b:
                    titles[row] += ("1 b tag ")
                    break
                titles[row] += (b[-1] + " b tags ")
                break
#         for region in REGIONS:
#             if region in grouping[row]:
# #                if "mt_met_lepg150" == region:
# #                    titles[row] += "mT > 150 "
# #                    break
# #                elif "mt_met_lepl150" == region:
# #                    titles[row] += "150 > mT > 50"
# #                    break
# #                elif "mctg200" == region:
#                 if "mctg200" == region:
#                     titles[row] += "mCT > 200"
#                     break
#                 else:
#                     titles[row] += "200 > mCT"
#                     break
#                titles[row] += (region[:-4] + " ")
#                if 'g' in region:
#                    titles[row] += "> "
#                else:
#                    titles[row] += "< "
#                titles[row] += (region[-3:])
#                break
        if ' ' == titles[row][-1]:
            titles[row] = titles[row][:-1]
    return titles

def generatePngNames(grouping):
    pngNames = ["" for row in range(len(grouping))]
    for row in range(len(pngNames)):
        if "nFat" in grouping[row]:
            pngNames[row] += ("Total_")
        else:
            pngNames[row] += ("Higgs_")
        for year in YEARS:
            if year in grouping[row]:
                pngNames[row] += (year + "_")
                break
        for jets in JETS:
            if jets in grouping[row]:
                pngNames[row] += (jets[-1] + "jets_")
                break
        for b in BTAGS:
            if b in grouping[row]:
                if '1' in b:
                    pngNames[row] += ("1btag_")
                    break
                pngNames[row] += (b[-1] + "btags_")
                break
#        for region in REGIONS:
#            if region in grouping[row]:
#                pngNames[row] += region 
#                if "mt_met_lepl150" == region:
#                    pngNames[row] += "mt_met_met_lepg50"
#                    break
        if '_' == pngNames[row][-1]:
            pngNames[row] = pngNames[row][:-1]
    return pngNames

### def isSR(fileName):
###     # SR does not have data
###     if (SR in fileName): 
###         return True
###     else:
###         return False

# Open file, get hist, and return IntegralAndError for entire spectrum
def combineIntoOneBin(fileName, idx):
    f = ROOT.TFile(fileName)
    assert not f.IsZombie()
    f.cd()
    canvasName = f.GetListOfKeys().At(0).GetName()
    tempCanvas = f.Get(canvasName)
    canvas = tempCanvas.Clone()
    f.Close()
    topPad = canvas.FindObject("mytoppad")
    topPadList = topPad.GetListOfPrimitives()
    #topPadList.ls()
    it = topPadList.begin()
    hist = it.Next()
    for i in range(idx-1):
        hist = it.Next()
    #print(hist.GetName())
    err = ROOT.Double()
    integ = hist.IntegralAndError(1, 30, err)
    return integ, err

def generateHist(lowmct, highmct, idx, title, color):
    lowmctYield, lowmctUncertainty = combineIntoOneBin(lowmct, idx)
    highmctYield, highmctUncertainty = combineIntoOneBin(highmct, idx)
    hist = ROOT.TH1D("", title + ";mCT [GeV];# Events", *BINNING_FOR_TH1D) 
    hist.SetLineWidth(2)
    hist.SetLineColor(color)
    hist.GetYaxis().SetTitleOffset(1.4);
    hist.SetBinContent(1, lowmctYield)
    hist.SetBinError(1, lowmctUncertainty)
    hist.SetBinContent(2, highmctYield)
    hist.SetBinError(2, highmctUncertainty)
    return hist 
    
def histsAndLegFromGroup(fileGroup, title):
    print sorted(fileGroup)
    lowmct = fileGroup[1] # l
    highmct = fileGroup[0] # g
    hists = []
    leg = ROOT.TLegend(0.5,0.75,0.9,0.9)
    for i, idx in enumerate(IDEXS):
        h = generateHist(lowmct, highmct, idx, title, COLORS[i])
        hists.append(h)
        leg.AddEntry(h, COMBINATION_STR[i], 'l')
    return hists, leg

def extractUfFromBin(hist, bin):
    binContent = hist.GetBinContent(bin)
    error = hist.GetBinError(bin)
    return uf(binContent, error)

def generateSavePath(options):
#    path = "plots/mCT/FatJet_pT/" + SM_WH 
    path = "plots/" + SM_WH 
#    if "mt" == options.variable:
#        path += "mT/" + "FatJet_pT/" + SM_WH
#    else: 
#        path += "mCT/" + "FatJet_pT/" + SM_WH
    if options.combineYears:
        path += "combYears"
    if options.combineJets:
        path += "combJets"
    if options.combineBTags:
        path += "combBTags"
    if options.combineBkgs:
        path += "combBkgs"
    if not ('s' == path[-1]):
        path += "noComb"
    if '/' == path[-1]:
        pass
    else:
        path += "/"
    return path
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if __name__ == "__main__":

    # Parsing command line
    (options, args) = addCmdlineOptions()
    setCombination(options)
    print(COMBINATION_STR)
    
    # Getting and grouping files
    allFiles = getFiles(options, SR_FILE_PATH, CR_FILE_PATH)
    print("Using {} files".format(len(allFiles)))
    fileGroups, grouping = groupFiles(allFiles, options)
    titles = generateTitles(grouping)
    for i, title in enumerate(titles):
        print("{:2} {}".format(i, title))
    pngNames = generatePngNames(grouping)
    for i, pngName in enumerate(pngNames):
        print("{:2} {}".format(i, pngName))
    savePath = generateSavePath(options)
    print savePath
    higgsPies = [[[[0,0],[0,0]] for j in range(len(grouping))] for i in range(len(IDEXS))]
    totalPies = [[[[0,0],[0,0]] for j in range(len(grouping))] for i in range(len(IDEXS))]
        #sys.exit()
    # Plotting
    ROOT.gStyle.SetOptStat(0)
    for groupCount, fileGroup in enumerate(fileGroups):
        can = ROOT.TCanvas("","",800,800)
        can.Draw()
        hists, leg = histsAndLegFromGroup(fileGroup, titles[groupCount])#, options)
#        hists, leg = histsAndLegFromGroup(fileGroup, titles[groupCount])#, options)
        for i, hist in enumerate(hists): 
            b = 999
            if "b0" in fileGroup[0]:
                b = 0
            elif "b1" in fileGroup[0]:
                b = 1
            else:
                b = 2
            if "Higgs" in fileGroup[0]:
                higgsPies[b][i][0][0] = hist.GetBinContent(1)
                higgsPies[b][i][0][1] = hist.GetBinError(1)
                higgsPies[b][i][1][0] = hist.GetBinContent(2)
                higgsPies[b][i][1][1] = hist.GetBinError(2)
            else:
                totalPies[b][i][0][0] = hist.GetBinContent(1)
                totalPies[b][i][0][1] = hist.GetBinError(1)
                totalPies[b][i][1][0] = hist.GetBinContent(2)
                totalPies[b][i][1][1] = hist.GetBinError(2)
            hist.Draw("SAME")
            hist.Draw("hist same")
        leg.Draw()
#        print("Saving {} \n".format(savePath + pngNames[groupCount] + ".png"))
        can.SaveAs(savePath + pngNames[groupCount] + ".png")

    
    print("\n\n\\n\n\n")
    print("higgs")
    for b in range(3):
        print "b{}".format(b)
        for idx in range(len(IDEXS)):
            print "{:>20} +- {:>20}                {:>20} +- {:>20}".format(higgsPies[b][idx][0][0], higgsPies[b][idx][0][1], higgsPies[b][idx][1][0], higgsPies[b][idx][1][1])
        print "\n"
    print("\n\n\n\n\n")
    print("total")
    for b in range(3):
        print "b{}".format(b)
        for idx in range(len(IDEXS)):
            print "{:>20} +- {:>20}                {:>20} +- {:>20}".format(totalPies[b][idx][0][0], totalPies[b][idx][0][1], totalPies[b][idx][1][0], totalPies[b][idx][1][1])
        print "\n"

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    # Data to plot
    names = ["bkgs", "signal all mass", "signal"]
    labels = 'b0', 'b1', 'b2'
    colors = ['lightskyblue', 'lightcoral', 'yellowgreen']    
#    for b, label in enumerate(labels):
    for idx in range(len(IDEXS)):
        sizes = []
        sizes.append(higgsPies[0][idx][0][0])
        sizes.append(higgsPies[1][idx][0][0])
        sizes.append(higgsPies[2][idx][0][0])
        plt.pie(sizes, labels=labels, colors=colors,  autopct='%.2f', shadow=True, startangle=140)
        #    sizes = [215, 130, 245, 210]
        
#explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
#plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    
#    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#            autopct='%.2f%',, shadow=True, startangle=140)

#        plt.axis('equal')
#plt.show()
        plt.savefig(savePath + "Higgs_lowmct_" + names[idx] + ".png")
        plt.clf()
    for idx in range(len(IDEXS)):
        sizes = []
        sizes.append(higgsPies[0][idx][1][0])
        sizes.append(higgsPies[1][idx][1][0])
        sizes.append(higgsPies[2][idx][1][0])
        plt.pie(sizes, labels=labels, colors=colors,  autopct='%.2f', shadow=True, startangle=140)
#        plt.pie(sizes, labels=labels, colors=colors,
#                autopct='%.2f', shadow=True, startangle=140)
#        plt.axis('equal')
        plt.savefig(savePath + "Higgs_highmct_" + names[idx] + ".png")
        plt.clf()
    for idx in range(len(IDEXS)):
        sizes = []
        sizes.append(totalPies[0][idx][0][0])
        sizes.append(totalPies[1][idx][0][0])
        sizes.append(totalPies[2][idx][0][0])
        plt.pie(sizes, labels=labels, colors=colors,  autopct='%.2f', shadow=True, startangle=140)
#        plt.pie(sizes, labels=labels, colors=colors,
#                autopct='%.2f', shadow=True, startangle=140)
        #plt.axis('equal')
        plt.savefig(savePath + "Total_lowmct_" + names[idx] + ".png")
        plt.clf()
    for idx in range(len(IDEXS)):
        sizes = []
        sizes.append(totalPies[0][idx][1][0])
        sizes.append(totalPies[1][idx][1][0])
        sizes.append(totalPies[2][idx][1][0])
        plt.pie(sizes, labels=labels, colors=colors,  autopct='%.2f', shadow=True, startangle=140)
#        plt.pie(sizes, labels=labels, colors=colors,
#                autopct='%.2f', shadow=True, startangle=140)
#        plt.axis('equal')
        plt.savefig(savePath + "Total_highmct_" + names[idx] + ".png")
        plt.clf()
