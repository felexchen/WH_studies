import sys
import ROOT
import array
#import glob
#from RootTools.core.standard import *
#from Tools.core.standard import *

#def getObjFromFile(fname, hname):
#    f = ROOT.TFile(fname)
#    assert not f.IsZombie()
#    f.cd()
#    htmp = f.Get(hname)
#    if not htmp:  return htmp
#    ROOT.gDirectory.cd('PyROOT:/')
#    res = htmp.Clone()
#    f.Close()
#    return res

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

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Currently:
# 1. Only 1 type of background
# 2. Only 1 year
# 3. Only 1 cut (ex: 2 jets, high mt)

binCount = 20
#higgsYield = [0] * nBackgrounds #[0] * binCount
#totalYield = [0] * nBackgrounds #[0] * binCount
nBackgrounds = 5
higgsYieldArr = [[0 for y in range(binCount)] for x in range(nBackgrounds)]
totalYieldArr = [[0 for y in range(binCount)] for x in range(nBackgrounds)]
actualBinCount = 4 # 125-200, 200-300, 300-400, 400-800
higgsYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nBackgrounds)]
totalYieldArrForPlot = [[0 for y in range(actualBinCount)] for x in range(nBackgrounds)]
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pngName = sys.argv[1]

def getYields(nextCount, argv):
    bkgIndex = nextCount - 1
    # loop over files
    for i, fileName in enumerate(argv):
        # the first argument is the program, ignore
        if (i == 0):
            continue # script name
        if (i == 1):
            continue # hist title
            
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
        it = topPadList.begin()
        hist = it.Next()
        for nextBkg in range(nextCount-1):
            hist = it.Next()
    #%%%%%%%%%%
        for bin in range(binCount):
            totalYieldArr[bkgIndex][bin] += hist.GetBinContent(bin+1)
            if "Higgs" in fileName:
                higgsYieldArr[bkgIndex][bin] += hist.GetBinContent(bin+1)
        print(hist.GetBinContent(22))
        print(" ")

for i in range(nBackgrounds):
    getYields(i+1, sys.argv)

#print("\n\n\nPrinting yield arrays now\n\n\n")
#for bkg in range(2):
#    for i in range(binCount):
#        print(higgsYieldArr[bkg][i])
#    print(" ")
#    for i in range(binCount):
#        print(totalYieldArr[bkg][i])
#    print(" ")
#    for i in range(binCount):
#        if(0.0 == totalYieldArr[bkg][i]):
#            print("0")
#            continue
#        print(higgsYieldArr[bkg][i]/totalYieldArr[bkg][i])
#    print(" ")

for i in range(nBackgrounds):
    higgsYieldArrForPlot[i][0] = higgsYieldArr[i][5]  + higgsYieldArr[i][6]  + higgsYieldArr[i][7]
    higgsYieldArrForPlot[i][1] = higgsYieldArr[i][8]  + higgsYieldArr[i][9]  + higgsYieldArr[i][10] + higgsYieldArr[i][11]
    higgsYieldArrForPlot[i][2] = higgsYieldArr[i][12] + higgsYieldArr[i][13] + higgsYieldArr[i][14] + higgsYieldArr[i][15]
    higgsYieldArrForPlot[i][3] = higgsYieldArr[i][16] + higgsYieldArr[i][17] + higgsYieldArr[i][18] + higgsYieldArr[i][19]

    totalYieldArrForPlot[i][0] = totalYieldArr[i][5]  + totalYieldArr[i][6]  + totalYieldArr[i][7]
    totalYieldArrForPlot[i][1] = totalYieldArr[i][8]  + totalYieldArr[i][9]  + totalYieldArr[i][10] + totalYieldArr[i][11]
    totalYieldArrForPlot[i][2] = totalYieldArr[i][12] + totalYieldArr[i][13] + totalYieldArr[i][14] + totalYieldArr[i][15]
    totalYieldArrForPlot[i][3] = totalYieldArr[i][16] + totalYieldArr[i][17] + totalYieldArr[i][18] + totalYieldArr[i][19]

binning = array.array('d', [125,200,300,400,500])
binningArgs = (len(binning)-1, binning)

ROOT.gStyle.SetOptStat(0)

