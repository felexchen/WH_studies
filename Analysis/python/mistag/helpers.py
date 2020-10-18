import ROOT
ROOT.gStyle.SetOptStat(0)
import sys
from optparse import OptionParser
import array
#import numpy as np
from WH_studies.Tools.asym_float import asym_float as af

YEARS = ["y2016", "y2017", "y2018"]
JETS = ["ngoodjets2", "ngoodjets3"]
BTAGS = ["b0", "b1", "b2"]
REGIONS = ["mt_met_lepg150", "mt_met_lepl150", "mctg200", "mctl200"] # Fix this. mt > 150 and mCT > 200 are pretty much the same thing
COLORS = [ROOT.kBlue+1, ROOT.kRed+1, ROOT.kGreen+1, ROOT.kYellow+1, ROOT.kOrange+1, ROOT.kViolet+1]
SM_WH = ""
GEN_H = ""
def pVars():
    print SM_WH
    print GEN_H

def appendToPath(path, directory):
    return path + "/" + directory + "/"

def printNewLines(nTimes = 0):
    for i in range(nTimes):
        print "\n"

def printDashes(nDashes = 0):
    dashes = ""
    for i in range(nDashes):
        dashes += '-'
    if 0 < nDashes:
        print dashes

# Add command line options
def addCmdlineOptions():
    parser = OptionParser()
    parser.add_option("--combineYears", dest = "combineYears", default = False      , action = "store_true", help = "Combine 2016, 2017, and 2018?")
    parser.add_option("--combineJets" , dest = "combineJets" , default = False      , action = "store_true", help = "Combine 2 and 3 jet selections?")
    parser.add_option("--combineBTags", dest = "combineBTags", default = False      , action = "store_true", help = "Combine 0, 1, and 2 b-tagged selections?")
    parser.add_option("--combineBkgs" , dest = "combineBkgs" , default = False      , action = "store_true", help = "Combine all backgrounds?")
    parser.add_option("--SMWH"        , dest = "SMWH"        , default = False      , action = "store_true", help = "Use root files with SM WH background?")
    parser.add_option("--GenH"        , dest = "GenH"        , default = False      , action = "store_true", help = "Use only Fat Jets with Gen H's inside?")
    parser.add_option("--variable"    , dest = "variable"    , default = "mT"       , action = "store"     , help = "Checking for mT or mCT dependence?")
    parser.add_option("--plotVariable", dest = "plotVariable", default = "FatJet_pT", action = "store"     , help = "What x-axis variable to plot against?")
    parser.add_option("--threshold"   , dest = "threshold"   , default = "150"      , action = "store"     , help = "What is the threshold for this signal/control region variable?")
    return parser

# If oldList = ["a","b"] and selection = ["1","3","4"], newList = ["a*1","b*1","a*3","b*3","a*4","b*4"]
def expandList(oldList, selection, separation = True):
    newList = []
    for sel in selection:
        for oldElem in oldList:
            if separation:
                newList.append(oldElem + "*" + sel)
            else:
                newList.append(oldElem + sel)
    return newList

def getFiles(options, paths, printInfo = False):
    from os import listdir
    from os.path import isfile, join
    allFiles = []
    for path in paths:
        for f in sorted(listdir(path)):
            if isfile(join(path, f)):
                allFiles.append(join(path, f))
    if printInfo:
        printNewLines(nTimes = 5)
        printDashes(nDashes = 50)
        print "The full set of files are:\n"
        for fCount, f in enumerate(allFiles): print "{:>5} {}".format(fCount+1, f)
        printDashes(nDashes = 50)        
        printNewLines(nTimes = 5)
    return allFiles

# Figures out how to group files
def generateGrouping(options, printInfo = False):
    grouping = [""]
    # Takes care of different years
    if not options.combineYears:
        grouping = expandList(grouping, YEARS)
    else:
        grouping = expandList(grouping, ["yComb"])
    # Takes care of different numbers of jets
    if not options.combineJets:
        grouping = expandList(grouping, JETS)
    else: 
        grouping = expandList(grouping, ["ngoodjetsge"])
    # Fix. Takes care of mt or mct. Could be more robust
    if "mt" == options.variable.lower():
        grouping = expandList(grouping, ["mt_met_lep"]) # Fix. Use either mt or mt_met_lep not either or
    else:
        grouping = expandList(grouping, ["mct"])
    # Fix.
    if "150" == options.threshold.lower():
        grouping = expandList(grouping, ["g150", "l150"], separation = False)
    else:
        grouping = expandList(grouping, ["g200", "l200"], separation = False)
    # Takes care of using Gen-H fat jets or any fat jet
    if not options.GenH:
        grouping = expandList(grouping, BTAGS)
    else:
        grouping = expandList(grouping, ["GenH"])
    # Appends * to every group
    for groupCount in range(len(grouping)):
        grouping[groupCount] += '*'
    # Print grouping if user desires to
    if printInfo:
        printNewLines(nTimes = 5)
        printDashes(nDashes = 50)
        print "The groups are:\n"
        for groupCount, group in enumerate(grouping): print "{:>5} {}".format(groupCount+1, group)
        printDashes(nDashes = 50)
        printNewLines(nTimes = 5)
    return grouping

