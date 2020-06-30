#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imports
import sys
import ROOT
import array
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# variable declarations and initializations
# Currently:
# 1. Only 1 type of background
# 2. Only 1 year
# 3. Only 1 cut (ex: 2 jets, high mt)

topIndex   = 0
bosonIndex = 1
dataIndex  = 2

ttbar     = 1
singletop = 2
WJets     = 3
ttV       = 4
diboson   = 5
data      = 6

nPlots = 3 # data, top, Wjets + diboson
nHists = 6 # data, 5 backgrounds
actualBinCount = 4 # 125-200, 200-300, 300-400, 400-2000
higgsYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nPlots)]
totalYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nPlots)]
mistag               = [[0 for y in range(actualBinCount)] for x in range(nPlots)]

higgsYieldInclusive = [0 for x in range(nPlots)]
totalYieldInclusive = [0 for x in range(nPlots)]
mistagInclusive     = [0 for x in range(nPlots)]

# Png file name and title.
pngName = sys.argv[1]
if "b0" in sys.argv[2]:
    pngName += "_b0"
elif "b1" in sys.argv[2]:
    pngName += "_b1"
elif "b2" in sys.argv[2]:
    pngName += "_b2"
splits = sys.argv[1].split('_')
title = splits[0]
if "2" in splits[2]:
    title+=(" 2 jets")
else:
    title+=(" 3 jets")
if "g" in splits[1]:
    title+=(" mT > 150")
else:
    title+=(" 150 > mT > 50")
title = title[12:] # removes "divideplots/"
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

def getYields(nextCount, argv):
    bkgIndex = nextCount - 1
    if ((ttbar == nextCount) or (singletop == nextCount) or (ttV == nextCount)): 
        bkgIndex = 0 # top processes
    elif ((WJets == nextCount) or (diboson == nextCount)):
        bkgIndex = 1 # Wjets + diboson
    elif ((data == nextCount)):
        bkgIndex = 2 # data
#    print "bkgIndex: {}".format(bkgIndex)
#%%%%%%%%%%
    # loop over files
    for i, fileName in enumerate(argv):
        # the first argument is the program, ignore
        if (i == 0):
            continue # script name
        if (i == 1):
            continue # hist title
        if (("mt_met_lepg150" in argv[2]) and (data == nextCount)): 
            continue # signal cut does not have data
        # Get iterator
        #    it = getIterator(fileName, "mytoppad")
        #    topPadList = getIterator(fileName, "mytoppad")
#%%%%%%%%%%
        f = ROOT.TFile(fileName)                       # open file
        assert not f.IsZombie()
        f.cd() # What does this do?
        canvasName = f.GetListOfKeys().At(0).GetName() # get canvas name 
        tempCanvas = f.Get(canvasName)                 # get canvas using canvas name
    #    if not tempCanvas:  return tempCanvas            
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
        if (data == nextCount): # for data, iterate one more time
            hist = it.Next()
    #%%%%%%%%%%
#        print("{} {}".format(i, fileName))
        if "Higgs" in fileName:
            higgsYieldArrForPlot[bkgIndex][0] += hist.Integral(6,8)
            higgsYieldArrForPlot[bkgIndex][1] += hist.Integral(9,12)
            higgsYieldArrForPlot[bkgIndex][2] += hist.Integral(13,16)
            higgsYieldArrForPlot[bkgIndex][3] += hist.Integral(17,80)
            higgsYieldInclusive[bkgIndex] += hist.Integral()
#            print("Higgs")
        else:
#            print("non-Higgs")
            totalYieldArrForPlot[bkgIndex][0] += hist.Integral(6,8)
            totalYieldArrForPlot[bkgIndex][1] += hist.Integral(9,12)
            totalYieldArrForPlot[bkgIndex][2] += hist.Integral(13,16)
            totalYieldArrForPlot[bkgIndex][3] += hist.Integral(17,80)
            totalYieldInclusive[bkgIndex] += hist.Integral()
#            print(totalYieldArrForPlot)
#        print(hist.GetBinContent(81))
#        print(" ")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
topHist   = ROOT.TH1D("topHist"   , title + ";MET [GeV];mistag efficiencies", *binningArgs)
bosonHist = ROOT.TH1D("bosontHist", title + ";MET [GeV];mistag efficiencies", *binningArgs)
dataHist  = ROOT.TH1D("dataHist"  , title + ";MET [GeV];mistag efficiencies", *binningArgs)

histArr.append(topHist)
histArr.append(bosonHist)
histArr.append(dataHist)

