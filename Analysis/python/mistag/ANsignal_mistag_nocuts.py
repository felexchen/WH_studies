import ROOT
import sys
from optparse import OptionParser
import fnmatch
import array
import numpy as np
from WH_studies.Tools.asym_float import asym_float as af
from RootTools.core.standard import *

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Global definitions

COLORS = [ROOT.kBlue+1, ROOT.kRed+1, ROOT.kGreen+1, ROOT.kYellow+1, ROOT.kOrange+1, ROOT.kViolet+1]

COMBINATION_STR = []

# Set file paths
SM_WH = ""
for arg in sys.argv:
    if "smwh" in arg.lower():
        SM_WH = "SM_WH/"
Gen = ""
for arg in sys.argv:
    if "gen" in arg.lower():
        Gen = "Gen_H/"
SR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/" + Gen + SM_WH + "g150/root/lin"
CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/" + Gen + SM_WH + "l150/root/lin"
for arg in sys.argv:
    if arg.lower() == "mct":
        CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mCT/ANsignal/FatJet_pT/" + Gen + SM_WH + "l200/root/lin"

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
N_Bs = len(BTAGS)
if not ("" == Gen):
    N_Bs = 1
REGIONS = [SR, CR]

# This order follows the cxx plotting script
BKG_IDX = 1
SIGNAL_750_1_FAST = 3
SIGNAL_350_100_FAST = 4
SIGNAL_750_1_FULL = 5
SIGNAL_350_100_FULL = 6
DATA_IDX = 7
#if not ("" == SM_WH):
#    # 1 more bkg means every non-bkg shifts down 1
#    SIGNAL_DELTA_250 += 1
#    SIGNAL_DELTA_250_500 += 1
#    SIGNAL_DELTA_500 += 1
##    SIGNAL_ALL_MASS += 1
##    SIGNAL_ALL += 1
##    SIGNAL_700_1 += 1
##    SIGNAL_650_300 += 1
##    SIGNAL_225_75 += 1
#    DATA_IDX += 1
#IDEXS = [BKG_IDX, SIGNAL_ALL_MASS, SIGNAL_ALL, SIGNAL_700_1, SIGNAL_650_300, SIGNAL_225_75, DATA_IDX]
#IDEXS = [BKG_IDX, SIGNAL_ALL_MASS, SIGNAL_ALL, DATA_IDX]
IDEXS = [BKG_IDX, SIGNAL_750_1_FAST, SIGNAL_350_100_FAST, SIGNAL_750_1_FULL, SIGNAL_350_100_FULL]#, DATA_IDX]
N_BKGS_DATA = len(IDEXS)

BINNING = array.array('d', [200,300,400,500,600,700,800,2000])#1750])
N_BINS = len(BINNING)-1
BINNING_FOR_TH1D = (N_BINS, BINNING)

B0_Y = [0, 0.1]
B1_Y = [0, 1]
B2_Y = [0.5, 1.1]

SF_B0_Y = [-4, 10]
SF_B1_Y = [0, 3]
SF_B2_Y = [0.8, 1.2]
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
    parser.add_option("--Gen"         , dest = "Gen"         , default = False, action = "store_true", help = "Use only Fat Jets with Gen H's inside?")
    parser.add_option("--variable"    , dest = "variable"    , default = "mt" , action = "store"     , help = "Checking for mT or mCT dependence?")
    return parser.parse_args()

def setCombination(options):
    if options.combineBkgs:
        COMBINATION_STR.append('t#bar{t}, single top, ttV, W + Jets, diboson')
        if not ("" == SM_WH):
            COMBINATION_STR[0]+=', SM WH'
#        COMBINATION_STR.append('signal (750, 1) FastSim')
#        COMBINATION_STR.append('signal (350, 100) FastSim')
#        COMBINATION_STR.append('signal (750, 1) FullSim')
#        COMBINATION_STR.append('signal (350, 100) FullSim')
        COMBINATION_STR.append('FastSim (750, 1)')
        COMBINATION_STR.append('FastSim (350, 100)')
        COMBINATION_STR.append('FullSim (750, 1)')
        COMBINATION_STR.append('FullSim (350, 100)')
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
    print Gen
    if ("" == Gen):
        if not options.combineBTags:
            grouping = expandList(grouping, BTAGS)
    else:
        for i in range(len(grouping)):
            grouping[i] += "*250g"
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
                print(f[20:])
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
        if ("" == Gen):
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
        if ("" == Gen):
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

