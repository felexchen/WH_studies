import sys
import ROOT
import array
import fnmatch

TT_IDX = 1
SINGLE_T_IDX = 2
W_JETS_IDX = 3
TT_V_IDEX = 4
DIBOSON_IDX = 5
DATA_IDX = 7 


var = "mt_met_lep"
threshold = "150"
loweredArgs = [x.lower() for x in sys.argv]
if "mct" in loweredArgs:
    var = "mct"
    threshold = "200"
COMB_JETS_COMB_B = ['*y2016*' + var + 'g' + threshold + '*',
                    '*y2016*' + var + 'l' + threshold + '*',
                    '*y2017*' + var + 'g' + threshold + '*',
                    '*y2017*' + var + 'l' + threshold + '*',
                    '*y2018*' + var + 'g' + threshold + '*',
                    '*y2018*' + var + 'l' + threshold + '*']
COMB_JETS = ['*y2016*' + var + 'g' + threshold + '*b0*',
             '*y2016*' + var + 'l' + threshold + '*b0*',
             '*y2017*' + var + 'g' + threshold + '*b0*',
             '*y2017*' + var + 'l' + threshold + '*b0*',
             '*y2018*' + var + 'g' + threshold + '*b0*',
             '*y2018*' + var + 'l' + threshold + '*b0*',

             '*y2016*' + var + 'g' + threshold + '*b1*',
             '*y2016*' + var + 'l' + threshold + '*b1*',
             '*y2017*' + var + 'g' + threshold + '*b1*',
             '*y2017*' + var + 'l' + threshold + '*b1*',
             '*y2018*' + var + 'g' + threshold + '*b1*',
             '*y2018*' + var + 'l' + threshold + '*b1*',

             '*y2016*' + var + 'g' + threshold + '*b2*',
             '*y2016*' + var + 'l' + threshold + '*b2*',
             '*y2017*' + var + 'g' + threshold + '*b2*',
             '*y2017*' + var + 'l' + threshold + '*b2*',
             '*y2018*' + var + 'g' + threshold + '*b2*',
             '*y2018*' + var + 'l' + threshold + '*b2*']
COMB_B = ['*y2016*ngoodjets2*' + var + 'g' + threshold + '*',
          '*y2016*ngoodjets2*' + var + 'l' + threshold + '*',
          '*y2017*ngoodjets2*' + var + 'g' + threshold + '*',
          '*y2017*ngoodjets2*' + var + 'l' + threshold + '*',
          '*y2018*ngoodjets2*' + var + 'g' + threshold + '*',
          '*y2018*ngoodjets2*' + var + 'l' + threshold + '*',

          '*y2016*ngoodjets3*' + var + 'g' + threshold + '*',
          '*y2016*ngoodjets3*' + var + 'l' + threshold + '*',
          '*y2017*ngoodjets3*' + var + 'g' + threshold + '*',
          '*y2017*ngoodjets3*' + var + 'l' + threshold + '*',
          '*y2018*ngoodjets3*' + var + 'g' + threshold + '*',
          '*y2018*ngoodjets3*' + var + 'l' + threshold + '*']