# Actually group the files now
def groupFiles(allFiles, grouping, printInfo = False):
    import fnmatch
    fileGroups = []
    for selection in grouping:
        fileGroup = []
        for f in allFiles:
            if fnmatch.fnmatch(f, selection):
                fileGroup.append(f)
        fileGroups.append(fileGroup)
    if printInfo:
        printNewLines(nTimes = 5)
        printDashes(nDashes = 50)
        print "The (relevant) files are now organized as:\n"
        for fileGroupCount, fileGroup in enumerate(fileGroups):
            print "\n"
            for fCount, f in enumerate(fileGroup):
                print "{:>5} {}".format(fCount, f)
        print "\nUsing {} total files".format(len(fileGroups)*len(fileGroups[0]))
        printDashes(nDashes = 50)
        printNewLines(nTimes = 5)
    return fileGroups
 
# Generate appropriate titles for each group of files
def generateTitles(grouping, printInfo = False):
    titles = ["" for row in range(len(grouping))]
    for row in range(len(titles)):
        for year in YEARS:
            if year in grouping[row]:
                titles[row] += (year + " ")
                break
        for jets in JETS:
            if jets in grouping[row]:
                titles[row] += (jets[-1] + " jets ")
        if "" == GEN_H: # Gen-H Fat Jets are not separated by b-tags
            for b in BTAGS:
                if b in grouping[row]:
                    if '1' in b:
                        titles[row] += ("1 b-tag ")
                        break
                    titles[row] += (b[-1] + " b-tags ")
                    break
        for region in REGIONS: # This could be fixed to be more robust
            if region in grouping[row]:
                if "mt_met_lepg150" == region:
                    titles[row] += "mT > 150 "
                    break
                elif "mt_met_lepl150" == region:
                    titles[row] += "150 > mT "
                    break
                elif "mctg200" == region:
                    titles[row] += "mCT > 200 "
                    break
                elif "mctl200" == region:
                    titles[row] += "200 > mCT "
                    break
        titles[row] = titles[row][:-1] # Remove trailing space
    if printInfo:
        printNewLines(nTimes = 5)
        printDashes(nDashes = 50)
        print "The titles are:\n"
        for titleCount, title in enumerate(titles):
            print "{:>5} {}".format(titleCount, title)
        printDashes(nDashes = 50)
        printNewLines(nTimes = 5)
    return titles
                    
# Generate appropriate output file names for each group of files
def generateOutNames(grouping, printInfo = False):
    outNames = ["" for row in range(len(grouping))]
    for row in range(len(outNames)):
        for year in YEARS:
            if year in grouping[row]:
                outNames[row] += (year + "_")
                break
        for jets in JETS:
            if jets in grouping[row]:
                outNames[row] += (jets[-1] + "jets_")
                break
        if "" == GEN_H:
            for b in BTAGS:
                if b in grouping[row]:
                    if '1' in b:
                        outNames[row] += ("1btag_")
                        break
                    outNames[row] += (b[-1] + "btags_")
        for region in REGIONS:
            if region in grouping[row]:
                outNames[row] += region + "_"
        outNames[row] = outNames[row][:-1] # Get rid of trailing '_'
    if printInfo:
        printNewLines(nTimes = 5)
        printDashes(nDashes = 50)
        print "The output file names are:\n"
        for outNameCount, outName in enumerate(outNames):
            print "{:>5} {}".format(outNameCount, outName)
        printDashes(nDashes = 50)
        printNewLines(nTimes = 5)
    return outNames
            
def copyHist(hist):
    yourCopy = ROOT.TH1D()
    for binCount in range(hist.GetNbinsX()):
        yourCopy.SetBinContent(binCount+1, hist.GetBinContent(binCount+1))
        yourCopy.SetBinError(binCount+1, hist.GetBinError(binCount+1))
    return yourCopy

# Extracts the idx-th histogram from fileName
def getHistFromFile(fileName, idx):
    f = ROOT.TFile(fileName)
    assert not f.IsZombie()
    f.cd()
    canvasName = f.GetListOfKeys().At(0).GetName()
    tempCanvas = f.Get(canvasName)
    canvas = tempCanvas.Clone()
    f.Close()
    # This mytoppad hack should be fixed
    topPad = canvas.FindObject("mytoppad")
    topPadList = topPad.GetListOfPrimitives()
    #topPadList.ls()
    it = topPadList.begin()
    hist = it.Next()
    for i in range(idx-1):
        hist = it.Next()
    return copyHist(hist)