def is2017(fileName):
    # SR does not have full sim
    if("2017" in fileName):
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

originalplots = []
originalnames = []
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
    if inclusive:
        err = ROOT.Double()
        singleBin = [min(BINNING), max(BINNING)]
        singleBinning = (1, array.array('d', singleBin))
#        histCombinedBin = ROOT.TH1D(hist.GetName(), "", *singleBinning)
        histCombinedBin = ROOT.TH1D("", "", *singleBinning)
        histCombinedBin.SetBinContent(1, hist.IntegralAndError(1, 7, err))
        histCombinedBin.SetBinError(1, err)
        return histCombinedBin
    else:
#        histCombinedBin = ROOT.TH1D(hist.GetName(), "", *BINNING_FOR_TH1D)
        histCombinedBin = ROOT.TH1D("", "", *BINNING_FOR_TH1D)
#        print hist.GetBinContent(5)
        for binCount in range(N_BINS):
#            if 1 == binCount:
#                err = ROOT.Double()
#                histCombinedBin.SetBinContent(2, hist.IntegralAndError(2, 4, err))
#                histCombinedBin.SetBinError(2, err)
#                break
            histCombinedBin.SetBinContent(binCount+1, hist.GetBinContent(binCount+1))
            histCombinedBin.SetBinError(binCount+1, hist.GetBinError(binCount+1))
        if (3 == idx) or (4 == idx) or (5 == idx) or (6 == idx):
            if not ("Higgs" in fileName):
                print "\n\n\nfound original plots\n\n\n"
                print hist.GetName()
                print fileName
                originalplots.append(histCombinedBin)
                originalnames.append(hist.GetName())
        return histCombinedBin

def generateMistagHistAndInclusive(passed, total, idx, title, color):
    passedCombinedBin = combineBins(passed, idx)
    totalCombinedBin = combineBins(total, idx)
    passedInclusive = combineBins(passed, idx, inclusive = True)
    totalInclusive = combineBins(total, idx, inclusive = True)
    if 1 == idx:
        return ROOT.TGraphAsymmErrors(), af(0,0,0)
#    if passedCombinedBin.GetBinContent(4) > totalCombinedBin.GetBinContent(4):
#        totalCombinedBin.SetBinContent(4, passedCombinedBin.GetBinContent(4))
    if ROOT.TEfficiency.CheckConsistency(passedCombinedBin, totalCombinedBin) and ROOT.TEfficiency.CheckConsistency(passedInclusive, totalInclusive):
        teff = ROOT.TEfficiency(passedCombinedBin, totalCombinedBin)
        teff.Paint("") # AP is default but still needs to be passed..
        graphCopy = teff.GetPaintedGraph()
        graph = ROOT.TGraphAsymmErrors(graphCopy.GetN())
#        graph.SetName(passedCombinedBin.GetName())
        graph.GetXaxis().SetLimits(200.,1000.)
#        print graphCopy.GetN()
        x = ROOT.Double()
        y = ROOT.Double()
        for i in range(graphCopy.GetN()):
            graphCopy.GetPoint(i,x,y)
            graph.SetPoint(i, x, y)#graphCopy.GetPointX(i), graphCopy.GetPointY(i))
#            graph.SetPointError(i, graphCopy.GetErrorXlow(i), graphCopy.GetErrorXhigh(i), graphCopy.GetErrorYlow(i), graphCopy.GetErrorYhigh(i))
            graph.SetPointError(i, 0, 0, graphCopy.GetErrorYlow(i), graphCopy.GetErrorYhigh(i))
#        mistagHist = ROOT.TH1D("", title + ";FatJet p_{T} [GeV];mistag efficiencies", *BINNING_FOR_TH1D) 
        graph.SetTitle(title + ";FatJet p_{T} [GeV];mistag efficiencies")        
        if "0 b" in title:
            # to check for negativity
