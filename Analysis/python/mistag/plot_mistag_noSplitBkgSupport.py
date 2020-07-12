import ROOT
import sys
from optparse import OptionParser
import fnmatch
import array
import numpy as np
from WH_studies.Tools.u_float import u_float as uf

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Global definitions

COMBINATION_STR = []

# Set file paths
SM_WH = ""
for arg in sys.argv:
    if "smwh" in arg.lower():
        SM_WH = "SM_WH/"
SR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/" + SM_WH + "g150/root/lin"
CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/" + SM_WH + "l150/root/lin"
for arg in sys.argv:
    if arg.lower() == "mct":
        CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mCT/" + SM_WH + "l200/root/lin"

VAR = "mt_met_lep"
VAR_THRESHOLD = "150"
for arg in sys.argv:
    if arg.lower() == "mct":
        VAR = "mct"
        VAR_THRESHOLD = "200"
SR = VAR + 'g' + VAR_THRESHOLD
CR = VAR + 'l' + VAR_THRESHOLD

YEARS = ["2016", "2017", "2018"]#, "Comb"]
JETS = ["ngoodjets2", "ngoodjets3"]
BTAGS = ["b0", "b1", "b2"]
REGIONS = [SR, CR]

# This order follows the cxx plotting script
BKG_IDX = 1
DATA_IDX = 6
if not ("" == SM_WH):
    DATA_IDX = 7 # One more bkg means we shift data 
IDEXS = [BKG_IDX, DATA_IDX]
N_BKGS_DATA = len(IDEXS)

BINNING = array.array('d', [125,200,300,400,800])
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
    parser.add_option("--variable"    , dest = "variable"    , default = "mt" , action = "store"     , help = "Checking for mT or mCT dependence?")
    return parser.parse_args()

def setCombination(options):
    #    combination = [[]]
    if options.combineBkgs:
#        combination = [[TT_IDX, SINGLE_T_IDX, TT_V_IDX, W_JETS_IDX, DIBOSON_IDX],
#                       [DATA_IDX]]
        COMBINATION_STR.append('t#bar{t}, single top, ttV, W + Jets, diboson')
        if not ("" == SM_WH):
            COMBINATION_STR[0]+=', SM WH'
        COMBINATION_STR.append('data')
    else:
#        combination = [[TT_IDX, SINGLE_T_IDX, TT_V_IDX], 
#                       [W_JETS_IDX, DIBOSON_IDX], 
#                       [DATA_IDX]]
        COMBINATION_STR.append('t#bar{t}, single top, ttV')
        COMBINATION_STR.append('W + jets, diboson')
        COMBINATION_STR.append('data')


# Get files from directories
def getFiles(*argv):
    from os import listdir
    from os.path import isfile, join
    allFiles = []
    for path in argv:
        for f in sorted(listdir(path)):
            full = join(path, f)
            if isfile(full):
                if not ("yComb" in full):
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
#                print(f[75:])
        fileGroups.append(dummyList)
#        print("\n")
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
    
def getIterator(fileName):
    f = ROOT.TFile(fileName)
    assert not f.IsZombie()
    f.cd()
    canvasName = f.GetListOfKeys().At(0).GetName()
    tempCan = f.Get(canvasName)
    can = tempCan.Clone()
    f.Close()
    topPad = can.FindObject("mytoppad")
    #topPad.ls()
    topPadList = topPad.GetListOfPrimitives()
    return topPadList.begin() # This is the iterator

def extractUfFromHist(hist, binLow, binHigh):
    error = ROOT.Double()
    integ = hist.IntegralAndError(binLow, binHigh, error)
#    if binLow == 17:
#        print("integ: {}".format(integ))
#        print("integ: {}".format(hist.Integral(32,80)))
    return uf(integ, error)
    
# Gets yields by bin of every hist in file
def getYields(fileName):
    yields = np.array([[uf(0.0) for y in range(N_BINS+1)] for x in range(N_BKGS_DATA)]) # +1 for overflow
    inclusive = np.array([[uf(0.0)] for x in range(N_BKGS_DATA)]) # A 1D array also works but 2D ensures compatibility with functions like compress() and negativeToZero()
#    it = getIterator(fileName)
    f = ROOT.TFile(fileName)
    assert not f.IsZombie()
    f.cd()
    canvasName = f.GetListOfKeys().At(0).GetName()
    tempCan = f.Get(canvasName)
    can = tempCan.Clone()
    f.Close()
    topPad = can.FindObject("mytoppad")
    topPadList = topPad.GetListOfPrimitives()
#    topPadList.ls()
    it = topPadList.begin()

    # lumi shapes messed this up
