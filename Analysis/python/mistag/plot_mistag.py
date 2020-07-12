import ROOT
import sys
from optparse import OptionParser
import fnmatch
import array
import numpy as np

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Global definitions

# Set file paths
SR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/g150/root/lin"
CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/l150/root/lin"
for arg in sys.argv:
    if arg.lower() == "mct":
        CR_FILE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mCT/l200/root/lin"

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
TT_IDX = 0
SINGLE_T_IDX = 1
W_JETS_IDX = 2
TT_V_IDX = 3
DIBOSON_IDX = 4
DATA_IDX = 5 # Data is actually the seventh object on the canvas but we'll deal with that below. See getYields
IDXES = [TT_IDX, SINGLE_T_IDX, W_JETS_IDX, TT_V_IDX, DIBOSON_IDX, DATA_IDX]
N_BKGS_DATA = len(IDXES)

BINNING = array.array('d', [125,200,300,400,2000])
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
    parser.add_option("--variable"    , dest = "variable"    , default = "mt" , action = "store"     , help = "Checking for mT or mCT dependence?")
    return parser.parse_args()

# Get files from directories
def getFiles(*argv):
    from os import listdir
    from os.path import isfile, join
    allFiles = []
    for path in argv:
        for f in sorted(listdir(path)):
            full = join(path, f)
            if isfile(full):
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
                    titles[row] += "150 > mT"
                    break
                elif "mt_met_lepl150" == region:
                    titles[row] += "150 > mT > 50"
                    break
                elif "mctg200" == region:
                    titles[row] += "200 > mCT"
                    break
                else:
                    titles[row] += "mCT > 200"
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
    integ = hist.Integral(binLow, binHigh, error)
    return uf(integ, error)
    