#            graph.GetPoint(0, x, y)
#            print y
#            print graph.GetErrorYlow(0)
#            print str(y - graph.GetErrorYlow(0))
#            graph.GetPoint(1, x, y)
#            print y            
#            print graph.GetErrorYlow(1)
#            print str(y - graph.GetErrorYlow(1))
#            mistagHist.SetAxisRange(B0_Y[0], B0_Y[1], "Y")
            graph.SetMinimum(B0_Y[0])
            graph.SetMaximum(B0_Y[1])
        elif "1 b" in title:
            graph.SetMinimum(B1_Y[0])
            graph.SetMaximum(B1_Y[1])
        #            mistagHist.SetAxisRange(B1_Y[0], B1_Y[1], "Y")
        elif "2 b" in title:
            graph.SetMinimum(B2_Y[0])
            graph.SetMaximum(B2_Y[1])
#            graph.GetYAxis().SetTitle(B2_Y[0], B2_Y[1])
            #            mistagHist.SetAxisRange(B2_Y[0], B2Y[1], "Y")
        graph.SetLineWidth(2)
        graph.SetLineColor(color)
        graph.GetYaxis().SetTitleOffset(1.4);
#          print graph.GetN()
#        for i in range(graph.GetN()):
#            x = ROOT.Double()
#            y = ROOT.Double()
#            graph.GetPoint(i, x, y)
#     #       print i 
#            mistagHist.SetBinContent(i+1, y)
#            e = graph.GetErrorY(i)
#            mistagHist.SetBinError(i+1, e)#graph.GetErrorY(i))
#            if i == 1:
#                print "{} {} {}".format(idx, y, e)
        incTeff = ROOT.TEfficiency(passedInclusive, totalInclusive)
        incTeff.Paint("")
        incGraph = incTeff.GetPaintedGraph()
        dummy = ROOT.Double()
        inclusive = ROOT.Double()
        incGraph.GetPoint(0, dummy, inclusive)
        inclusiveUncertaintyLow = incGraph.GetErrorYlow(0)
        inclusiveUncertaintyHigh = incGraph.GetErrorYhigh(0)
        #        return mistagHist, inclusive, inclusiveUncertainty
        return graph, af(inclusive, inclusiveUncertaintyHigh, inclusiveUncertaintyLow)
    else:
        print "idx: {}".format(idx)
#        print "hello"
        for i in range(N_BINS):
            print passedCombinedBin.GetBinContent(i+1)
            print totalCombinedBin.GetBinContent(i+1)
        print("ERROR: inconsistent!\n{}\n{}".format(passed, total))
#        for binCount in range(N_BINS):
#            print passedCombinedBin.GetBinContent(binCount+1)
#            print totalCombinedBin.GetBinContent(binCount+1)
        sys.exit()

def histsAndLegFromGroup(fileGroup, title):#, options):
    # fileGroup has two files. ALWAYS
#    print sorted(fileGroup)
    print("\n\n\n\n\n")
    print fileGroup
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
#                print "FOUND SR"
                continue
        if ((SIGNAL_750_1_FULL == idx) or (SIGNAL_350_100_FULL == idx)):
            if is2017(fileGroup[0]): # any index will work
                continue # 2017 does hot have full
#        print("idx: {}".format(idx))
        if is2017(fileGroup[0]) and DATA_IDX == idx:
            h, mistagInclusive = generateMistagHistAndInclusive(passed, total, 9, title, COLORS[i]) 
        else:
            h, mistagInclusive = generateMistagHistAndInclusive(passed, total, idx, title, COLORS[i]) 
        mistagInclusives.append(mistagInclusive)
        hists.append(h)
        leg.AddEntry(h, COMBINATION_STR[i], 'l')
        leg.AddEntry(None, "inclusive: " + str(mistagInclusive.central)[:5] + " + " + str(mistagInclusive.up)[:5], '')
        leg.AddEntry(None, "inclusive: " + str(mistagInclusive.central)[:5] + " - " + str(mistagInclusive.down)[:5], '')
#    return hists, leg#, mistagInclusive
    print mistagInclusives
    return hists, leg, mistagInclusives

def extractAfFromBin(hist, bin):
    dummy = ROOT.Double()
    central = ROOT.Double()
    hist.GetPoint(bin, dummy, central)
    down = hist.GetErrorYlow(bin)
    up = hist.GetErrorYhigh(bin)
    return af(central, up, down)

