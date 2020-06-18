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

# nPlots = 6 # 5 backgrounds + data
nPlots = 3 # data, top, Wjets + diboson
actualBinCount = 4 # 125-200, 200-300, 300-400, 400-1000
higgsYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nPlots)]
totalYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nPlots)]

# Png file name and title. Fix!
pngName = sys.argv[1]
print("\n\n\n{}\n\n\n".format(pngName))
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
    if ((1 == nextCount) or (2 == nextCount) or (3 == nextCount)): 
        bkgIndex = 0 # top processes
    elif ((4 == nextCount) or (5 == nextCount)):
        bkgIndex = 1 # Wjets + diboson
    elif ((6 == nextCount)):
        bkgIndex = 2 # data
    # loop over files
    for i, fileName in enumerate(argv):
        # the first argument is the program, ignore
        if (i == 0):
            continue # script name
        if (i == 1):
            continue # hist title
        if (("mt_met_lepg150" in argv[2]) and (6 == nextCount)): 
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
        if (6 <= nextCount): # for data, iterate one more time
            hist = it.Next()
    #%%%%%%%%%%
#        for bin in range(binCount):
#            totalYieldArr[bkgIndex][bin] += hist.GetBinContent(bin+1)
#            if "Higgs" in fileName:
#                higgsYieldArr[bkgIndex][bin] += hist.GetBinContent(bin+1)
#        print(hist)

        if "Higgs" in fileName:
            higgsYieldArrForPlot[bkgIndex][0] += hist.Integral(6,8)
            higgsYieldArrForPlot[bkgIndex][1] += hist.Integral(9,12)
            higgsYieldArrForPlot[bkgIndex][2] += hist.Integral(13,16)
            higgsYieldArrForPlot[bkgIndex][3] += hist.Integral(17,80)
        else:
            totalYieldArrForPlot[bkgIndex][0] += hist.Integral(6,8)
            totalYieldArrForPlot[bkgIndex][1] += hist.Integral(9,12)
            totalYieldArrForPlot[bkgIndex][2] += hist.Integral(13,16)
            totalYieldArrForPlot[bkgIndex][3] += hist.Integral(17,80)
        print(hist.GetBinContent(81))
        print(" ")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Yield extraction 
for i in range(nPlots): # for backgrounds
    getYields(i+1, sys.argv)
#if "mt_met_lepl150" in sys.argv[1]:
#    getYields(i, sys.argv)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ROOT and histogramming set up
ROOT.gStyle.SetOptStat(0)

binning = array.array('d', [125,200,300,400,2000])
binningArgs = (len(binning)-1, binning)

histArr = []
ttbarHist   = ROOT.TH1D("ttbarHist"  , "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
singletHist = ROOT.TH1D("singletHist", "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
WJetsHist   = ROOT.TH1D("WJetsHist"  , "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
ttbarVHist  = ROOT.TH1D("ttbarVHist" , "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
dibosonHist = ROOT.TH1D("dibosonHist", "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
dataHist = ROOT.TH1D("dataHist", "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)

histArr.append(ttbarHist)
histArr.append(singletHist)
histArr.append(WJetsHist)
#histArr.append(ttbarVHist)
#histArr.append(dibosonHist)
#histArr.append(dataHist)

histArr[0].SetLineColor(ROOT.kRed+1)
histArr[1].SetLineColor(ROOT.kBlue+1)
histArr[2].SetLineColor(ROOT.kGreen+1)
# histArr[3].SetLineColor(ROOT.kYellow+1)
# histArr[4].SetLineColor(ROOT.kOrange+1)
# #histArr[5].SetLineColor(ROOT.kViolet+1)
# histArr[5].SetMarkerStyle(1)
# histArr[5].SetMarkerSize(20)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Plot
for iHist in range(len(histArr)):
    for i in range(actualBinCount):
        if (0.0 == totalYieldArrForPlot[iHist][i]):
            histArr[iHist].SetBinContent(i+1, 0)
            continue
        histArr[iHist].SetBinContent(i+1, higgsYieldArrForPlot[iHist][i]/totalYieldArrForPlot[iHist][i])
    histArr[iHist].SetAxisRange(0,1,"Y")
    if iHist == 5: continue
    histArr[iHist].SetLineWidth(2)
for i in range(nPlots):
    print(higgsYieldArrForPlot[i])
print(" ")
for i in range(nPlots):
    print(totalYieldArrForPlot[i])
print(" ")
div = higgsYieldArrForPlot
for i in range(nPlots):
    for j in range(actualBinCount):
        if (0.0 == totalYieldArrForPlot[i][j]):
            div[i][j] = 0
            continue
        div[i][j] = (higgsYieldArrForPlot[i][j]/totalYieldArrForPlot[i][j])
for i in range(nPlots):
    print(div[i])     
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Draw and save.
mistagCanvas = ROOT.TCanvas("","",500,500)
mistagCanvas.Draw()

for iHist in range(len(histArr)):
    if (("nodata" in sys.argv[2]) and (2 == iHist)):
        continue # is there isn't any data, don't plot it
    histArr[iHist].Draw("hist same")

leg = ROOT.TLegend(0.75,0.75,0.9,0.9)
leg.AddEntry(histArr[0], 't#bar{t}'  , 'l')
leg.AddEntry(histArr[1], 'single t'  , 'l')
# leg.AddEntry(histArr[2], 'W + Jets'  , 'l')
# leg.AddEntry(histArr[3], 't#bar{t} V', 'l')
# leg.AddEntry(histArr[4], 'diboson'   , 'l')
if "nodata" not in sys.argv[2]:
    leg.AddEntry(histArr[2], 'data', 'l')
leg.Draw()

mistagCanvas.SaveAs(pngName+".png")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Exit
sys.exit()
    