NO_COMB = ['*y2016*ngoodjets2*' + var + 'g' + threshold + '*b0*',
           '*y2016*ngoodjets2*' + var + 'l' + threshold + '*b0*',
           '*y2017*ngoodjets2*' + var + 'g' + threshold + '*b0*',
           '*y2017*ngoodjets2*' + var + 'l' + threshold + '*b0*',
           '*y2018*ngoodjets2*' + var + 'g' + threshold + '*b0*',
           '*y2018*ngoodjets2*' + var + 'l' + threshold + '*b0*',
           
           '*y2016*ngoodjets2*' + var + 'g' + threshold + '*b1*',
           '*y2016*ngoodjets2*' + var + 'l' + threshold + '*b1*',
           '*y2017*ngoodjets2*' + var + 'g' + threshold + '*b1*',
           '*y2017*ngoodjets2*' + var + 'l' + threshold + '*b1*',
           '*y2018*ngoodjets2*' + var + 'g' + threshold + '*b1*',
           '*y2018*ngoodjets2*' + var + 'l' + threshold + '*b1*',
           
           '*y2016*ngoodjets2*' + var + 'g' + threshold + '*b2*',
           '*y2016*ngoodjets2*' + var + 'l' + threshold + '*b2*',
           '*y2017*ngoodjets2*' + var + 'g' + threshold + '*b2*',
           '*y2017*ngoodjets2*' + var + 'l' + threshold + '*b2*',
           '*y2018*ngoodjets2*' + var + 'g' + threshold + '*b2*',
           '*y2018*ngoodjets2*' + var + 'l' + threshold + '*b2*',
           
           '*y2016*ngoodjets3*' + var + 'g' + threshold + '*b0*',
           '*y2016*ngoodjets3*' + var + 'l' + threshold + '*b0*',
           '*y2017*ngoodjets3*' + var + 'g' + threshold + '*b0*',
           '*y2017*ngoodjets3*' + var + 'l' + threshold + '*b0*',
           '*y2018*ngoodjets3*' + var + 'g' + threshold + '*b0*',
           '*y2018*ngoodjets3*' + var + 'l' + threshold + '*b0*',
           
           '*y2016*ngoodjets3*' + var + 'g' + threshold + '*b1*',
           '*y2016*ngoodjets3*' + var + 'l' + threshold + '*b1*',
           '*y2017*ngoodjets3*' + var + 'g' + threshold + '*b1*',
           '*y2017*ngoodjets3*' + var + 'l' + threshold + '*b1*',
           '*y2018*ngoodjets3*' + var + 'g' + threshold + '*b1*',
           '*y2018*ngoodjets3*' + var + 'l' + threshold + '*b1*',
           
           '*y2016*ngoodjets3*' + var + 'g' + threshold + '*b2*',
           '*y2016*ngoodjets3*' + var + 'l' + threshold + '*b2*',
           '*y2017*ngoodjets3*' + var + 'g' + threshold + '*b2*',
           '*y2017*ngoodjets3*' + var + 'l' + threshold + '*b2*',
           '*y2018*ngoodjets3*' + var + 'g' + threshold + '*b2*',
           '*y2018*ngoodjets3*' + var + 'l' + threshold + '*b2*']

def noData(fileName):
    # var + "l" + threshold constitutes a CR and CRs have data
    if ((var + "l" + threshold) in fileName): 
        return True
    else:
        return False

def drawYEqualsOne(binning):
    bin = [min(binning), max(binning)]
    binForHist = (1, array.array('d', bin))
    one = ROOT.TD1D("","","",*binForHist)
    one.SetBinContent(1,1)
    one.SetLineColor(ROOT.kBlack)
    one.Draw("hist same")

def generateHist(title = "", binning, , *argv):
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
    


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if __name__ == "__main__":

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--combineJets" , dest = "combineJets" , default = False, action = "store_true", help = "Combine 2 and 3 jet selections?")
    parser.add_option("--combineBTags", dest = "combineBTags", default = False, action = "store_true", help = "Combine 0, 1, and 2 b-tagged selections?")
    parser.add_option("--combineBkgs" , dest = "combineBkgs" , default = False, action = "store_true", help = "Combine all backgrounds?")
    parser.add_option("--variable"    , dest = "variable"    , default = "mt" , action = "store"     , help = "Checking for mT or mCT dependence?")
    (options, args) = parser.parse_args()

    # Calculate the number of files we're working with (= to number of cuts).
    # The end result is the number of "sets" of files which = number of plots.
    differentJetCuts = 2      # 2 jets or 3 jets
    differentBTagCuts = 3     # 0, 1, or 2 b tags
    differentHiggsTagCuts = 2 # Higgs tag or no Higgs tag
    differentYearCuts = 3     # 2016, 2017, or 2018
    differentVariableCuts = 2 # High mT (150 >) or low mT (150, 50). High mCT (200 >) or low mCT (200 <)
    numberOfFiles = differentJetCuts * differentBTagCuts * differentHiggsTagCuts * differentYearCuts * differentVariableCuts
    if True == options.combineJets:
        numberOfFiles = numberOfFiles/differentJetCuts  # Means do not differentiate between jet cuts.
    if True == options.combineBTags:
        numberOfFiles = numberOfFiles/differentBTagCuts # Means do not differentiate between b tag cuts.
    numberOfFiles = numberOfFiles/differentHiggsTagCuts # Obviously any single mistag plot needs a Higgs and non-Higgs file, so we cannot differentiate between them.

    # Get files and sort into into sets
    from os import listdir
    from os.path import isfile, join
    CRFilePath = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/l150/root/lin"
    SRFilePath = ""
    if "mct" == options.variable.lower():
        SRFilePath = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mCT/g150/root/lin"
    else:
        SRFilePath = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/g150/root/lin"
    allFiles = []