def generateSF(hists, title, mistagInclusive):
    # Last index is always for data
    dataHist = hists[-1]
    dataInclusive = mistagInclusive[-1]
    SFHists = []
    leg = ROOT.TLegend(0.5,0.75,0.9,0.9)
    for histCount, bkgHist in enumerate(hists):
#        if len(hists) == histCount+1:
        if 0 < histCount:
            break # Obviously we don't calculate data/data (and signal since we get them)

        bkgSFHist = ROOT.TGraphAsymmErrors(N_BINS)
        bkgSFHist.GetYaxis().SetTitleOffset(1.4);
#        bkgSFHist = ROOT.TH1D("", title + " SF" + ";FatJet p_{T} [GeV];Data/MC", *BINNING_FOR_TH1D)
        bkgSFHist.SetLineColor(COLORS[histCount])
        bkgSFHist.SetTitle(title + " SF;FatJet p_{T} [GeV];Data/MC")        
        if "0 b" in title:
            bkgSFHist.SetMinimum(SF_B0_Y[0])
            bkgSFHist.SetMaximum(SF_B0_Y[1])
#            bkgSFHist.SetAxisRange(SF_B0_Y[0], SF_B0_Y[1], "Y")
        if "1 b" in title:
            bkgSFHist.SetMinimum(SF_B1_Y[0])
            bkgSFHist.SetMaximum(SF_B1_Y[1])

#            bkgSFHist.SetAxisRange(SF_B1_Y[0], SF_B1_Y[1], "Y")
        if "2 b" in title:
            bkgSFHist.SetMinimum(SF_B2_Y[0])
            bkgSFHist.SetMaximum(SF_B2_Y[1])

#            bkgSFHist.SetAxisRange(SF_B2_Y[0], SF_B2_Y[1], "Y")
        bkgSFHist.SetLineWidth(2)
        for binCount in range(N_BINS):
            dataUf = extractAfFromBin(dataHist, binCount)#+1)
            bkgUf = extractAfFromBin(bkgHist, binCount)#+1)
            frac = af(0,0,0)
            if not (0 == bkgUf.central):
                frac = dataUf/bkgUf
            x = ROOT.Double()
            dummy = ROOT.Double()
            bkgHist.GetPoint(binCount, x, dummy)
#            if 0 == bkgUf.central:
#                print "Setting to 0 SF"
#                bkgSFHist.SetPoint(binCount, x, 0) # misleading
#                bkgSFHist.SetPointError(binCount, 0, 0, 0, 0) # misleading
#            else:
            bkgSFHist.SetPoint(binCount, x, frac.central)#(dataUf/bkgUf).central)
            bkgSFHist.SetPointError(binCount, 0, 0, frac.down, frac.up)#(dataUf/bkgUf).down, (dataUf/bkgUf).up)
            #print (dataUf/bkgUf).down
            #print (dataUf/bkgUf).up
            #if (dataUf/bkgUf).up == 0.0:
            #    print binCount
            #    print dataUf
            #    print bkgUf
                          #if 0 == bkgUf.val:
            #    bkgSFHist.SetBinContent(binCount+1,0) # misleading
            #    print("setting content to 0")
            #else:
            #    bkgSFHist.SetBinContent(binCount+1, (dataUf/bkgUf).val)
            #if 0 == bkgUf.sigma:
            #    bkgSFHist.SetBinError(binCount+1,0) # misleading
            #    print("setting error to 0")
            #else:
            #    bkgSFHist.SetBinError(binCount+1, (dataUf/bkgUf).sigma)
        leg.AddEntry(bkgSFHist, COMBINATION_STR[histCount], 'l')
        if 0 == mistagInclusive[histCount].central:# misleading
            leg.AddEntry(None, "inclusive: " + str(0) + " + " + str(0), '')
            leg.AddEntry(None, "inclusive: " + str(0) + " - " + str(0), '')
        else:
            leg.AddEntry(None, "inclusive: " + str((dataInclusive/mistagInclusive[histCount]).central)[:5] + " + " + str((dataInclusive/mistagInclusive[histCount]).up)[:5], '')
            leg.AddEntry(None, "inclusive: " + str((dataInclusive/mistagInclusive[histCount]).central)[:5] + " - " + str((dataInclusive/mistagInclusive[histCount]).down)[:5], '')
        SFHists.append(bkgSFHist)
    return SFHists, leg