histArr = []
ttbarHist   = ROOT.TH1D("ttbarHist"  , "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
singletHist = ROOT.TH1D("singletHist", "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
WJetsHist   = ROOT.TH1D("WJetsHist"  , "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
ttbarVHist  = ROOT.TH1D("ttbarVHist" , "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
dibosonHist = ROOT.TH1D("dibosonHist", "mistag efficiencies vs MET;MET [GeV];mistag efficiencies", *binningArgs)
histArr.append(ttbarHist)
histArr.append(singletHist)
histArr.append(WJetsHist)
histArr.append(ttbarVHist)
histArr.append(dibosonHist)
for iHist in range(len(histArr)):
    for i in range(actualBinCount):
        if (0.0 == totalYieldArrForPlot[iHist][i]):
            histArr[iHist].SetBinContent(i+1, 0)
            continue
        histArr[iHist].SetBinContent(i+1, higgsYieldArrForPlot[iHist][i]/totalYieldArrForPlot[iHist][i])
        print(higgsYieldArrForPlot[iHist][i]/totalYieldArrForPlot[iHist][i])
    histArr[iHist].SetLineWidth(2)
    histArr[iHist].SetAxisRange(0,1,"Y")

for i in range(nBackgrounds):
    print(higgsYieldArrForPlot[i])
print(" ")
for i in range(nBackgrounds):
    print(totalYieldArrForPlot[i])
print(" ")
div = higgsYieldArrForPlot
for i in range(nBackgrounds):
    for j in range(actualBinCount):
        div[i][j] = (higgsYieldArrForPlot[i][j]/totalYieldArrForPlot[i][j])
for i in range(nBackgrounds):
    print(div[i])



histArr[0].SetLineColor(ROOT.kRed+1)
histArr[1].SetLineColor(ROOT.kBlue+1)
histArr[2].SetLineColor(ROOT.kGreen+1)
histArr[3].SetLineColor(ROOT.kYellow+1)
histArr[4].SetLineColor(ROOT.kOrange+1)
# for i in range(actualBinCount):
#     if (0.0 == totalYieldArrForPlot[0][i]):
#         ttbarHist.SetBinContent(i, 0)
#         continue
#     ttbarHist.SetBinContent(i, higgsYieldArrForPlot[0][i]/totalYieldArrForPlot[0][i])
#     print(higgsYieldArrForPlot[0][i]/totalYieldArrForPlot[0][i])
# 
# for i in range(actualBinCount):
#     if (0.0 == totalYieldArrForPlot[1][i]):
#         singletopHist.SetBinContent(i, 0)
#         continue
#     singletopHist.SetBinContent(i, higgsYieldArrForPlot[1][i]/totalYieldArrForPlot[1][i])
#     print(higgsYieldArrForPlot[0][i]/totalYieldArrForPlot[1][i])

mistagCanvas = ROOT.TCanvas("","",500,500)
mistagCanvas.Draw()
for iHist in range(len(histArr)):
    histArr[iHist].Draw("hist same")
leg = ROOT.TLegend(0.75,0.75,0.9,0.9)
leg.AddEntry(histArr[0], 't#bar{t}'   , 'l')
leg.AddEntry(histArr[1], 'single t'   , 'l')
leg.AddEntry(histArr[2], 'W + Jets'   , 'l')
leg.AddEntry(histArr[3], 't#bar{t} V', 'l')
leg.AddEntry(histArr[4], 'diboson'    , 'l')
leg.Draw()

print(histArr[1].GetBinContent(0))

mistagCanvas.SaveAs(pngName+".png")

sys.exit()
    

    # create file
    #tf = ROOT.TFile(ef)
    #canName = tf.GetListOfKeys().At(0).GetName() 
    #tempcan = tf.Get(canName)
    #can = tempcan.Clone()
    #tf.Close()
    #print(canName)
    #print(" ")
    #pad = can.FindObject("mytoppad")
#    pad.ls()
    #padlist = pad.GetListOfPrimitives()
#    padlist.ls()
#    print(padlist.First())
    #frame = padlist.First()
    #frame.ls()
    #listiter = padlist.begin()
    #for i in range(10):
    
#    hist = listiter.Next()
#    histcan = ROOT.TCanvas("","",500,500)
#    histcan.Draw()
#    hist.Draw()    
#    histcan.SaveAs("divideplots/name.png")
#    totalYield = 0
#    for i in range(20):
#        totalYield += hist.GetBinContent(i)
#    print(totalYield)


#    print(hist.GetBinContent(7))
#    listiter = padlist.begin()
#    print(padlist)
#    print(listiter.GetCollection())
#    print(padlist.First())
#    print(padlist.Last())
#    mylist = listiter.GetCollect



