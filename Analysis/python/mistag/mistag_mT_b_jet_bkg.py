#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# This script:
# 1. Separates by high and low mT
# 2. Separates by number of b-tags
# 3. Combines 2 and 3 jets plots
# 4. Combines all backgrounds
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imports
import sys
import ROOT
import array
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
combinedBkgIndex   = 0
dataIndex  = 1

nPlots = 2 # data, bkg
nHists = 6 # data, 5 backgrounds
actualBinCount = 4 # 125-200, 200-300, 300-400, 400-2000
higgsYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nPlots)]
totalYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nPlots)]
mistag               = [[0 for y in range(actualBinCount)] for x in range(nPlots)]

higgsYieldInclusive = [0 for x in range(nPlots)]
totalYieldInclusive = [0 for x in range(nPlots)]
mistagInclusive     = [0 for x in range(nPlots)]

# Png file name
pngName = sys.argv[1]
if "b0" in sys.argv[2]:
    pngName += "_b0"
elif "b1" in sys.argv[2]:
    pngName += "_b1"
elif "b2" in sys.argv[2]:
    pngName += "_b2"

# Title
splits = sys.argv[1].split('_')
title = splits[0]
if "g" in splits[1]:
    title+=(" mT > 150")
else:
    title+=(" 150 > mT > 50")
title = title[6:] # removes "plots/"
if "b0" in sys.argv[2]:
    title += " 0 b tags"
elif "b1" in sys.argv[2]:
    title += " 1 b tag"
elif "b2" in sys.argv[2]:
    title += " 2 b tags"

print("\n\n\n\n\n\n\n\n\n\n{}\n{}\n\n\n".format(pngName, title))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Function definitions.
# Get a list iterator to retrieve histograms
def getIterator(fileName, padName):
    f = ROOT.TFile(fileName)                       # open file
    assert not f.IsZombie()
    f.cd() # What does this do?
    canvasName = f.GetListOfKeys().At(0).GetName() # get canvas name 
    tempCanvas = f.Get(canvasName)                 # get canvas using canvas name
    if not tempCanvas:  return tempCanvas            
    canvas = tempCanvas.Clone()                    # clone canvas
    f.Close()                                      # close file
    topPad = canvas.FindObject(padName)            # get top pad
    topPadList = topPad.GetListOfPrimitives()      # get list from top pad
    print("got top pad list")
    return topPadList
#    iterator = topPadList.begin()                  # get iterator from top pad list 
#    return iterator                                # return iterator

dataCount = 6

def getYields(nextCount, argv):
    bkgIndex = combinedBkgIndex # 0 is for background
    if ((dataCount == nextCount)): # sixth hist is data
        bkgIndex = dataIndex # 1 is for data
 #%%%%%%%%%%
    # loop over files
    for i, fileName in enumerate(argv):
        # the first argument is the program, ignore
        if (i == 0):
            continue # script name
        if (i == 1):
            continue # hist title
        if (("mt_met_lepg150" in argv[2]) and (dataCount == nextCount)): 
            continue # signal cut does not have data
#%%%%%%%%%%
        f = ROOT.TFile(fileName)                       # open file
        assert not f.IsZombie()
        f.cd() # What does this do?
        canvasName = f.GetListOfKeys().At(0).GetName() # get canvas name 
        tempCanvas = f.Get(canvasName)                 # get canvas using canvas name
        canvas = tempCanvas.Clone()                    # clone canvas
        f.Close()                                      # close file
        topPad = canvas.FindObject("mytoppad")         # get top pad
        topPadList = topPad.GetListOfPrimitives()      # get list from top pad
    #%%%%%%%%%%
#        topPadList.ls()
        it = topPadList.begin()
        hist = it.Next()
        for nextBkg in range(nextCount - 1):
            hist = it.Next()
        if (dataCount == nextCount): # for data, iterate one more time
            hist = it.Next()
    #%%%%%%%%%%
        if "Higgs" in fileName:
            higgsYieldArrForPlot[bkgIndex][0] += hist.Integral(6,8)
            higgsYieldArrForPlot[bkgIndex][1] += hist.Integral(9,12)
            higgsYieldArrForPlot[bkgIndex][2] += hist.Integral(13,16)
            higgsYieldArrForPlot[bkgIndex][3] += hist.Integral(17,80)
            higgsYieldInclusive[bkgIndex] += hist.Integral()
            print("Higgs") # should be 10 or 12 times (2 and 3 jets * 5 or 6 hists)
        else:
            totalYieldArrForPlot[bkgIndex][0] += hist.Integral(6,8)
            totalYieldArrForPlot[bkgIndex][1] += hist.Integral(9,12)
            totalYieldArrForPlot[bkgIndex][2] += hist.Integral(13,16)
            totalYieldArrForPlot[bkgIndex][3] += hist.Integral(17,80)
            totalYieldInclusive[bkgIndex] += hist.Integral()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i in range(len(sys.argv)): print sys.argv[i]
# Yield extraction 
for i in range(nHists): # for backgrounds
    getYields(i+1, sys.argv)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Calculate mistags
for i in range(nPlots):
    if (("mt_met_lepg150" in sys.argv[2]) and (dataIndex == i)):
        continue # signal cut does not have data
    for j in range(actualBinCount):
        if 0 == totalYieldArrForPlot[i][j]: # this is very misleading, unfortunately
            mistag[i][j] = 0
            continue
        mistag[i][j] = (higgsYieldArrForPlot[i][j]/totalYieldArrForPlot[i][j])