def generateSavePath(options):
    path = "plots/" 
    if "mt" == options.variable:
        path += "mT/" + "ANsignal/" + "FatJet_pT/" + SM_WH + Gen
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

def generateSignalSFs(fileName, options):
    YEAR = 0
    WP = 1
    PTMIN = 2
    PTMAX = 3
    CENTRAL = 4
    DOWN = 5
    UP = 6
    nBins = 5
    binning = [200,300,400,500,600,1000]
    nYears = 3
    arr2D = []
    with open(fileName) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if 0 == i:
                continue # first line is a description
            if not ("mp" in line):
                continue # only want "middle"? working point
            dummy = []
            for token in line.split():
                dummy.append(token)
            arr2D.append(dummy)
        f.close()
    graphs = []
    for year in range(nYears):
        graph = ROOT.TGraphAsymmErrors(nBins)
        for bin in range(nBins):
            graph.SetPoint(bin, (binning[bin+1]+binning[bin])/2, float(arr2D[bin+(year*nBins)][CENTRAL]))
            graph.SetPointError(bin, 0, 0, float(arr2D[bin+(year*nBins)][DOWN]), float(arr2D[bin+(year*nBins)][UP]))
        graph.SetTitle("201" + str(year+6) + " Signal SF;FatJet p_{T} [GeV];Data/MC")
        if 0 == year:
            graph.SetMinimum(0.8)
            graph.SetMaximum(1.2)
        elif 1 == year:
            graph.SetMinimum(0.8)
            graph.SetMaximum(1.2)
        elif 2 == year:
            graph.SetMinimum(1.1)
            graph.SetMaximum(1.4)
        graph.SetLineWidth(2)
        graph.SetLineColor(ROOT.kRed+1)
        graph.GetYaxis().SetTitleOffset(1.4);
        graphs.append(graph)
    return graphs

def drawSig(graphs, inclusives, title, pngName, p1, p2, name1, name2):
    can = ROOT.TCanvas("","",800,800)
    can.Draw()
    th1ds = []
    leg = ROOT.TLegend(0.5,0.78,0.9,0.9)
#    for graphCount, graph in enumerate(graphs):
#        # resetting things
#        graph.SetLineColor(COLORS[graphCount])
#        graph.SetTitle(title + ";FatJet p_{T} [GeV];tagging efficiencies")
#        graph.SetMinimum(0)
#        graph.SetMaximum(50)
##        if 0 == graphCount:
##            graph.Draw("AP")
##        else:
##            graph.Draw("P")
#        ROOT.gPad.Modified()
#        ROOT.gPad.Update()
#        graph.GetXaxis().SetLimits(200.,1000.)
#        ROOT.gPad.Modified()
#        ROOT.gPad.Update()
    for graphCount, graph in enumerate(graphs):
        h = ROOT.TH1D("", title + ";FatJet p_{T} [GeV];tagging efficiencies", *BINNING_FOR_TH1D)
        x = ROOT.Double()
        y = ROOT.Double()
        for binCount in range(N_BINS):
            graph.GetPoint(binCount, x, y)
            h.SetBinContent(binCount+1, y)
            h.SetBinError(binCount+1, graph.GetErrorYlow(binCount))
            print graph.GetErrorYlow(binCount)
            print graph.GetErrorYhigh(binCount)
            if not (graph.GetErrorYlow(binCount) == graph.GetErrorYhigh(binCount)):
                print "error high and error low are different!"
                sys.exit()
        h.SetLineWidth(2)
        h.SetLineColor(COLORS[graphCount])
        h.legendText = COMBINATION_STR[graphCount+1] + ": " + str(inclusives[graphCount].central)[:5] + " #pm " + str(inclusives[graphCount].up)[:5]
#        h.SetTextSize(50)
        h.style = styles.lineStyle(COLORS[graphCount], errors = True)
        th1ds.append(h)
        
        leg.AddEntry(h, COMBINATION_STR[graphCount+1] + ": " + str(inclusives[graphCount].central)[:5] + " #pm " + str(inclusives[graphCount].up)[:5], 'l')
