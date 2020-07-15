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
CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/FatJet_pT/" + SM_WH + "l150/root/lin"
for arg in sys.argv:
    if arg.lower() == "mct":
        CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mCT/FatJet_pT/" + SM_WH + "l200/root/lin"

VAR = "mt_met_lep"
VAR_THRESHOLD = "150"
for arg in sys.argv:
    if arg.lower() == "mct":
        VAR = "mct"
        VAR_THRESHOLD = "200"
SR = VAR + 'g' + VAR_THRESHOLD
CR = VAR + 'l' + VAR_THRESHOLD

YEARS = ["2016", "2017", "2018"]
JETS = ["ngoodjets2", "ngoodjets3"]
BTAGS = ["b0", "b1", "b2"]
REGIONS = [SR, CR]

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
#IDEXS = [BKG_IDX, SIGNAL_ALL_MASS, SIGNAL_ALL, SIGNAL_700_1, SIGNAL_650_300, SIGNAL_225_75, DATA_IDX]
IDEXS = [BKG_IDX, SIGNAL_ALL_MASS, SIGNAL_ALL, DATA_IDX]
N_BKGS_DATA = len(IDEXS)

BINNING = array.array('d', [250,350,950])#1750])
N_BINS = len(BINNING)-1
BINNING_FOR_TH1D = (N_BINS, BINNING)

B0_Y = [-0.01, 0.05]
B1_Y = [-0.1, 0.7]
B2_Y = [0, 1.1]

SF_B0_Y = [-1, 7]
SF_B1_Y = [0, 1.5]
SF_B2_Y = [0, 1.25]
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
    parser.add_option("--variable"    , dest = "variable"    , default = "mt" , action = "store"     , help = "Checking for mT or mCT dependence?")
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
    grouping = expandList(grouping, REGIONS)
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
        for region in REGIONS:
            if region in grouping[row]:
                if "mt_met_lepg150" == region:
                    titles[row] += "mT > 150 "
                    break
                elif "mt_met_lepl150" == region:
                    titles[row] += "150 > mT > 50"
                    break
                elif "mctg200" == region:
                    titles[row] += "mCT > 200"
                    break
                else:
                    titles[row] += "200 > mCT"
                    break
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
        for region in REGIONS:
            if region in grouping[row]:
                pngNames[row] += region 
                if "mt_met_lepl150" == region:
                    pngNames[row] += "mt_met_met_lepg50"
                    break
        if '_' == pngNames[row][-1]:
            pngNames[row] = pngNames[row][:-1]
    return pngNames

def isSR(fileName):
    # SR does not have data
    if (SR in fileName): 
        return True
    else:
        return False

# Plots y = 1
def yEqualsOne(xmin, xmax):
    binning = [xmin, xmax]
    binningForTH1D = (1, array.array('d', binning))
    one = ROOT.TH1D("","",*binningForTH1D)
    one.SetBinContent(1,1)
    one.SetLineColor(ROOT.kBlack)
    return one
    
# Open file, get hist, and create new hist with binning given by BINNING above
def combineBins(fileName, idx, inclusive = False):
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
    print(hist.GetName())
    err = ROOT.Double()
    if inclusive:
        singleBin = [min(BINNING), max(BINNING)]
        singleBinning = (1, array.array('d', singleBin))
        histCombinedBin = ROOT.TH1D("", "", *singleBinning)
        histCombinedBin.SetBinContent(1, hist.IntegralAndError(1, 30, err))
        histCombinedBin.SetBinError(1, err)
        return histCombinedBin
    else:
        histCombinedBin = ROOT.TH1D("", "", *BINNING_FOR_TH1D)
        histCombinedBin.SetBinContent(1, hist.IntegralAndError(1, 3, err))
        histCombinedBin.SetBinError(1, err)
        histCombinedBin.SetBinContent(2, hist.IntegralAndError(4, 30, err))
        histCombinedBin.SetBinError(2, err)
        return histCombinedBin

