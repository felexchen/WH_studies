'''
Some plots for comparing FastSim and FullSim for SUSY signals
This uses the RootTools package to handle samples, make histograms and produce plots

'''

import ROOT

from RootTools.core.standard import *

### 2016
## FullSim samples
#fullSim      = Sample.fromDirectory("FullSim",    "/hadoop/cms/store/user/dspitzba/nanoAOD/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/") # original file
fullSim      = Sample.fromFiles("FullSim",    ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FullSim_JEC.root"])

## FastSim sample, only 850,1 mass point
fastSim      = Sample.fromFiles("FastSim",    ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FastSim_JEC.root"])

# Apply MET filters
fullSim.setSelectionString("Flag_goodVertices&&Flag_globalSuperTightHalo2016Filter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_ecalBadCalibFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilterV2")

fastSim.setSelectionString("Flag_goodVertices&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_ecalBadCalibFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilter")

# Select events with one higgs tag (medium WP)
presel  = 'nFatJet>0&&Sum$(FatJet_pt>200&&FatJet_deepTagMD_HbbvsQCD>0.8695)>0'
preselHighPt  = 'nFatJet>0&&Sum$(FatJet_pt>500&&FatJet_deepTagMD_HbbvsQCD>0.8695)>0'

plot_path = './FatJet_FastFull/'

## JECs and jet responses
h_profile_JEC_full = fullSim.get1DHistoFromDraw(variableString="FatJet_pt/(FatJet_pt*(1-FatJet_rawFactor)):FatJet_pt", binning=[170, 200, 250, 300, 400, 600, 1000, 1500, 2000], binningIsExplicit=True, isProfile=True, selectionString=presel)
h_profile_JEC_fast = fastSim.get1DHistoFromDraw(variableString="FatJet_corr_JEC:FatJet_pt_nom", binning=[170, 200, 250, 300, 400, 600, 1000, 1500, 2000], binningIsExplicit=True, isProfile=True, selectionString=presel)

h_profile_response_b_full = fullSim.get1DHistoFromDraw(variableString="Jet_pt/GenJet_pt[Jet_genJetIdx]:Jet_pt", binning=[30,50,70,100,130, 170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&Jet_hadronFlavour==5&&Jet_genJetIdx>-1')
h_profile_response_b_fast = fastSim.get1DHistoFromDraw(variableString="Jet_pt_nom/GenJet_pt[Jet_genJetIdx]:Jet_pt_nom", binning=[30,50,70,100,130,170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&Jet_hadronFlavour==5&&Jet_genJetIdx>-1')

h_profile_response_ISR_full = fullSim.get1DHistoFromDraw(variableString="Jet_pt/GenJet_pt[Jet_genJetIdx]:Jet_pt", binning=[30,50,70,100,130, 170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&!(Jet_hadronFlavour==5)&&Jet_btagDeepB<0.4941&&Jet_genJetIdx>-1')
h_profile_response_ISR_fast = fastSim.get1DHistoFromDraw(variableString="Jet_pt_nom/GenJet_pt[Jet_genJetIdx]:Jet_pt_nom", binning=[30,50,70,100,130,170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&!(Jet_hadronFlavour==5)&&Jet_btagDeepB<0.4941&&Jet_genJetIdx>-1')

## styles
h_profile_JEC_fast.legendText = 'FastSim'
h_profile_JEC_full.legendText = 'FullSim'
h_profile_JEC_fast.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
h_profile_JEC_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

h_profile_response_b_fast.legendText = 'FastSim'
h_profile_response_b_full.legendText = 'FullSim'
h_profile_response_b_fast.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
h_profile_response_b_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

h_profile_response_ISR_fast.legendText = 'FastSim'
h_profile_response_ISR_full.legendText = 'FullSim'
h_profile_response_ISR_fast.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
h_profile_response_ISR_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

plotting.draw(
    Plot.fromHisto(name = 'JEC_AK8', histos = [ [h_profile_JEC_fast], [h_profile_JEC_full] ], texX = "p_{T} (AK8) (GeV)", texY = "jet energy correction"),
    plot_directory = plot_path,
    logX = False, logY = False, sorting = False,
    #scaling = {1:0, 2:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange':(0.95,1.35)},
)

plotting.draw(
    Plot.fromHisto(name = 'response_b', histos = [ [h_profile_response_b_fast], [h_profile_response_b_full] ], texX = "p_{T} (b-jet) (GeV)", texY = "response"),
    plot_directory = plot_path,
    logX = False, logY = False, sorting = False,
    yRange = (0.9,1.8),
    #scaling = {1:0, 2:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

plotting.draw(
    Plot.fromHisto(name = 'response_ISR', histos = [ [h_profile_response_ISR_fast], [h_profile_response_ISR_full] ], texX = "p_{T} (light jet) (GeV)", texY = "response"),
    plot_directory = plot_path,
    logX = False, logY = False, sorting = False,
    yRange = (0.9,1.8),
    #scaling = {1:0, 2:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