# Calculate mistag inclusive
for i in range(nPlots):
    if (("mt_met_lepg150" in sys.argv[2]) and (dataIndex == i)):
        continue # signal cut does not have data
    mistagInclusive[i] = higgsYieldInclusive[i]/totalYieldInclusive[i]

# Print 
for i in range(nPlots):
    print(higgsYieldArrForPlot[i])
print(" ")
for i in range(nPlots):
    print(totalYieldArrForPlot[i])
print(" ")
for i in range(nPlots):
    print(mistag[i])     
print(" ")
for i in range(nPlots):
    print(higgsYieldInclusive[i])
print(" ")
for i in range(nPlots):
    print(totalYieldInclusive[i])
print(" ")
for i in range(nPlots):
    print(mistagInclusive[i])
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ROOT and histogramming set up
ROOT.gStyle.SetOptStat(0)

binning = array.array('d', [125,200,300,400,2000])
binningArgs = (len(binning)-1, binning)

histArr = []
bkgHist  = ROOT.TH1D("backgroundHist", title + ";MET [GeV];mistag efficiencies", *binningArgs)
dataHist = ROOT.TH1D("dataHist"      , title + ";MET [GeV];mistag efficiencies", *binningArgs)

histArr.append(bkgHist)
histArr.append(dataHist)

histArr[combinedBkgIndex].SetLineColor(ROOT.kBlue+1)
histArr[       dataIndex].SetLineColor(ROOT.kRed+1)
histArr[       dataIndex].SetMarkerStyle(1)
histArr[       dataIndex].SetMarkerSize(20)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Plot
for iHist in range(len(histArr)):
    for i in range(actualBinCount):
        histArr[iHist].SetBinContent(i+1, mistag[iHist][i])
    histArr[iHist].SetAxisRange(-0.2,1.2,"Y")
    histArr[iHist].SetLineWidth(2)

# Draw canvas
mistagCanvas = ROOT.TCanvas("","",500,500)
mistagCanvas.Draw()

# Draw hists
for iHist in range(len(histArr)):
    if (("nodata" in sys.argv[2]) and (1 == iHist)):
        continue # is there isn't any data, don't plot it
    histArr[iHist].Draw("hist same")

onebin = [min(binning),max(binning)]
onebinArgs = (1, array.array('d', onebin))
one = ROOT.TH1D("","",*onebinArgs)
one.SetBinContent(1,1)
one.SetLineColor(ROOT.kBlack)
one.Draw("hist same")

# Draw legends
leg = ROOT.TLegend(0.55,0.75,0.9,0.9)
bkgInclusive  = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binningArgs)
dataInclusive = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binningArgs)
bkgInclusive.SetLineColor(ROOT.kWhite)
dataInclusive.SetLineColor(ROOT.kWhite)
leg.AddEntry(histArr[combinedBkgIndex], 't#bar{t}, single top, ttV, W + Jets, diboson', 'l')
leg.AddEntry(bkgInclusive, "inclusive: " + str(mistagInclusive[combinedBkgIndex]), 'l')
if "nodata" not in sys.argv[2]:
    leg.AddEntry(histArr[dataIndex], 'data', 'l')
    leg.AddEntry(dataInclusive, "inclusive: " + str(mistagInclusive[dataIndex]), 'l')
leg.Draw()

mistagCanvas.SaveAs(pngName+".png")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Data/MC Scale Factors
if "nodata" not in sys.argv[2]: # Of course, we can only calculate data/MC if we have data
    #print sys.argv[2]
    bkgSFHist = ROOT.TH1D("", title + ";MET [GeV];Data/MC", *binningArgs)
    bkgSFHist.SetLineColor(ROOT.kBlue+1)

    for i in range(actualBinCount):
        if 0 == bkgHist.GetBinContent(i+1): # misleading
            bkgSFHist.SetBinContent(i+1,0)
        else:
            bkgSFHist.SetBinContent(i+1, dataHist.GetBinContent(i+1)/bkgHist.GetBinContent(i+1))

    # Draw canvas
    SFCanvas = ROOT.TCanvas("","",500,500)
    SFCanvas.Draw()

    # Custom
    bkgSFHist.SetAxisRange(-0.1,3,"Y")
    bkgSFHist.SetLineWidth(2)

    # Draw hists
    bkgSFHist.Draw("hist same")
    one.Draw("hist same")

    # Draw legends
    legSF = ROOT.TLegend(0.55,0.75,0.9,0.9)
    bkgSFInclusive   = ROOT.TH1D("", title + ";MET [GeV];Data/MC", *binningArgs)
    bkgSFInclusive.SetLineColor(ROOT.kWhite)
        
    legSF.AddEntry(histArr[combinedBkgIndex], 't#bar{t}, single top, ttV, W + Jets, diboson', 'l')
    if 0 == mistagInclusive[combinedBkgIndex]:
        legSF.AddEntry(bkgInclusive, "inclusive: " + str(0), 'l')
    else:
        legSF.AddEntry(bkgInclusive, "inclusive: " + str(mistagInclusive[dataIndex]/mistagInclusive[combinedBkgIndex]), 'l')

    legSF.Draw()
    
    SFCanvas.SaveAs(pngName+"SF.png")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Exit
sys.exit()
    