#        leg.AddEntry(None, "inclusive: " + str(inclusives[graphCount].central)[:5] + " #pm " + str(inclusives[graphCount].up)[:5], '')
#        leg.AddEntry(h, graph.GetName(), 'l')
        if not (str(inclusives[graphCount].up)[:5] == str(inclusives[graphCount].down)[:5]):
            print "assymetric error!"
            sys.exit()
#        leg.AddEntry(None, "inclusive: " + str(inclusives[graphCount].central)[:5] + " + " + str(inclusives[graphCount].up)[:5], '')
#        leg.AddEntry(None, "inclusive: " + str(inclusives[graphCount].central)[:5] + " - " + str(inclusives[graphCount].down)[:5], '')    
#    for h in th1ds:
#        h.Draw("SAME")
#        h.Draw("hist same")
    one = yEqualsOne(min(BINNING), max(BINNING))
#    one.Draw("hist same")
    leg.Draw()
    can.SaveAs(savePath + pngName + ".png")    

    p1.Scale(1/p1.Integral())
    p2.Scale(1/p2.Integral())
    p1.SetLineColor(COLORS[4])
    p2.SetLineColor(COLORS[5])
    p1.SetLineStyle(1)
    p2.SetLineStyle(2)
    p1.SetLineWidth(2)
    p2.SetLineWidth(2)
    print name1
    print name2
    if "fast" in name1.lower():
        p1.legendText = "FastSim (750,1) p_{T} spectrum"
        p2.legendText = "FastSim (350,100) p_{T} spectrum"
    else:
        p1.legendText = "FullSim (750,1) p_{T} spectrum"
        p2.legendText = "FullSim (350,100) p_{T} spectrum"
        
    if not ("2017" in pngName):
#        for th in th1ds:
#            th.SetTitle("das")
        print th1ds
        plotting.draw(
            Plot.fromHisto(name = pngName + "_ratio", histos = [ [th1ds[0]], [th1ds[1]], [th1ds[2]], [th1ds[3]], [p1], [p2] ], texX = "FatJet p_{T} (GeV)", texY = "Tagging Efficiencies"),
#            plot_directory = "./plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/",
            plot_directory = "./noCuts/",
            logX = False, logY = False, sorting = False,
            yRange = (0,1),
            legend = (0.4, 0.2, 0.9, 0.4),
            scaling = {1:0},
            ratio = {'histos': [(2,0), (3,1)], 'texY': 'Full / Fast', 'yRange': (0.6, 1.4)},
            title = "das",
            ) 
    else:
        for th in th1ds:
            th.SetTitle("das")
        print th1ds
        plotting.draw(
            Plot.fromHisto(name = pngName + "_ratio", histos = [ [th1ds[0]], [th1ds[1]], [p1], [p2] ], texX = "FatJet p_{T} (GeV)", texY = "Tagging Efficiencies"),
            #plot_directory = "./plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/",
            plot_directory = "./noCuts/",
            logX = False, logY = False, sorting = False,
            yRange = (0,1),
            legend = (0.4, 0.2, 0.9, 0.4),
            scaling = {1:0},
            title = "das",
#            ratio = {'histos': [(2,0), (3,1)], 'texY': 'Full / Fast'},
            ) 
    
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if __name__ == "__main__":

    # Parsing command line
    (options, args) = addCmdlineOptions()
    setCombination(options)
    print(COMBINATION_STR)

    # Getting and grouping files
    allFiles = getFiles(options, SR_FILE_PATH, CR_FILE_PATH)
    print("Using {} files".format(len(allFiles)))
    for f in allFiles:
        print f
#    fileGroups, grouping = groupFiles(allFiles, options)
    grouping = [["*2016*"],
                ["*2017*"],
                ["*2018*"]
                ]
    fileGroups = [["/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root",
                   "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root"
                   ],
                  ["/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root",
                   "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root"
                   ],
                  ["/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root",
                   "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root"
                   ]
                  ]
    print("Actually using {} files".format(len(fileGroups)*len(fileGroups[0])))
#    titles = generateTitles(grouping)
    titles = ["2016",
              "2017",
              "2018"
              ]
    for i, title in enumerate(titles):
        print("{:2} {}".format(i, title))
#    pngNames = generatePngNames(grouping)
    pngNames = ["2016",
                "2017",
                "2018"
                ]
    for i, pngName in enumerate(pngNames):
        print("{:2} {}".format(i, pngName))