def generateMistagHistAndInclusive(passed, total, idx, title, color):
    passedCombinedBin = combineBins(passed, idx)
    totalCombinedBin = combineBins(total, idx)
    passedInclusive = combineBins(passed, idx, inclusive = True)
    totalInclusive = combineBins(total, idx, inclusive = True)
    if ROOT.TEfficiency.CheckConsistency(passedCombinedBin, totalCombinedBin) and ROOT.TEfficiency.CheckConsistency(passedInclusive, totalInclusive):
        teff = ROOT.TEfficiency(passedCombinedBin, totalCombinedBin)
        teff.Paint("") # AP is default but still needs to be passed..
        graph = teff.GetPaintedGraph()
        mistagHist = ROOT.TH1D("", title + ";FatJet p_{T} [GeV];mistag efficiencies", *BINNING_FOR_TH1D) 
        if "0 b" in title:
            mistagHist.SetAxisRange(B0_Y[0], B0_Y[1], "Y")
        elif "1 b" in title:
            mistagHist.SetAxisRange(B1_Y[0], B1_Y[1], "Y")
        elif "2 b" in title:
            mistagHist.SetAxisRange(B2_Y[0], B2_Y[1], "Y")
        mistagHist.SetLineWidth(2)
        mistagHist.SetLineColor(color)
        mistagHist.GetYaxis().SetTitleOffset(1.4);
#          print graph.GetN()
        for i in range(graph.GetN()):
            x = ROOT.Double()
            y = ROOT.Double()
            graph.GetPoint(i, x, y)
     #       print i 
            mistagHist.SetBinContent(i+1, y)
            e = graph.GetErrorY(i)
            mistagHist.SetBinError(i+1, e)#graph.GetErrorY(i))
            if i == 1:
                print "{} {} {}".format(idx, y, e)
        incTeff = ROOT.TEfficiency(passedInclusive, totalInclusive)
        incTeff.Paint("")
        incGraph = incTeff.GetPaintedGraph()
        dummy = ROOT.Double()
        inclusive = ROOT.Double()
        incGraph.GetPoint(0, dummy, inclusive)
        inclusiveUncertainty = incGraph.GetErrorY(0)
        return mistagHist, inclusive, inclusiveUncertainty
#        return ROOT.TH1D("","asdasdasdas", *BINNING_FOR_TH1D), inclusive, inclusiveUncertainty
#####        return ROOT.TH1D("","asdasdasdas", *BINNING_FOR_TH1D), 0, 0


    else:
        print("ERROR: inconsistent!\n{}\n{}".format(passed, total))
        sys.exit()

def histsAndLegFromGroup(fileGroup, title):#, options):
    # fileGroup has two files. ALWAYS
#    print sorted(fileGroup)
    print("\n\n\n\n\n")
    passed = sorted(fileGroup)[1]
    total = sorted(fileGroup)[0]
    hists = []
    mistagInclusives = []
    leg = ROOT.TLegend(0.5,0.75,0.9,0.9)
    for i, idx in enumerate(IDEXS):
#        if not (i == 0):
#            continue
        if len(IDEXS) == (i+1):
            if isSR(fileGroup[0]): # any index will work
                print "FOUND SR"
                continue 
        h, inclusive, inclusiveUncertainty = generateMistagHistAndInclusive(passed, total, idx, title, COLORS[i]) 
        mistagInclusives.append(uf(inclusive, inclusiveUncertainty))
        hists.append(h)
        leg.AddEntry(h, COMBINATION_STR[i], 'l')
        leg.AddEntry(None, "inclusive: " + str(inclusive)[:5] + " #pm " + str(inclusiveUncertainty)[:5], '')
#    return hists, leg#, mistagInclusive
    return hists, leg, mistagInclusives

def extractUfFromBin(hist, bin):
    binContent = hist.GetBinContent(bin)
    error = hist.GetBinError(bin)
    return uf(binContent, error)

