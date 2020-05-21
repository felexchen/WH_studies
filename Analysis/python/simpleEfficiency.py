#!/usr/bin/env python
import os, sys
import ROOT
import array
import json
import math
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
import array

ROOT.PyConfig.IgnoreCommandLineOptions = True

from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from RootTools.core.standard import *
from WH_studies.Tools.u_float import u_float as uf

def hasBit(value,bit):
  """Check if i'th bit is set to 1, i.e. binary of 2^(i-1),
  from the right to the left, starting from position i=0."""
  # https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html#GenPart
  # Gen status flags, stored bitwise, are:
  #    0: isPrompt,                          8: fromHardProcess,
  #    1: isDecayedLeptonHadron,             9: isHardProcessTauDecayProduct,
  #    2: isTauDecayProduct,                10: isDirectHardProcessTauDecayProduct,
  #    3: isPromptTauDecayProduct,          11: fromHardProcessBeforeFSR,
  #    4: isDirectTauDecayProduct,          12: isFirstCopy,
  #    5: isDirectPromptTauDecayProduct,    13: isLastCopy,
  #    6: isDirectHadronDecayProduct,       14: isLastCopyBeforeFSR
  #    7: isHardProcess,
  ###return bin(value)[-bit-1]=='1'
  ###return format(value,'b').zfill(bit+1)[-bit-1]=='1'
  return (value & (1 << bit))>0


def fixUncertainties(teff, heff, x_binning, y_binning):
    for x in x_binning:
        for y in y_binning:
            x_bin = heff.GetXaxis().FindBin(x)
            y_bin = heff.GetYaxis().FindBin(y)
            n_bin = teff.FindFixBin(x,y)
            err   = (teff.GetEfficiencyErrorUp(n_bin) + teff.GetEfficiencyErrorLow(n_bin) ) / 2.
            heff.SetBinError(x_bin, y_bin, err)
    return heff

def writeObjToFile(fname, obj, update=False):
    gDir = ROOT.gDirectory.GetName()
    if update:
        f = ROOT.TFile(fname, 'UPDATE')
    else:
        f = ROOT.TFile(fname, 'recreate')
    objw = obj.Clone()
    objw.Write()
    f.Close()
    ROOT.gDirectory.cd(gDir+':/')
    return



## Do the nanoAOD-tools stuff
class TaggerAnalysis(Module):
    def __init__(self, btagWP=0.4941, htagWP=0.8, tagger="deepTagMD_HbbvsQCD"):
        self.writeHistFile = True
        self.btagWP = btagWP
        self.htagWP = htagWP
        self.tagger = tagger

    def beginJob(self,histFile=None,histDirName=None):
        Module.beginJob(self,histFile,histDirName)

        pt_thresholds           = [200,300,400,500,600,2000]
        # pt_thresholds   = []
        # for i in range(19):
        #   pt_thresholds.append((i*100)+200)

        # 1D hists
        self.h_FatJet_pt_all    = ROOT.TH1F("FatJet_pt_all",    "", len(pt_thresholds)-1, array.array('d',pt_thresholds))
        self.h_FatJet_pt_pass   = ROOT.TH1F("FatJet_pt_pass",   "", len(pt_thresholds)-1, array.array('d',pt_thresholds))

        for o in [self.h_FatJet_pt_all, self.h_FatJet_pt_pass]:
            self.addObject(o)

    def deltaPhi(self, phi1, phi2):
        dphi = phi2-phi1
        if  dphi > math.pi:
            dphi -= 2.0*math.pi
        if dphi <= -math.pi:
            dphi += 2.0*math.pi
        return abs(dphi)

    def deltaR2(self, l1, l2):
        return self.deltaPhi(l1.phi, l2.phi)**2 + (l1.eta - l2.eta)**2

    def deltaR(self, l1, l2):
        return math.sqrt(self.deltaR2(l1,l2))

    def hasAncestor(self, p, ancestorPdg, genParts):
        motherIdx = p.genPartIdxMother
        while motherIdx>0:
            if (abs(genParts[motherIdx].pdgId) == ancestorPdg): return True
            motherIdx = genParts[motherIdx].genPartIdxMother
        return False

    def analyze(self, event):
        subjets     = Collection(event, "SubJet")
        fatjets     = Collection(event, "FatJet")
        genparts    = Collection(event, "GenPart")

        # filter out all the Higgs bosons from the generated particles
        # 13 = last copy
        # 25 = higgs
        Higgs = [ p for p in genparts if (abs(p.pdgId)==25 and hasBit(p.statusFlags,13) ) ] # last copy Ws

        # there should only be one.
        if len(Higgs)>1:
            print "Found more than 1 Higgs. Please check!"
            return False

        nFatJets = len(fatjets)

        # only measure if at least one Higgs boson was found in the generated particles
        nHiggsInFatJet = 0

        if len(Higgs)>0:
            # loop over all FatJets
            for fatjet in fatjets:
                # deltaR matching of the fatjet and the higgs boson
                if self.deltaR(fatjet, Higgs[0]) < 0.4:
                    # that speaks for itself
                    nHiggsInFatJet += 1
                    self.h_FatJet_pt_all.Fill(fatjet.pt)
                    if getattr(fatjet, self.tagger) > self.htagWP:
                        self.h_FatJet_pt_pass.Fill(fatjet.pt)
        
        if nHiggsInFatJet>1:
            print "More than one FatJet with Higgs boson deltaR match. Weird -> please check!"

        return True

    def endJob(self):
        pass
        #self.eff    = ROOT.TEfficiency(self.h_pt1_passEvents, self.h_pt1_totalEvents)
        #self.addObject(self.eff)