histArr[  topIndex].SetLineColor(ROOT.kRed+1)
histArr[bosonIndex].SetLineColor(ROOT.kBlue+1)
histArr[ dataIndex].SetLineColor(ROOT.kGreen+1)
histArr[ dataIndex].SetMarkerStyle(1)
histArr[ dataIndex].SetMarkerSize(20)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Plot
for iHist in range(len(histArr)):
    for i in range(actualBinCount):
        histArr[iHist].SetBinContent(i+1, mistag[iHist][i])
    histArr[iHist].SetAxisRange(-0.2,1.2,"Y")
#    if iHist == dataIndex: continue
    histArr[iHist].SetLineWidth(2)

# Draw canvas
mistagCanvas = ROOT.TCanvas("","",500,500)
mistagCanvas.Draw()

# Draw hists
for iHist in range(len(histArr)):
    if (("nodata" in sys.argv[2]) and (2 == iHist)):
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
topInclusive   = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binningArgs)
bosonInclusive = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binningArgs)
dataInclusive  = ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binningArgs)
topInclusive.SetLineColor(ROOT.kWhite)
bosonInclusive.SetLineColor(ROOT.kWhite)
dataInclusive.SetLineColor(ROOT.kWhite)
leg.AddEntry(histArr[  topIndex], 't#bar{t}, single top, ttV', 'l')
leg.AddEntry(  topInclusive, "inclusive: " + str(mistagInclusive[  topIndex]), 'l')
leg.AddEntry(histArr[bosonIndex], 'W + Jets, diboson'        , 'l')
leg.AddEntry(bosonInclusive, "inclusive: " + str(mistagInclusive[bosonIndex]), 'l')
if "nodata" not in sys.argv[2]:
    leg.AddEntry(histArr[dataIndex], 'data', 'l')
    leg.AddEntry(dataInclusive, "inclusive: " + str(mistagInclusive[dataIndex]), 'l')
leg.Draw()

mistagCanvas.SaveAs(pngName+".png")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Data/MC Scale Factors
if "nodata" not in sys.argv[2]: # Of course, we can only calculate data/MC if we have data
    topSFHist   = ROOT.TH1D("", title + ";MET [GeV];Data/MC", *binningArgs)
    bosonSFHist = ROOT.TH1D("", title + ";MET [GeV];Data/MC", *binningArgs)
    topSFHist.SetLineColor(ROOT.kRed+1)
    bosonSFHist.SetLineColor(ROOT.kBlue+1)

    for i in range(actualBinCount):
        if 0 == topHist.GetBinContent(i+1): # misleading
            topSFHist.SetBinContent(i+1,0)
        else:
            topSFHist.SetBinContent(i+1, dataHist.GetBinContent(i+1)/topHist.GetBinContent(i+1))

        if 0 == bosonHist.GetBinContent(i+1): # misleading
            bosonSFHist.SetBinContent(i+1,0)
        else:
            bosonSFHist.SetBinContent(i+1, dataHist.GetBinContent(i+1)/bosonHist.GetBinContent(i+1))

    # Draw canvas
    SFCanvas = ROOT.TCanvas("","",500,500)
    SFCanvas.Draw()

    # Custom
    topSFHist.SetAxisRange(-0.1,3,"Y")
    bosonSFHist.SetAxisRange(-0.1,3,"Y")
    topSFHist.SetLineWidth(2)
    bosonSFHist.SetLineWidth(2)

    # Draw hists
    topSFHist.Draw("hist same")
    bosonSFHist.Draw("hist same")
    one.Draw("hist same")

    # Draw legends
    legSF = ROOT.TLegend(0.55,0.75,0.9,0.9)
    topSFInclusive   = ROOT.TH1D("", title + ";MET [GeV];Data/MC", *binningArgs)
    bosonSFInclusive = ROOT.TH1D("", title + ";MET [GeV];Data/MC", *binningArgs)
    topSFInclusive.SetLineColor(ROOT.kWhite)
    bosonSFInclusive.SetLineColor(ROOT.kWhite)
    
    legSF.AddEntry(histArr[  topIndex], 't#bar{t}, single top, ttV', 'l')
    if 0 == mistagInclusive[topIndex]:
        legSF.AddEntry(topInclusive, "inclusive: " + str(0), 'l')
    else:
        legSF.AddEntry(  topInclusive, "inclusive: " + str(mistagInclusive[dataIndex]/mistagInclusive[  topIndex]), 'l')
    legSF.AddEntry(histArr[bosonIndex], 'W + Jets, diboson'        , 'l')
    if 0 == mistagInclusive[bosonIndex]:
        legSF.AddEntry(bosonInclusive, "inclusive: " + str(0), 'l')
    else:
        legSF.AddEntry(bosonInclusive, "inclusive: " + str(mistagInclusive[dataIndex]/mistagInclusive[bosonIndex]), 'l')
    legSF.Draw()
    
    SFCanvas.SaveAs(pngName+"SF.png")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Exit
sys.exit()
    