#    print(listdir(CRFilePath))
    for i in sorted(listdir(CRFilePath)):
        f = join(CRFilePath, i)
        if isfile(f):
            allFiles.append(f)
            print(f)
    for i in sorted(listdir(SRFilePath)):
        f = join(SRFilePath, i)
        if isfile(f):
            allFiles.append(f)
            print(f)
    sortedFiles = [[]]

    if ((True == options.combineJets) and (True == options.combineBTags)):
        for i in COMB_JETS_COMB_B:
            dummy = []
            for j in allFiles:
                if fnmatch.fnmatch(j, i):
                    print(j[80:])
                    dummy.append(j)
            sortedFiles.append(dummy)
            print("\n")
    elif True == options.combineJets:
        for i in COMB_JETS:
            for j in allFiles:
                if fnmatch.fnmatch(j, i):
                    print(j)
            print("\n")
    elif True == options.combineBTags:
        for i in COMB_B:
            for j in allFiles:
                if fnmatch.fnmatch(j, i):
                    print(j)
            print("\n")
    else:
        for i in NO_COMB:
            for j in allFiles:
                if fnmatch.fnmatch(j, i):
                    print(j)
            print("\n")

#    sys.exit()        
#    print("hello")
#    histCount = 3 # top related, W + jets and diboson, data
#    if options.combineBkg:
#        histCount = 2
            
    # ROOT and historamming set up
    ROOT.gStyle.SetOptStat(0)
    binning = array.array('d', [125,200,300,400,2000])
    binningArgs = (len(binning)-1, binning)


    for fileSet in sortedFiles:
#        if options.combineBkgs:
#            getYields([[TT_IDX], 
#                       [DATA_IDX]], 
#                      fileSet)
#        else:
#            getYields([[TT_IDX, , 5], 
#                       [3, 4], 
#                       [6]], 
#                      fileSet)
        can = ROOT.TCanvas("","",500,500)
        can.Draw()
        drawYEqualsOne(binning)
        for fileName in fileSet:
            print("asserting " + fileName)
            f = ROOT.TFile(fileName)                       # open file
            assert not f.IsZombie()
            f.cd() # What does this do?
            canvasName = f.GetListOfKeys().At(0).GetName() # get canvas name 
            tempCanvas = f.Get(canvasName)                 # get canvas using canvas name
            canvas = tempCanvas.Clone()                    # clone canvas
            f.Close()                                      # close file
            topPad = canvas.FindObject("mytoppad")         # get top pad
            topPadList = topPad.GetListOfPrimitives()      # get list from top pad
            #topPadList.ls()
            it = topPadList.begin()
            arr = [[0 for y in range(5)] for x in range(6)]
            for i in range(6):
                hist = it.Next()
                if 6 == i:
                    hist = it.Next() # There's a TLegend object between bkgs and data (check topPadList.ls())
                    if noData(fileName):
                        continue # No data in SR
                arr[i][0] = hist.Integral(6,8)   # 125-200
                arr[i][1] = hist.Integral(9,12)  # 200-300
                arr[i][2] = hist.Integral(13,16) # 300-400
                arr[i][3] = hist.Integral(17,80) # 400-2000
                arr[i][4] = hist.Integral() # 0-2000
            for i in range(6):
            
                arr[i][0] -= arr[i+1][0]
                arr[i][1] -= arr[i+1][1]
                arr[i][2] -= arr[i+1][2]
                arr[i][3] -= arr[i+1][3]
                arr[i][4] -= arr[i+1][4]
                print(arr[i])
            print("\n")
            
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
                    
                

    sys.exit()

    for i, f in enumerate(allFiles):
        if fnmatch.fnmatch(f, 'y2016*'):
            print(f)
    print("Imported {} files".format(len(allFiles)))
    



#    # ROOT and historamming set up
#    ROOT.gStyle.SetOptStat(0)
#    binning = array.array('d', [125,200,300,400,2000])
#    binningArgs = (len(binning)-1, binning)
#    # There are 3 columns of plots - top related, W + jets and diboson, and data. If --combineBkgs is True, then there are 2 columns - all backgrounds and data.
#    columns = 3
#    if True == options.combineBkgs:
#        columns = 2
#    numberOfPlots = [[ROOT.TH1D("", title + ";MET [GeV];mistag efficiencies", *binningArgs) for i in range(columns)] for x in range(numberOfFiles)] # Read as number of "sets" of files.