# Fix. Maybe this function should come before all the generateMistag stuff in generateMistags (notice the 's'). Maybe this could somehow also utilize copyHist, but that might be too confusing
def combineHistBins(fileHist, idx, totalNBins, binning):
    yourHist = ROOT.TH1D("", "", *binning)
    for binCount in range(totalNBins):
        if (binCount+1) == totalNBins:
            err = ROOT.Double()
            yourHist.SetBinContent(totalNBins, fileHist.IntegralAndError(totalNBins, fileHist.GetNbinsX(), err))
            yourHist.SetBinError(totalNBins, err)
            break
        yourHist.SetBinContent(binCount+1, fileHist.GetBinContent(binCount+1))
        yourHist.SetBinError(binCount+1, fileHist.GetBinError(binCount+1))
    return yourHist                

# Fix. Clones TGraphAsymmErrors. However, there might be a built in function already...
def copyGraph(graph):
    yourCopy = ROOT.TGraphAsymmErrors(graph.GetN())
    x = ROOT.Double()
    y = ROOT.Double()
    for bin in range(graph.GetN()):
        graph.GetPoint(bin, x, y)
        yourCopy.SetPoint(bin, x, y)
        yourCopy.SetPointError(bin, graph.GetErrorXlow(bin), graph.GetErrorXhigh(bin), graph.GetErrorYlow(bin), graph.GetErrorYhigh(bin))
    return yourCopy

# Extract the y value, up error, and down error from TGraphAsymmError at bin-th bin
def extractAfFromAsymmBin(asymmGraph, bin):
    x = ROOT.Double()    
    y = ROOT.Double()
    asymmGraph.GetPoint(bin, x, y)
    down = asymmGraph.GetErrorYlow(bin)
    up = asymmGraph.GetErrorYhigh(bin)
    return af(y, up, down)    

def generateMistag(passedFile, totalFile, idx, totalNBins, binning, title, color):
    passedFileHist = getHistFromFile(passedFile, idx)
    totalFileHist = getHistFromFile(totalFile, idx)
    passedHist = combineHistBins(passedFileHist, idx, totalNBins, binning)
    totalHist = combineHistBins(totalFileHist, idx, totalNBins, binning)
    passedInclusiveHist = combineHistBins(passedFileHist, idx, 1, binning)
    totalInclusiveHist = combineHistBins(totalFileHist, idx, 1, binning)
    if ROOT.TEfficiency.CheckConsistency(passedHist, totalHist) and ROOT.TEfficiency.CheckConsistency(passedInclusiveHist, totalInclusiveHist):
        teff = ROOT.TEfficiency(passedHist, totalHist)
        teff.Draw() # Fix. I did not have to call this in the old code, but now I do...?
        teff.Paint("") # Fix. Is this necessary?
        graph = copyGraph(teff.GetPaintedGraph())
        inclusiveTeff = ROOT.TEfficiency(passedInclusiveHist, totalInclusiveHist)
        inclusiveTeff.Paint("") # Fix. Is this necessary?
        return graph, extractAfFromAsymmBin(inclusiveTeff.GetPaintedGraph(), 0)
    else:
      print "ERROR: inconsistent!\n{}\n{}".format(passed, total)
      sys.exit()

def generateMistags(fileGroup, title, idexs, totalNBins, binning, labels, skipIdexs = []):
    if 0 != len(skipIdexs):
        print "You are skipping indices. Have you shifted (if necessary) the other indices to compensate?"
    # fileGroup always has two files
    passedFile = sorted(fileGroup)[1]
    totalFile = sorted(fileGroup)[0]
    graphs = []
    inclusives = []
    for idxCount, idx in enumerate(idexs):
        if idx in skipIdexs:
            continue # Skip indices that user wants to skip
        if len(idexs) == (idxCount+1):
            if isSignalRegion(fileGroup[0]): # any index (that exists) will work
                continue # Signal region does not have data
        graph, inclusive = generateMistag(passedFile, totalFile, idx, totalNBins, binning, title, COLORS[idxCount])
        graphs.append(graph)
        inclusives.append(inclusive)
    return graphs, inclusives

# Generate legend for list of plats with (or without) asymmetric inclusive values 
def generateLegend(xleft, ydown, xright, yup, plots, inclusives, labels):
    leg = ROOT.TLegend(xleft, ydown, xright, yup)
    asymmetryExists = False
    for inclusive in inclusives:
        if inclusive.up != inclusive.down:
            asymmetryExists = True
            break
    for plotCount, plot in enumerate(plots):
        leg.AddEntry(plot, labels[plotCount], 'l')
        if asymmetryExists:
            leg.AddEntry(None, "inclusive: " + str(inclusives[plotCount].central)[:5] + " + " + str(inclusives[plotCount].up)[:5] + " - " + str(inclusives.down)[:5], '')
        else: 
            leg.AddEntry(None, "inclusive: " + str(inclusives[plotCount].central)[:5] + " #pm " + str(inclusives[plotCount].up)[:5], '')
    return leg
            