#    hist = it.Next()
#    yields[0][0] = extractUfFromHist(hist, 6, 8)
#    yields[0][1] = extractUfFromHist(hist, 9, 12)
#    yields[0][2] = extractUfFromHist(hist, 13, 16)
#    yields[0][3] = extractUfFromHist(hist, 17, 80)
#    inclusive[0][0] = extractUfFromHist(hist, 1, 80) 
#    for i in range(DATA_IDX-BKG_IDX):
#        hist = it.Next()
#        if not (hist.GetName() == "TPave"):
#            print(hist.GetName() + " " + str(hist.Integral()))

    hist = it.Next()
    yields[0][0] += extractUfFromHist(hist, 6, 8)
    yields[0][1] += extractUfFromHist(hist, 9, 12)
    yields[0][2] += extractUfFromHist(hist, 13, 16)
    yields[0][3] += extractUfFromHist(hist, 17, 80)
    inclusive[0][0] += extractUfFromHist(hist, 1, 80)         
    for i in range(DATA_IDX-BKG_IDX):
        hist = it.Next()
#        print(hist.GetName())
        if i+1 == (DATA_IDX-BKG_IDX):
#            print("Reached data")
            break
        yields[0][0] += extractUfFromHist(hist, 6, 8)
        yields[0][1] += extractUfFromHist(hist, 9, 12)
        yields[0][2] += extractUfFromHist(hist, 13, 16)
        yields[0][3] += extractUfFromHist(hist, 17, 80)
        inclusive[0][0] += extractUfFromHist(hist, 1, 80) 

    if not isSR(fileName):
#        hist = it.Next() # one more iteration for data # lumi shapes fixed this!!!
        yields[1][0] = extractUfFromHist(hist, 6, 8)
        yields[1][1] = extractUfFromHist(hist, 9, 12)
        yields[1][2] = extractUfFromHist(hist, 13, 16)
        yields[1][3] = extractUfFromHist(hist, 17, 80)
        inclusive[1][0] = extractUfFromHist(hist, 1, 80) 
    return yields, inclusive

def negativeToZero(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].val < 0:
                arr[i][j] = uf(0, arr[i][j].sigma) # check error
    return arr

def checkDivideByZero(numer, denom):
    for i in range(len(denom)):
        for j in range(len(denom[i])):
            if 0 == denom[i][j].val:
                if not (0 == numer[i][j].val):
                    print("Error: Somehow total is zero but Higgs is non-zero")
                    sys.exit()
                denom[i][j] = uf(1, denom[i][j].sigma) # Any number for val is ok since numer/denom = 0 # Check error                
    return denom

def calcMistag(higgsArr, totalArr):#, combination):
    #numer = compress(higgsArr, combination)
    #denom = compress(totalArr, combination)
    #denom = checkDivideByZero(numer, denom)
    totalArr = checkDivideByZero(higgsArr, totalArr)
#    print(numer)
#    print(denom)
#    print(numer/denom)
#    return numer/denom
    return higgsArr/totalArr

def generateHistFromMistag(mistag, color, title = ""):
    h = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *BINNING_FOR_TH1D)
#    h.SetAxisRange(-0.2, 1.2, "Y")
    h.SetLineWidth(2)
    h.SetLineColor(color)
    h.GetYaxis().SetTitleOffset(1.4);
    for i, m in enumerate(mistag):
        if i+1 == 5:
            print("overflowing: {}".format(m.val))
        h.SetBinContent(i+1, m.val)
        h.SetBinError(i+1, m.sigma)
    return h

def histsAndLegFromGroup(fileGroup, title, options):
    higgsYields = np.array([[uf(0.0,0.0) for y in range(N_BINS+1)] for x in range(N_BKGS_DATA)]) # +1 for overflow
    totalYields = np.array([[uf(0.0,0.0) for y in range(N_BINS+1)] for x in range(N_BKGS_DATA)]) # +1 for overflow
    higgsInclusive = np.array([[uf(0.0)] for x in range(N_BKGS_DATA)])  # A 1D array also works but 2D ensures compatibility with functions like compress() and negativeToZero()
    totalInclusive = np.array([[uf(0.0)] for x in range(N_BKGS_DATA)])  # A 1D array also works but 2D ensures compatibility with functions like compress() and negativeToZero()
    for fileName in fileGroup:
        tempYields, tempInclusive = getYields(fileName)
        if "Higgs" in fileName:
            higgsYields += tempYields
            higgsInclusive += tempInclusive
        else:
            totalYields += tempYields
            totalInclusive += tempInclusive
    higgsYields = negativeToZero(higgsYields)
    totalYields = negativeToZero(totalYields)
    higgsInclusive = negativeToZero(higgsInclusive)
    totalInclusive = negativeToZero(totalInclusive)