def generateSF(hists, title, mistagInclusive):
    # Last index is always for data
    dataHist = hists[-1]
    dataInclusive = mistagInclusive[-1]
    SFHists = []
    leg = ROOT.TLegend(0.5,0.75,0.9,0.9)
    for histCount, bkgHist in enumerate(hists):
        if len(hists) == histCount+1:
            break # Obviously we don't calculate data/data
        bkgSFHist = ROOT.TH1D("", title + " SF" + ";FatJet p_{T} [GeV];Data/MC", *BINNING_FOR_TH1D)
        bkgSFHist.SetLineColor(COLORS[histCount])
        if "0 b" in title:
            bkgSFHist.SetAxisRange(SF_B0_Y[0], SF_B0_Y[1], "Y")
        if "1 b" in title:
            bkgSFHist.SetAxisRange(SF_B1_Y[0], SF_B1_Y[1], "Y")
        if "2 b" in title:
            bkgSFHist.SetAxisRange(SF_B2_Y[0], SF_B2_Y[1], "Y")
        bkgSFHist.SetLineWidth(2)
        for binCount in range(N_BINS):
            dataUf = extractUfFromBin(dataHist, binCount+1)
            bkgUf = extractUfFromBin(bkgHist, binCount+1)
            if 0 == bkgUf.val:
                bkgSFHist.SetBinContent(binCount+1,0) # misleading
                print("setting content to 0")
            else:
                bkgSFHist.SetBinContent(binCount+1, (dataUf/bkgUf).val)
            if 0 == bkgUf.sigma:
                bkgSFHist.SetBinError(binCount+1,0) # misleading
                print("setting error to 0")
            else:
                bkgSFHist.SetBinError(binCount+1, (dataUf/bkgUf).sigma)
        leg.AddEntry(bkgSFHist, COMBINATION_STR[histCount], 'l')
        if 0 == mistagInclusive[histCount].val:
            leg.AddEntry(None, "inclusive: " + str(0), '')
        else:
            leg.AddEntry(None, "inclusive: " + str((dataInclusive/mistagInclusive[histCount]).val)[:5] + " #pm " + str((dataInclusive/mistagInclusive[histCount]).sigma)[:5], '')
        SFHists.append(bkgSFHist)
    return SFHists, leg

def generateSavePath(options):
    path = "plots/" 
    if "mt" == options.variable:
        path += "mT/" + "FatJet_pT/" + SM_WH
    else: 
        path += "mCT/" + "FatJet_pT/" + SM_WH
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
#    sys.exit()
    # Plotting
    ROOT.gStyle.SetOptStat(0)
#    ROOT.gROOT.ForceStyle(True)
    SFHistsArr = []
    SFLegs = []
    SFPngNames = []
    for groupCount, fileGroup in enumerate(fileGroups):
        can = ROOT.TCanvas("","",800,800)
        can.Draw()
        hists, leg, mistagInclusive = histsAndLegFromGroup(fileGroup, titles[groupCount])#, options)
#        hists, leg = histsAndLegFromGroup(fileGroup, titles[groupCount])#, options)
        if not isSR(fileGroup[0]): # any index (that exists) will work
##            print(fileGroup[0])
##            print(titles[groupCount])
            SFPngNames.append(pngNames[groupCount])
            SFHist, SFLeg = generateSF(hists, titles[groupCount], mistagInclusive)
            SFHistsArr.append(SFHist)
            SFLegs.append(SFLeg)
        for i, hist in enumerate(hists): 
#            hist.SetMarkerStyle(1)
#            hist.SetMarkerSize(20)
            hist.SetTitle(titles[groupCount] + ";FatJet p_{T} [GeV];mistag efficiencies")
            hist.Draw("SAME")
            hist.Draw("hist same")
#        one = yEqualsOne(min(BINNING), max(BINNING))
#        one.Draw("hist same")
        leg.Draw()
#        print("Saving {} \n".format(savePath + pngNames[groupCount] + ".png"))
        can.SaveAs(savePath + pngNames[groupCount] + ".png")

#    sys.exit()
    for SFCount, SFHists in enumerate(SFHistsArr):
        can = ROOT.TCanvas("","",800,800)
        can.Draw()
        for SFHist in SFHists:
            SFHist.Draw("SAME")
            SFHist.Draw("hist same")
        one = yEqualsOne(min(BINNING), max(BINNING))
        one.Draw("hist same")
        SFLegs[SFCount].Draw()
#        print("Saving {} \n".format(savePath + SFPngNames[SFCount] + "SF.png"))
        can.SaveAs(savePath + SFPngNames[SFCount] + "SF.png")
    
