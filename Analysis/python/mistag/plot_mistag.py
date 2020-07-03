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

YEARS = ["2016", "2017", "2018"]
JETS = ["ngoodjets2", "ngoodjets3"]
BTAGS = ["b0", "b1", "b2"]
REGIONS = [SR, CR]

# This order follows the cxx plotting script
TT_IDX = 1
SINGLE_T_IDX = 2
W_JETS_IDX = 3
TT_V_IDX = 4
DIBOSON_IDX = 5
DATA_IDX = 6 # Data is actually the seventh object on the canvas but we'll deal with that below. See getYields
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
    fileGroups = [[]]
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
    one = ROOT.TD1D("","","",*binningForTH1D)
    one.SetBinContent(1,1)
    one.SetLineColor(ROOT.kBlack)
    return one

def generateHist(title, binning, *argv):
    h = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binning)
    h.SetAxisRange(-0.2, 1.2, "Y")
    h.SetLineWidth(2)
    for i in range(4):
        sum = 0
        for j in argv:
            sum += arr[j][i]
        h.SetBinContent(i+1, arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i] + arr[4][i])
    return h
#                bkg.Draw("hist same")
    
def getIterator(fileName):
    f = ROOT.TFile(fileName):
    assert not f.IsZombie()
    f.cd()
    canvasName = f.GetListOfKeys().At(0).Getname()
    tempCan = f.Get(canvasName)
    can = tempCan.Clone()
    f.Close()
    topPad = canvas.FindObject("mytoppad")
#    topPad.ls()
    topPadList = topPad.GetListOFPrimitives()
    return topPadList.begin() # This is the iterator

# Gets yields by bin of every hist in file
def getYields(fileName):
    yields = numpy.np([[0 for y in range(len(N_BINS))] for x in range(N_BKGS_DATA)])
    inclusive = numpy.np([])
    it = getIterator(fileName):
    for idx in IDXES:
        hist = it.Next()
        if DATA_IDX == idx:
            hist = it.Next() # See definition of DATA_IDX
            if isSR(fileName):
                continue # No Data in SR
        yields[idx][0] = hist.Integral(6,8)   # 125-200
        yields[idx][1] = hist.Integral(9,12)  # 200-300
        yields[idx][2] = hist.Integral(13,16) # 300-400
        yields[idx][3] = hist.Integral(17,80) # 400-2000
        inclusive[idx] = hist.Integral() 
    # Hists in the back contain yields of all others in front of it. The difference is the actual yield 
    for idx in IDXES:
        if ((DATA_IDX == idx) or (DIBOSON_IDX == idx)):
            continue
        yields[idx][0] -= yields[idx+1][0]
        yields[idx][1] -= yields[idx+1][1]
        yields[idx][2] -= yields[idx+1][2]
        yields[idx][3] -= yields[idx+1][3]
        print(yields[idx])
        inclusive[idx] -= inclusive[idx+1]
        print(inclusive[idx])
    print("\n")
    return yields, inclusive

def negativeToZero(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < 0
                arr[i][j] = 0
    return arr

def checkDivideByZero(numer, denom):
    for i in range(len(denom)):
        for j in range(len(denom[i])):
            if 0 == denom[i][j]:
                if not (0 == numer[i][j]):
                    print("Error: Somehow total is zero but Higgs is non-zero")
                    sys.exit()
                denom[i][j] = 1 # Any number is ok since numer/denom = 0
    return denom

def calcMistag(higgsArr, totalArr, combination):
    numer = compress(higgsArr, combination)
    denom = compress(totalARr, combination)
    denom = checkDivideByZero(numer, denom)
    return numer/denom
def histsFromGroup(fileGroup, title, options):
    higgsYields = np.array([[0 for y in range(len(N_BINS))] for x in range(N_BKGS_DATA)])
    totalYields = np.array([[0 for y in range(len(N_BINS))] for x in range(N_BKGS_DATA)])
    higgsInclusive = np.array([for x in range(N_BKGS_DATA)])
    totalInclusive = np.array([for x in range(N_BKGS_DATA)])
    for fileName in fileGroup:
        tempYields, tempInclusive = getYields(fileName)
        if "Higgs" in fileName:
            higgsYield += tempYields
            higgsInclusive += tempInclusive
        else:
            totalYield += tempYields
            totalInclusive += tempInclusive
    higgsYields = negativeToZero(higgsYields)
    totalYields = negativeToZero(totalYields)
    higgsInclusive = negativeToZero(higgsInclusive)
    totalInclusive = negativeToZero(totalInclusive)
    
    mistag = [[]]
    mistagInclusive = []
    combination = [[]]
    if options.combineBkgs:
        combination = [[TT_IDX, SINGLE_T_IDX, TT_V_IDX, W_JETS_IDX, DIBOSON_IDX],
                       [DATA_IDX]]
    else:
        combination = [[TT_IDX, SINGLE_T_IDX, TT_V_IDX], 
                       [W_JETS_IDX, DIBOSON_IDX], 
                       [DATA_IDX]]
    mistag = calcMistag(higgsYield, totalYield, combinations)
    mistagInclusive = calcMistag(higgsInclusive, totalInclusive, combination)

#        numer = compress(higgsYield, [[TT_IDX, SIGNLE_T_IDX, TT_V_IDX], [W_JETS_IDX, DIBOSON], [DATA_IDX]])
#        denom = compress(totalYield, [[TT_IDX, SIGNLE_T_IDX, TT_V_IDX], [W_JETS_IDX, DIBOSON], [DATA_IDX]])
#        denom = checkDivideByZero(numer, denom)
#        mistag = numer/denom
#
#        numerInclusive = compress(higgsInclusive, [[TT_IDX, SIGNLE_T_IDX, TT_V_IDX], [W_JETS_IDX, DIBOSON], [DATA_IDX]])
#        denomInclusive = compress(totalInclusive, [[TT_IDX, SIGNLE_T_IDX, TT_V_IDX], [W_JETS_IDX, DIBOSON], [DATA_IDX]])
#        denomInclusive = checkDivideByZero(numerInclusive, denomInclusive)
#        mistagInclusive = numerInclusive/denomInclusive
                   
            if options.combineBkgs:
#                bkgHist = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binningArgs)
                bkgHist = ROOT.TH1D("", ";MET [GeV];mistag efficiencies", *binningArgs)
                bkgHist.SetAxisRange(-0.2, 1.2, "Y")
                bkgHist.SetLineWidth(2)
                for i in range(4):
                    bkgHist.SetBinContent(i+1, arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i] + arr[4][i])
                bkgHist.Draw("hist same")
            else:
                bkgHist = ROOT.TH1D("", ";MET [GeV];mistag efficiencies", *binningArgs)
                
                bkgHist.SetAxisRange(-0.2, 1.2, "Y")
                bkgHist.SetLineWidth(2)
                for i in range(4):
                    bkgHist.SetBinContent(i+1, arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i] + arr[4][i])
                bkgHist.Draw("hist same")
            



if !noData(fileName):
                    dataHist = ROOT.TH1D("", ";MET [GeV];mistag efficiencies", *binningArgs)
                    dataHist.SetAxisRange(-0.2, 1.2, "Y")
                    dataHist.SetLineWidth(2)
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
    for groupcCount, fileGroup in enumerate(fileGroups):
        can = ROOT.TCanvas("","",500,500)
        can.Draw()
        one = yEqualsOne(min(BINNING), max(BINNING))
        one.Draw()
        hists = histsFromGroup(fileGroup, titles[groupCount], options)
        for hist in hists: 
            hist.Draw()
        can.SaveAs(pngNames[groupCount])