#    for i in range(len(higgsInclusive)):
#        if higgsInclusive[i] < 0:
#            higgsInclusive[i] = 0
#    for i in range(len(totalInclusive)):
#        if totalInclusive[i] < 0:
#            totalInclusive[i] = 0
    
    # Calculating mistags
    mistag = [[]]
    mistagInclusive = [[]] # A 1D array also works but 2D ensures compatibility with functions like compress() and negativeToZero()

    mistag = calcMistag(higgsYields, totalYields)#, combination)
    mistagInclusive = calcMistag(higgsInclusive, totalInclusive)#, combination)

    print(higgsYields)
    print(totalYields)
    print(mistag)
 
    print(higgsInclusive)
    print(totalInclusive)
    print(mistagInclusive)
    colors = [ROOT.kBlue+1, ROOT.kRed+1, ROOT.kGreen+1]
    
    # Plotting
    hists = []
#    ROOT.gStyle.SetLegendFont(42)
#    ROOT.gStyle.SetLegendFillColor(1)
    leg = ROOT.TLegend(0.5,0.75,0.9,0.9)
    for i in range(len(mistag)):
        # SR has no data. Skip if SR
        if len(mistag) == (i+1):
            if isSR(fileGroup[0]): # any index will work
                continue
        h = generateHistFromMistag(mistag[i], colors[i], title)
        hists.append(h)
        leg.AddEntry(h, COMBINATION_STR[i], 'l')
        leg.AddEntry(None, "inclusive: " + str(mistagInclusive[i][0].val)[:5] + " #pm " + str(mistagInclusive[i][0].sigma)[:5], '')
    return hists, leg, mistagInclusive

def extractUfFromBin(hist, bin):
    binContent = hist.GetBinContent(bin)
    error = hist.GetBinError(bin)
    return uf(binContent, error)

def generateSF(hists, title, mistagInclusive):
    # Last index is always for data
    dataHist = hists[-1]
    dataInclusive = mistagInclusive[-1][0]
    SFHists = []
    colors = [ROOT.kBlue+1, ROOT.kRed+1, ROOT.kGreen+1]
    leg = ROOT.TLegend(0.5,0.75,0.9,0.9)
    for histCount, bkgHist in enumerate(hists):
        if len(hists) == histCount+1:
            break # Obviously we don't calculate data/data
        bkgSFHist = ROOT.TH1D("", title + " SF" + ";MET [GeV];Data/MC", *BINNING_FOR_TH1D)
        bkgSFHist.SetLineColor(colors[histCount])
#        bkgSFHist.SetAxisRange(-0.1, 3, "Y")
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
        if 0 == mistagInclusive[histCount][0].val:
            leg.AddEntry(None, "inclusive: " + str(0), '')
        else:
            leg.AddEntry(None, "inclusive: " + str((dataInclusive/mistagInclusive[histCount][0]).val)[:5] + " #pm " + str((dataInclusive/mistagInclusive[histCount][0]).sigma)[:5], '')
        SFHists.append(bkgSFHist)
    return SFHists, leg

def generateSavePath(options):
    path = "plots/" 
    if "mt" == options.variable:
        path += "mT/" + SM_WH
    else: 
        path += "mCT/" + SM_WH
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
    allFiles = getFiles(SR_FILE_PATH, CR_FILE_PATH)
    print("Using {} files".format(len(allFiles)))
    fileGroups, grouping = groupFiles(allFiles, options)
    titles = generateTitles(grouping)
    pngNames = generatePngNames(grouping)
    savePath = generateSavePath(options)

    # Plotting
    ROOT.gStyle.SetOptStat(0)
    SFHistsArr = []
    SFLegs = []
    SFPngNames = []
    for groupCount, fileGroup in enumerate(fileGroups):
        can = ROOT.TCanvas("","",800,800)
        can.Draw()
        hists, leg, mistagInclusive = histsAndLegFromGroup(fileGroup, titles[groupCount], options)
        if not isSR(fileGroup[0]): # any index (that exists) will work
#            print(fileGroup[0])
#            print(titles[groupCount])
            SFPngNames.append(pngNames[groupCount])
            SFHist, SFLeg = generateSF(hists, titles[groupCount], mistagInclusive)
            SFHistsArr.append(SFHist)
            SFLegs.append(SFLeg)
        for i, hist in enumerate(hists): 
#            hist.SetMarkerStyle(1)
#            hist.SetMarkerSize(20)
            hist.Draw("SAME")
            hist.Draw("hist same")
#        one = yEqualsOne(min(BINNING), max(BINNING))
#        one.Draw("hist same")
        leg.Draw()
#        print("Saving {} \n".format(savePath + pngNames[groupCount] + ".png"))
        can.SaveAs(savePath + pngNames[groupCount] + ".png")
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
    