# Gets yields by bin of every hist in file
def getYields(fileName):
    yields = np.array([[uf(0.0) for y in range(N_BINS)] for x in range(N_BKGS_DATA)])
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
    for idx in IDXES:
        hist = it.Next()
        if DATA_IDX == idx:
            hist = it.Next() # See definition of DATA_IDX
            if isSR(fileName):
                continue # No Data in SR
        yields[idx][0] = extractUfFromHist(hist, 6, 8)
        yields[idx][1] = extractUfFromHist(hist, 9, 12)
        yields[idx][2] = extractUfFromHist(hist, 13, 16)
        yields[idx][3] = extractUfFromHist(hist, 17, 80)
        inclusive[idx[[0] = 
        yields[idx][0] = hist.Integral(6,8)   # 125-200
        yields[idx][1] = hist.Integral(9,12)  # 200-300
        yields[idx][2] = hist.Integral(13,16) # 300-400
        yields[idx][3] = hist.Integral(17,80) # 400-2000
        inclusive[idx][0] = hist.Integral()
#        print(hist.Integral())
    # Hists in the back contain yields of all others in front of it. The difference is the actual yield 
    for idx in IDXES:
        if ((DATA_IDX == idx) or (DIBOSON_IDX == idx)):
            continue
        yields[idx][0] -= yields[idx+1][0]
        yields[idx][1] -= yields[idx+1][1]
        yields[idx][2] -= yields[idx+1][2]
        yields[idx][3] -= yields[idx+1][3]
        inclusive[idx][0] -= inclusive[idx+1][0]
#        print(yields[idx])
        print(inclusive[idx])
    print("\n")
    return yields, inclusive

def negativeToZero(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].val < 0:
                arr[i][j] = uf(0, arr[i][j].sigma) # check error
    return arr

def compress(oldArr, combination):
    # len(oldArr[any index]) gives number of columns
    newArr = np.array([[uf(0.0,0.0) for y in range(len(oldArr[0]))] for x in range(len(combination))])
    for i, row in enumerate(combination):
        for j in row:
            newArr[i] += oldArr[j]
            print(i)
            print(j)
            print(oldArr[j])
#    print(oldArr)
#    print("newArr")
#    print(newArr)
    return newArr

def checkDivideByZero(numer, denom):
    for i in range(len(denom)):
        for j in range(len(denom[i])):
            if 0 == denom[i][j].val:
                if not (0 == numer[i][j].val):
                    print("Error: Somehow total is zero but Higgs is non-zero")
                    sys.exit()
                denom[i][j] = uf(1, denom[i][j].sigma) # Any number for val is ok since numer/denom = 0 # Check error
                
    return denom

def calcMistag(higgsArr, totalArr, combination):
    numer = compress(higgsArr, combination)
    denom = compress(totalArr, combination)
    denom = checkDivideByZero(numer, denom)
    print(numer)
    print(denom)
    print(numer/denom)
    return numer/denom

def generateHistFromMistag(mistag, color, title = ""):
    h = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *BINNING_FOR_TH1D)
    h.SetAxisRange(-0.2, 1.2, "Y")
    h.SetLineWidth(2)
    h.SetLineColor(color)
    for i, m in enumerate(mistag):
        h.SetBinContent(i+1, m.val)
        h.SetBinError(i+1, m.sigma)
    return h

def histsAndLegFromGroup(fileGroup, title, options):
    higgsYields = np.array([[uf(0.0,0.0) for y in range(N_BINS)] for x in range(N_BKGS_DATA)])
    totalYields = np.array([[uf(0.0,0.0) for y in range(N_BINS)] for x in range(N_BKGS_DATA)])
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
    combination = [[]]
    combinationStr = []
    if options.combineBkgs:
        combination = [[TT_IDX, SINGLE_T_IDX, TT_V_IDX, W_JETS_IDX, DIBOSON_IDX],
                       [DATA_IDX]]
        combinationStr = ['t#tbar{t}, single top, ttV, W + Jets, diboson',
                          'data']
    else:
        combination = [[TT_IDX, SINGLE_T_IDX, TT_V_IDX], 
                       [W_JETS_IDX, DIBOSON_IDX], 
                       [DATA_IDX]]
        combinationStr = ['t#tbar{t}, single top, ttV',
                          'W + jets, diboson',
                          'data']
    mistag = calcMistag(higgsYields, totalYields, combination)
#    print(mistag)
    mistagInclusive = calcMistag(higgsInclusive, totalInclusive, combination)
    print(higgsInclusive)
    print(totalInclusive)
    print(mistagInclusive)
    colors = [ROOT.kBlue+1, ROOT.kRed+1, ROOT.kGreen+1]
    
    # Plotting
    hists = []
    leg = ROOT.TLegend(0.55,0.75,0.9,0.9)
    for i in range(len(mistag)):
        # SR has no data. Skip if SR
        if len(mistag) == (i+1):
            if isSR(fileGroup[0]): # any index will work
                continue
        h = generateHistFromMistag(mistag[i], colors[i], title)
        hists.append(h)
        leg.AddEntry(h, combinationStr[i], 'l')
        inclusiveHist = ROOT.TH1D("","",*BINNING_FOR_TH1D)
        leg.AddEntry(inclusiveHist, "inclusive: " + str(mistagInclusive[i][0]), 'l')
    return hists, leg, combinationStr, mistagInclusive

def generateSavePath(options):
    path = "plots/" 
    if "mt" == options.variable:
        path += "mT/"
    else: 
        path += "mCT/"
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

    # Getting and grouping files
    allFiles = getFiles(SR_FILE_PATH, CR_FILE_PATH)
    fileGroups, grouping = groupFiles(allFiles, options)
    titles = generateTitles(grouping)
    pngNames = generatePngNames(grouping)

    # Plotting
    ROOT.gStyle.SetOptStat(0)
    for groupCount, fileGroup in enumerate(fileGroups):
        can = ROOT.TCanvas("","",500,500)
        can.Draw()
        hists, leg, combinationStr, mistagInclusive = histsAndLegFromGroup(fileGroup, titles[groupCount], options)
        ll = ROOT.TLegend(0.55,0.75,0.9,0.9)
        for i, hist in enumerate(hists): 
            hist.Draw("hist same")
            ll.AddEntry(hist, combinationStr[i] + "\n" + "inclusive:", 'l')
#           inclusiveHist = ROOT.TH1D("",titles[groupCount] + ";MET [GeV];mistag efficiencies",*BINNING_FOR_TH1D)
#           inclusiveHist.SetLineColor(ROOT.kWhite)
            histInc = hist
            histInc.SetLineColor(ROOT.kWhite)
            ll.AddEntry(histInc, "inclusive: " + str(mistagInclusive[i][0]), 'l')
        
#        print(leg)
#        leg.Draw()
        one = yEqualsOne(min(BINNING), max(BINNING))
        one.Draw("hist same")
        ll.Draw()
        print("Saving {} \n".format(generateSavePath(options) + pngNames[groupCount] + ".png"))
        can.SaveAs(generateSavePath(options) + pngNames[groupCount] + ".png")