#    savePath = generateSavePath(options)
    savePath = "./noCuts/"
    print savePath
#    sys.exit()



    # Plotting
    ROOT.gStyle.SetOptStat(0)
    SFHistsArr = []
    SFLegs = []
    SFPngNames = []
    sigslow = []
    sigsinclow = []
    sigshigh = []
    sigsinchigh = []
    for groupCount, fileGroup in enumerate(fileGroups):
        sig = []
        siginc = []
        can = ROOT.TCanvas("","",800,800)
        can.Draw()
        hists, leg, mistagInclusive = histsAndLegFromGroup(fileGroup, titles[groupCount])#, options)
        if not isSR(fileGroup[0]): # any index (that exists) will work
            SFPngNames.append(pngNames[groupCount])
            SFHist, SFLeg = generateSF(hists, titles[groupCount], mistagInclusive)
            SFHistsArr.append(SFHist)
            SFLegs.append(SFLeg)
        #print hists
        sig.append(hists[1])
        sig.append(hists[2])
        if not is2017(fileGroup[0]):
            sig.append(hists[3])
            sig.append(hists[4])
#        print sig
        siginc.append(mistagInclusive[1])
        siginc.append(mistagInclusive[2])
        if not is2017(fileGroup[0]):
            siginc.append(mistagInclusive[3])
            siginc.append(mistagInclusive[4])

        if not isSR(fileGroup[0]):
            sigslow.append(sig)
            sigsinclow.append(siginc)
        else:
            sigshigh.append(sig)
            sigsinchigh.append(siginc)
        for i, hist in enumerate(hists):
            if (1 == i) or (2 == i):
                continue # separating background and signal
            if 0 == i:
                hist.Draw("AP")
            else:
                hist.Draw("P")
            ROOT.gPad.Modified()
            ROOT.gPad.Update()
            hist.GetXaxis().SetLimits(200.,1000.)
            ROOT.gPad.Modified()
            ROOT.gPad.Update()
        th1ds = []
        for i, hist in enumerate(hists): 
            if (1 == i) or (2 == i):
                continue # separating background and signal
            h = ROOT.TH1D("", titles[groupCount] + ";FatJet p_{T} [GeV];mistag efficiencies", *BINNING_FOR_TH1D)
            x = ROOT.Double()
            y = ROOT.Double()
            for binCount in range(N_BINS):
                hist.GetPoint(binCount, x, y)
                h.SetBinContent(binCount+1, y)
            h.SetLineWidth(2)
            h.SetLineColor(COLORS[i])
            th1ds.append(h)
        for h in th1ds:
            h.Draw("hist same")
        leg.Draw()
#        can.SaveAs(savePath + pngNames[groupCount] + ".png")

    for siglow in sigslow:
        print siglow
    for sighigh in sigshigh:
        print sighigh
    for siginclow in sigsinclow:
        print siginclow
    for siginchigh in sigsinchigh:
        print siginchigh

#    sys.exit()

    # I don't think I need columns
#    fast_750_1 = 0
#    fast_350_100 = 1
#    full_750_1 = 2
#    full_350_100 = 3
    print
    years = ["2016", "2017", "2018"]
#    for i, year in enumerate(years):
#drawSig(sigslow[i] , sigsinclow[i] , str(year) + " 150 > mT", "signal_" + str(year) + "_low_tag")
    drawSig(sigslow[0] , sigsinclow[0] , "2016" + " 150 > mT", "signal_" + "2016" + "_low_tag", originalplots[2], originalplots[3], originalnames[2], originalnames[3])
    drawSig(sigslow[1] , sigsinclow[1] , "2017" + " 150 > mT", "signal_" + "2017" + "_low_tag", originalplots[4], originalplots[5], originalnames[4], originalnames[5])
    drawSig(sigslow[2] , sigsinclow[2] , "2018" + " 150 > mT", "signal_" + "2018" + "_low_tag", originalplots[8], originalplots[9], originalnames[8], originalnames[9])