def convertAsymmToHist(graph, binning):
    x = ROOT.Double()
    y = ROOT.Double()
    hist = ROOT.TH1D("", "", *binning)
    for binCount in range(graph.GetN()):
        graph.GetPoint(binCount, x, y)
        hist.SetBinContent(binCount + 1, y)
        if graph.GetErrorYhigh(binCount) != graph.GetErrorYlow(binCount):
            print("Asymmetrical errors encountered while converting asymmetrical graph to 1D histogram. Exiting")
            sys.exit()
        hist.SetBinError(binCount + 1, graph.GetErrorYhigh(binCount))
    return hist

# Fix. Write this
#def convertHistToAsymm():

def calcAsymmSF(num, den):
    if 0 == den.central:
        return af(0,0,0)
    else:
        return num/den

def generateSFs(graphs, title, inclusives):
    dataGraph = graphs[-1]
    dataInclusive = inclusives[-1]
    SFGraphs = []
    SFInclusives = []
    for graphCount, graph in enumerate(graphs):
        if len(graphs) == (graphCount+1):
            continue # obviously we don't calculate data/data
        SFGraph =  ROOT.TGraphAsymmErrors(graph.GetN())
        for binCount in range(graph.GetN()):
            SF = calcAsymmSF(extractAfFromAsymmBin(graph, binCount), extractAfFromAsymmBin(dataGraph, binCount))
            x = ROOT.Double()
            y = ROOT.Double()
            graph.GetPoint(binCount, x, y)
            SFGraph.SetPoint(binCount, x, SF.central)
            SFGraph.SetPointError(binCount, 0, 0, SF.down, SF.up)
        SFGraphs.append(SFGraph)
        SFInclusives.append(calcAsymmSF(inclusives[graphCount], dataInclusive))
    return SFGraphs, SFInclusives


def setHistProperties(hist, name = None, title = None, xTitle = None, yTitle = None, lineWidth = None, lineColor = None):
    if not (None == name):
        hist.SetName(name)
    if not (None == title):
        hist.SetTitle(title)
    if not (None == xTitle):
        hist.SetXTitle(xTitle)
    if not (None == yTitle):
        hist.SetYTitle(yTitle)
    if not (None == lineWidth):
        hist.SetLineWidth(lineWidth)
    if not (None == lineColor):
        hist.SetLineColor(lineColor)
        return hist

def setAsymmProperties(asymmGraph, name = None, title = None, xTitle = None, yTitle = None, lineWidth = None, lineColor = None, yOffset = None, yMin = None, yMax = None):
    if not (None == name):
        asymmGraph.SetName(name)
    if not (None == title):
        asymmGraph.SetTitle(title)
    if not (None == xTitle):
        asymmGraph.GetXAxis().SetTitle(xTitle)
    if not (None == yTitle):
        asymmGraph.GetYAxis().SetTitle(yTitle)
    if not (None == lineWidth):
        asymmGraph.SetLineWidth(lineWidth)
    if not (None == lineColor):
        asymmGraph.SetLineColor(lineColor)
    if not (None == yOffset):
        asymmGraph.GetYAxis().SetTitleOffset(yOffset)
    if not (None == yMin):
        asymmGraph.SetMinimum(yMin)
    if not (None == yMax):
        asymmGraph.SetMaximum(yMax)
    return asymmGraph

def checkForSubstring(fileName, someSubstring):
    if (someSubstring in fileName):
        return True
    else:
        return False

def isSignalRegion(fileName):
    return checkForSubstring(fileName, "mt_met_lepg150") # fix. This is of course not the only thing that implies we are in the signal region. Ex: mctg200 also counts

def is2016(fileName):
    return checkForSubstring(fileName, "2016")

def is2017(fileName):
    return checkForSubstring(fileName, "2017")

def is2018(fileName):
    return checkForSubstring(fileName, "2018")

def yEqualsOne(xmin, xmax):
    binning = [xmin, xmax]
    binningForTH1D = (1, array.array('d', binning))
    one = ROOT.TH1D("","",*binningForTH1D)
    one.SetBinContent(1,1)
    one.SetLineColor(ROOT.kBlack)
    return one


# To do
# 1. Whatever has a "fix"
# 2. Make a generic print info function?
# 3. SM_WH and GEN_H can not be changed from another file
# 4. Figure out how to pass by reference