if __name__ == "__main__":

    ## Define WH samples
    WH_F17_FullSim = Sample.fromFiles("WH_F17_FullSim", ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FullSim_JEC.root"], "Events", xSection=123.) # arbitrary x-sec
    WH_F17_FastSim = Sample.fromFiles("WH_F17_FastSim", ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FastSim_JEC.root"], "Events", xSection=123.) # arbitrary x-sec

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--year",                  dest="year",                  default=2016, type="int",    action="store",      help="Which year?")
    parser.add_option("--tagger",                dest="tagger",                default="deepTagMD_HbbvsQCD",action="store",      help="Which Higgs tagger should be used?")
    parser.add_option("--customWP",              dest="customWP",              default=-1,   type="float",  action="store",      help="Define a custom higgs tagger WP")
    parser.add_option("--fastSim",               dest="fastSim",               default=False,               action="store_true", help="Use FastSim?")
    (options, args) = parser.parse_args()

    ## select proper b-tag WP depending on year.
    if options.year == 2016:
        btagWP = 0.6321
        htagWP = 0.8945 #0.8
        sample = S16
    elif options.year == 2017:
        btagWP = 0.4941
        htagWP = 0.8695
#        sample = WH_F17_FullSim if not options.fastSim else WH_F17_FastSim
        sampleFast = WH_F17_FastSim # hack for us to use both samples while only running this once
        sampleFull = WH_F17_FullSim # hack for us to use both samples while only running this once
    elif options.year == 2018:
        btagWP = 0.4184
        htagWP = 0.8365 #0.8
        sample = A18
    else:
        print "Don't know year %s"%options.year
        btatWP = 1

    if options.customWP > 0:
        htagWP = options.customWP

    # very loose preselection
    preselection = 'nFatJet>0'
#    files = sample.files
    filesFast = sampleFast.files # hack (see sampleFull sampleFast)
    filesFull = sampleFull.files # hack (see sampleFull sampleFast)
    
    # this is where the magic happens
#    p = PostProcessor(".", files, cut=preselection, branchsel=None, modules=[TaggerAnalysis(btagWP, htagWP, options.tagger)], noOut=True, histFileName="histOut.root", histDirName="plots")
    pFast = PostProcessor(".", filesFast, cut=preselection, branchsel=None, modules=[TaggerAnalysis(btagWP, htagWP, options.tagger)], noOut=True, histFileName="histOut.root", histDirName="plots") # hack (see sampleFull sampleFast)
    pFull = PostProcessor(".", filesFull, cut=preselection, branchsel=None, modules=[TaggerAnalysis(btagWP, htagWP, options.tagger)], noOut=True, histFileName="histOut.root", histDirName="plots") # hack (see sampleFull sampleFast)
    print "Starting the processor"
    pFast.run() # hack (see sampleFull sampleFast)
    pFull.run() # hack (see sampleFull sampleFast)

    # get the root histograms from the processor
    hFast_all   = pFast.histFile.Get("FatJet_pt_all")  # hack (see sampleFull sampleFast)
    hFast_pass  = pFast.histFile.Get("FatJet_pt_pass") # hack (see sampleFull sampleFast)
    hFull_all   = pFull.histFile.Get("FatJet_pt_all")  # hack (see sampleFull sampleFast)
    hFull_pass  = pFull.histFile.Get("FatJet_pt_pass") # hack (see sampleFull sampleFast)

    # get the efficiency. we use TEfficiency because the uncertainties are correlated, and this is taken into account in this ROOT routine
    effFast     = ROOT.TEfficiency(hFast_pass, hFast_all) # hack (see sampleFull sampleFast)
    effFull     = ROOT.TEfficiency(hFull_pass, hFull_all) # hack (see sampleFull sampleFast)
    # hist.Integral() experiment
    #    #print(h_pass.Integral(0,10000))
    #    #print(h_all.Integral())
    #    #print(h_pass.Integral(200,300))
    #    #print(h_all.Integral(200,300))
    #    #print(h_pass.Integral(300,400))
    #    #print(h_all.Integral(300,400))
    #    #
    #    for i in range(len(pt_thresholds)): 
    #      passInt = h_pass.Integral(i+1,i+2) # root bin numbers start at 1
    #      allInt  = h_all.Integral(i+1,i+2)  # root bin numbers start at 1
    #      eff.append(passInt/allInt)
    #      print(passInt)
    #      print(allInt)
    #      print(passInt/allInt)
    #      print("")
    
    # pt thresholds
    pt_thresholds   = [200,300,400,500,600,2000]
    # pt_thresholds   = []
    # for i in range(19):
    #   pt_thresholds.append((i*100)+200)
    
    # get the efficiencies into a list, and symmetrize the uncertainties
    efficienciesFast    = [ uf(effFast.GetEfficiency(i+1), (effFast.GetEfficiencyErrorUp(i+1)+effFast.GetEfficiencyErrorLow(i+1))/2) for i in range(len(pt_thresholds)) ] # root bin numbers start with 1 (0 is the underflow bin)
    efficienciesFull    = [ uf(effFull.GetEfficiency(i+1), (effFull.GetEfficiencyErrorUp(i+1)+effFull.GetEfficiencyErrorLow(i+1))/2) for i in range(len(pt_thresholds)) ] # root bin numbers start with 1 (0 is the underflow bin)
    ratio = [ uf(effFull.GetEfficiency(i+1), (effFull.GetEfficiencyErrorUp(i+1)+effFull.GetEfficiencyErrorLow(i+1))/2)/uf(effFast.GetEfficiency(i+1), (effFast.GetEfficiencyErrorUp(i+1)+effFast.GetEfficiencyErrorLow(i+1))/2) for i in range(len(pt_thresholds)) ] 
    
    bin_str = [ "%s-%s"%(pt_thresholds[i], pt_thresholds[i+1]) for i in range(len(pt_thresholds)) if i<len(pt_thresholds)-1 ] + ['>2000'] # also use overflow

    print "Fast efficiencies:"
    for i, e in enumerate(efficienciesFast):
      print "{:15}{:6.3f}{:6.3f}".format(bin_str[i], e.val, e.sigma)
    print "Full efficiencies:"
    for i, e in enumerate(efficienciesFull):
      print "{:15}{:6.3f}{:6.3f}".format(bin_str[i], e.val, e.sigma)
    print "Full/Fast:"
    for i, r in enumerate(ratio):
      print "{:15}{:6.3f}{:6.3f}".format(bin_str[i], r.val, r.sigma)
#      with open('ratio.txt', 'a') as f:
#        print >> f, "{:6.3f}{:6.3f}".format(r.val, r.sigma)

# plotting
ROOT.gStyle.SetOptStat(0) # get rid of stat box

#bins = 18 # Ensures edge of merged bins in new hist match bin edges of old hist
#minpt = 200
#maxpt = 2000

binning = array.array('d',pt_thresholds)
#numberOfBins = len(pt_thresholds)-1
binningArgs = (len(binning)-1, binning)

figSizeX = 500
figSizeY = 500
#%%%%%%%%%%
print "plotting full"
histFullEff = ROOT.TH1D("histFullEff","deepTagMD_HbbvsQCD Efficiency vs pT (Full);pT [GeV];efficiency", *binningArgs)
histFullEff.SetLineColor(ROOT.kGreen+1)
histFullEff.SetLineWidth(2)
histFullEff.SetMarkerStyle(1)
# properly bin
#histFullEff.Rebin(numberOfBins,"",binning)
for i, e in enumerate(efficienciesFull):
  if(i == (len(efficienciesFull) - 1)):
    break # dont want > 2000
  print((pt_thresholds[i+1] + pt_thresholds[i])/2)
  histFullEff.Fill((pt_thresholds[i+1]+pt_thresholds[i])/2, e.val)
  histFullEff.SetBinError(i+1,e.sigma)
fullCan = ROOT.TCanvas("fullCan","",figSizeX,figSizeY)
fullCan.Draw()
histFullEff.SetAxisRange(0.2,0.8,"Y")
histFullEff.Draw()
histFullEff.Draw("hist same")
fullCan.SaveAs("FullHist.png")
#%%%%%%%%%%
print "plotting fast"
histFastEff = ROOT.TH1D("histFastEff","deepTagMD_HbbvsQCD Efficiency vs pT (Fast);pT [GeV];efficiency", *binningArgs)
histFastEff.SetLineColor(ROOT.kGreen+1)
histFastEff.SetLineWidth(2)
histFastEff.SetMarkerStyle(1)
# properly bin
#histFastEff.Rebin(numberOfBins,"",binning)
# fill hist and set error bars
for i, e in enumerate(efficienciesFast):
  if(i == (len(efficienciesFast) - 1)):
    break # dont want > 2000
  print((pt_thresholds[i+1] + pt_thresholds[i])/2)
  histFastEff.Fill((pt_thresholds[i+1]+pt_thresholds[i])/2, e.val)
  histFastEff.SetBinError(i+1,e.sigma)
fastCan = ROOT.TCanvas("fastCan","",figSizeX,figSizeY)
fastCan.Draw()
histFastEff.SetAxisRange(0.2,0.8,"Y")
histFastEff.Draw()
histFastEff.Draw("hist same")
fastCan.SaveAs("FastHist.png")
#%%%%%%%%%%
print "plotting Full/Fast"
full_fast = ROOT.TH1D("full_fast","deepTagMD_HbbvsQCD Full/Fast vs pT;pT [GeV];Full/Fast", *binningArgs)
full_fast.SetLineColor(ROOT.kGreen+1)
full_fast.SetLineWidth(2)
full_fast.SetMarkerStyle(1)
# properly bin
#full_fast.Rebin(numberOfBins,"",binning)
# fill hist and set error bars
for i, r in enumerate(ratio):
  if(i == (len(ratio)-1)):
    break # don't want > 2000
  print((pt_thresholds[i+1] + pt_thresholds[i])/2)
  full_fast.Fill((pt_thresholds[i+1]+pt_thresholds[i])/2, r.val)
  full_fast.SetBinError(i+1,r.sigma)
full_fastCan = ROOT.TCanvas("full_fastCan","",figSizeX,figSizeY)
# drawing y = 1 line
onebin = [min(pt_thresholds),max(pt_thresholds)]
onebinArgs = (1, array.array('d', onebin))
one = ROOT.TH1D("","",*onebinArgs)
one.SetBinContent(1,1)
one.SetLineColor(ROOT.kBlack)
full_fastCan.Draw()
full_fast.SetAxisRange(0.8,1.2,"Y")
full_fast.Draw()
full_fast.Draw("hist same")
one.Draw("hist same")
full_fastCan.SaveAs("FulloverFastHist.png")

# terminate program
sys.exit(0)
#%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%

#####         #    eff     = [ h_pass.Integral(i+1,i+2)/h_all.Integral(i+1,i+2) for i in range(len(pt_thresholds)) ] # root bin numbers start with 1 (0 is the underflow bin)
#####     #    print(eff)
#####     #    for i in range(len(eff)):
#####     #      print(eff[i])
#####         bin_str = [ "%s-%s"%(pt_thresholds[i], pt_thresholds[i+1]) for i in range(len(pt_thresholds)) if i<len(pt_thresholds)-1 ] + ['>2000'] # also use overflow
#####     #    print(bin_str)
#####     #    for i in range(len(bin_str)):
#####     #      print(bin_str[i])
#####     
#####     #    with open('out.txt', 'a') as f:
#####         errorbars = []
#####         print
#####         print "| {:15}|{:>17} |".format("pt bin (GeV)", "efficiency")
#####         print "| "+"-"*33+" |"
#####         for i, eff in enumerate(efficiencies):
#####     #    for i in range(len(eff)):#, eff in enumerate(eff):
#####           #        print "| {:15}|{:6.3f} +/- {:6.3f} |".format(bin_str[i], eff.val, eff.sigma)
#####                     #print >> f, 'Filename:', filename     # Python 2.x
#####             #print('Filename:', filename, file=f)  # Python 3.x
#####           print "| {:15}|{:6.3f} +/- {:6.3f} |".format(bin_str[i], eff.val, eff.sigma)
#####           errorbars.append(eff.sigma)
#####     #print "| {:15}|{:6.3f} |".format(bin_str[i], eff[i])
#####           with open('out.txt', 'a') as f:
#####             print >> f, "{:15}{:6.3f}{:6.3f}".format(bin_str[i], eff.val,eff.sigma)
#####     #        print >> f, "{:15}{:6.3f}".format(bin_str[i], eff[i])
#####     
#####     y = []
#####     for i, eff in enumerate(efficiencies):
#####       y.append(eff.val)
#####     #y = eff
#####     
#####     #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#####     # ROOT plotting code
#####     
#####     ROOT.gStyle.SetOptStat(0)
#####     bins = 18 # Ensures edge of merged bins in new hist match bin edges of old hist
#####     minpt = 200
#####     maxpt = 2000
#####     h1 = ROOT.TH1F("h1","deepTagMD_HbbvsQCD Full/Fast vs pT",bins,minpt,maxpt)
#####     for i in range(len(y)):
#####       print pt_thresholds[i]
#####       print y[i]
#####       h1.Fill(pt_thresholds[i],y[i])
#####       h1.SetBinError(i,errobars[i])
#####     binning = array.array('d', pt_thresholds)
#####     h1.Rebin(len(pt_thresholds)-1,"", binning)
#####     sizex = 500
#####     sizey = 500
#####     can = ROOT.TCanvas("can","",sizex,sizey)
#####     can.Draw()
#####     h1.Draw()
#####     h1.Draw("hist same")
#####     can.SaveAs("Full_Fast_ratio.png")
#####     #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#####     # matplotlib plotting code
#####     
#####     #f = plt.figure()
#####     plt.scatter(pt_thresholds, y)#, label='inclusive = '+str(h_pass.Integral()/h_all.Integral()))
#####     plt.errorbar(pt_thresholds, y, yerr=errorbars, ls='none')
#####     plt.xlabel('p_T [GeV]')
#####     plt.ylabel('EFficiency')
#####     simType = 'Full' if not options.fastSim else 'Fast'
#####     plt.title('deepTagMD_HbbvsQCD Efficiency vs p_T (' + simType + ')')
#####     plt.annotate('inclusive = '+str(h_pass.Integral()/h_all.Integral()), xy=(0.05,0.95), xycoords='axes fraction')
#####     #plt.legend()
#####     plt.savefig(simType + '.png')
#####     #plt.show()
#####     #f.savefig("out.pdf")    

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
# hpass hall divide them as in like 182
# t efficiency instead of .divide
# efificneis and scale factos for different taggers
# WP = 0.8
# 158 and 156
# mesure scale factors for all the year after we get 2018 and 2016
# how do we check
 
# got a reply
# we should look at jet response for their samples
# daniel will send me instructions on how to copy over
# small step in between: switch out JEC
# daniel will c

# tried to find good way to find ttbar background. we cannot probperly estimate background with lost lepton
# extracting from lower to higher MCT region. Monte CArlo predicts this. 
# stick with MCT method bc it has higher stastitics for most of the region
# lost lepton bacground estimate for cross check.
# a hybrid method use one for low met and one for high met and sperated for boosted/not boosted
# high met regions lost lepton would have higehr statitiscs
# we have some systematic uncertainties ... if we see large discrepancy then we assign difference as systematics 
# if we have differnce than we have a big problem anyway
# first give full status talk about whole anayslis and plan for background and () uncertiaintes
# if we get approval then we can un... signal regions 
# first blind analysis then unblinding then pre-approval which is a talk where you describe the whole analysis 
# should start this in 3 week sbut before they want to hear 