#        drawSig(sigshigh[i], sigsinchigh[i], str(year) + " mT > 150", "signal_" + str(year) + "_high_tag")
    print originalplots
    print originalnames
    sys.exit()

    delta_500 = 0
    delta_250_500 = 1
    delta_250 = 2
    if "" == Gen:
        drawSig(sigslow , sigsinclow , delta_500    , "150 > mT > 50", "signal_500_low_mistag")
        drawSig(sigslow , sigsinclow , delta_250_500, "150 > mT > 50", "signal_250_500_low_mistag")
        drawSig(sigslow , sigsinclow , delta_250    , "150 > mT > 50", "signal_250_low_mistag")
        drawSig(sigshigh, sigsinchigh, delta_500    , "mT > 150"     , "signal_500_high_mistag")
        drawSig(sigshigh, sigsinchigh, delta_250_500, "mT > 150"     , "signal_250_500_high_mistag")
        drawSig(sigshigh, sigsinchigh, delta_250    , "mT > 150"     , "signal_250_high_mistag")
    else:
        sigslow.append([sigslow[0][1]])
        sigslow.append([sigslow[0][2]])
        sigshigh.append([sigshigh[0][1]])
        sigshigh.append([sigshigh[0][2]])
        sigsinclow.append([sigsinclow[0][1]])
        sigsinclow.append([sigsinclow[0][2]])
        sigsinchigh.append([sigsinchigh[0][1]])
        sigsinchigh.append([sigsinchigh[0][2]])
        drawSig(sigslow, sigsinclow, 0, "150 > mT > 50", "signal_low_mistag") 
        drawSig(sigshigh, sigsinchigh, 0, "mT > 150", "signal_high_mistag") 
    sys.exit()






    for SFCount, SFHists in enumerate(SFHistsArr):
        can = ROOT.TCanvas("","",800,800)
        can.Draw()
        for i, SFHist in enumerate(SFHists):
            if 0 == i:
                SFHist.Draw("AP")
            else:
                SFHist.Draw("P")
            ROOT.gPad.Modified()
            ROOT.gPad.Update()
            SFHist.GetXaxis().SetLimits(200.,1000.)
            ROOT.gPad.Modified()
            ROOT.gPad.Update()

        th1ds = []
        for i, SFHist in enumerate(SFHists):
            h = ROOT.TH1D("", titles[groupCount] + " SF;FatJet p_{T} [GeV];Data/MC", *BINNING_FOR_TH1D)
            x = ROOT.Double()
            y = ROOT.Double()
            for binCount in range(N_BINS):
                SFHist.GetPoint(binCount, x, y)
                h.SetBinContent(binCount+1, y)
            h.SetLineWidth(2)
#            h.SetAxisRange(0,1,"Y")
            h.SetLineColor(COLORS[i])
            th1ds.append(h)
        for h in th1ds:
            h.Draw("hist same")
        SFLegs[SFCount].Draw()
        one = yEqualsOne(min(BINNING), max(BINNING))
        one.Draw("hist same")

#        print("Saving {} \n".format(savePath + SFPngNames[SFCount] + "SF.png"))
        can.SaveAs(savePath + SFPngNames[SFCount] + "SF.png")
    
    signalSFs = generateSignalSFs("deepak8v2_bbvslight.csv", options)    
    for signalSFCount, signalSF in enumerate(signalSFs):
        can = ROOT.TCanvas("","",800,800)
        can.Draw()
        signalSF.Draw("AP")
        ROOT.gPad.Modified()
        ROOT.gPad.Update()
        signalSF.GetXaxis().SetLimits(200.,1000.)
        ROOT.gPad.Modified()
        ROOT.gPad.Update()

        binning = [200,300,400,500,600,1000]
        binningForTH1D = (len(binning)-1, array.array('d', binning))

        h = ROOT.TH1D("", "Signal SF;FatJet p_{T} [GeV];Data/MC", *binningForTH1D)
        x = ROOT.Double()
        y = ROOT.Double()
        for i in range(5):
            signalSF.GetPoint(i, x, y)
            h.SetBinContent(i+1, y)
        h.SetLineWidth(2)
        h.SetLineColor(ROOT.kRed+1)
        h.Draw("hist same")
        one = yEqualsOne(min(BINNING), max(BINNING))
        one.Draw("hist same")
#        if len(signalSFs) == 0:
#            can.SaveAs(savePath + "yComb" + "signalSF.png")
 #       else:
        can.SaveAs(savePath + "201" + str(signalSFCount+6) + "signalSF.png")
    
