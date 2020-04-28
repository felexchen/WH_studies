'''
Some plots for comparing FastSim and FullSim for SUSY signals
This uses the RootTools package to handle samples, make histograms and produce plots

'''

import ROOT

from RootTools.core.standard import *

##################################################
### 2016
## FullSim samples
#fullSim      = Sample.fromDirectory("FullSim",    "/hadoop/cms/store/user/dspitzba/nanoAOD/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/") # original file
fullSim      = Sample.fromFiles("FullSim",    ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FullSim_JEC.root"])

## FastSim sample, only 850,1 mass point
fastSim      = Sample.fromFiles("FastSim",    ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FastSim_JEC.root"])

##################################################
# Apply MET filters
fullSim.setSelectionString("Flag_goodVertices&&Flag_globalSuperTightHalo2016Filter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_ecalBadCalibFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilterV2")

fastSim.setSelectionString("Flag_goodVertices&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_ecalBadCalibFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilter")

##################################################
# Select events with one higgs tag (medium WP)

# more than one fat jet
# AND
# sum of () > 0
# () = fat jet pt > 200 AND fat jet deep tag  
presel        = 'nFatJet>0&&Sum$(FatJet_pt>200&&FatJet_deepTagMD_HbbvsQCD>0.8695)>0' 
# same as above, except fat jet pt > 500
preselHighPt  = 'nFatJet>0&&Sum$(FatJet_pt>500&&FatJet_deepTagMD_HbbvsQCD>0.8695)>0'

# pt > 400 
# AND
# absolute value of eta < 2.4 (aka "central" jets only)
# AND
# jet id
# AND
# 5 = b quarks (or non b)
# AND
# btag > 0.4941 for b quarks (or non b)
bPresel400   = 'Jet_pt>400&&abs(Jet_eta)<2.4&&Jet_jetId&&Jet_hadronFlavour==5&&Jet_btagDeepB>0.4941'
ISRPresel400 = 'Jet_pt>400&&abs(Jet_eta)<2.4&&Jet_jetId&&!(Jet_hadronFlavour==5)&&Jet_btagDeepB<0.4941'
# same as above, except pt > 30
bPresel30    = 'Jet_pt>30&&abs(Jet_eta)<2.4&&Jet_jetId&&Jet_hadronFlavour==5&&Jet_btagDeepB>0.4941'
ISRPresel30  = 'Jet_pt>30&&abs(Jet_eta)<2.4&&Jet_jetId&&!(Jet_hadronFlavour==5)&&Jet_btagDeepB<0.4941'
##################################################
# plot path
plot_path = './tmp_plots/'

##################################################
# charged electromagnetic energy fraction b jet | pt > 400

b_charged_em_EF_400      = fastSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
b_charged_em_EF_400_full = fullSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')

b_charged_em_EF_400.legendText      = 'FastSim'
b_charged_em_EF_400_full.legendText = 'FullSim'

## styles
b_charged_em_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_charged_em_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b charged em energy fraction 400', histos = [ [b_charged_em_EF_400], [b_charged_em_EF_400_full] ], texX = "b charged em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# charged electromagnetic energy fraction b jet | pt > 30

b_charged_em_EF_30      = fastSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
b_charged_em_EF_30_full = fullSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')

b_charged_em_EF_30.legendText      = 'FastSim'
b_charged_em_EF_30_full.legendText = 'FullSim'

## styles
b_charged_em_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_charged_em_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b charged em energy fraction 30', histos = [ [b_charged_em_EF_30], [b_charged_em_EF_30_full] ], texX = "b charged em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

#################### 
# charged electromagnetic energy fraction ISR | pt > 400

ISR_charged_em_EF_400      = fastSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
ISR_charged_em_EF_400_full = fullSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')

ISR_charged_em_EF_400.legendText      = 'FastSim'
ISR_charged_em_EF_400_full.legendText = 'FullSim'

## styles
ISR_charged_em_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_charged_em_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR charged em energy fraction 400', histos = [ [ISR_charged_em_EF_400], [ISR_charged_em_EF_400_full] ], texX = "ISR charged em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# charged electromagnetic energy fraction ISR jet | pt > 30

ISR_charged_em_EF_30      = fastSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
ISR_charged_em_EF_30_full = fullSim.get1DHistoFromDraw('Jet_chEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')

ISR_charged_em_EF_30.legendText      = 'FastSim'
ISR_charged_em_EF_30_full.legendText = 'FullSim'

## styles
ISR_charged_em_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_charged_em_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR charged em energy fraction 30', histos = [ [ISR_charged_em_EF_30], [ISR_charged_em_EF_30_full] ], texX = "ISR charged em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
 
##################################################
# charged hadron energy fraction b jet | pt > 400

b_charged_hadron_EF_400      = fastSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
b_charged_hadron_EF_400_full = fullSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')

b_charged_hadron_EF_400.legendText      = 'FastSim'
b_charged_hadron_EF_400_full.legendText = 'FullSim'

## styles
b_charged_hadron_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_charged_hadron_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b charged hadron energy fraction 400', histos = [ [b_charged_hadron_EF_400], [b_charged_hadron_EF_400_full] ], texX = "b charged hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# charged hadron energy fraction b jet | pt > 30

b_charged_hadron_EF_30      = fastSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
b_charged_hadron_EF_30_full = fullSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')

b_charged_hadron_EF_30.legendText      = 'FastSim'
b_charged_hadron_EF_30_full.legendText = 'FullSim'

## styles
b_charged_hadron_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_charged_hadron_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b charged hadron energy fraction 30', histos = [ [b_charged_hadron_EF_30], [b_charged_hadron_EF_30_full] ], texX = "b charged hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

#################### 
# charged hadron energy fraction ISR | pt > 400

ISR_charged_hadron_EF_400      = fastSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
ISR_charged_hadron_EF_400_full = fullSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')

ISR_charged_hadron_EF_400.legendText      = 'FastSim'
ISR_charged_hadron_EF_400_full.legendText = 'FullSim'

## styles
ISR_charged_hadron_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_charged_hadron_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR charged hadron energy fraction 400', histos = [ [ISR_charged_hadron_EF_400], [ISR_charged_hadron_EF_400_full] ], texX = "ISR charged hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# charged hadron energy fraction ISR jet | pt > 30

ISR_charged_hadron_EF_30      = fastSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
ISR_charged_hadron_EF_30_full = fullSim.get1DHistoFromDraw('Jet_chHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')

ISR_charged_hadron_EF_30.legendText      = 'FastSim'
ISR_charged_hadron_EF_30_full.legendText = 'FullSim'

## styles
ISR_charged_hadron_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_charged_hadron_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR charged hadron energy fraction 30', histos = [ [ISR_charged_hadron_EF_30], [ISR_charged_hadron_EF_30_full] ], texX = "ISR charged hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
 
##################################################
# neutral electromagnetic energy fraction b jet | pt > 400

b_neutral_em_EF_400      = fastSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
b_neutral_em_EF_400_full = fullSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')

b_neutral_em_EF_400.legendText      = 'FastSim'
b_neutral_em_EF_400_full.legendText = 'FullSim'

## styles
b_neutral_em_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_neutral_em_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b neutral em energy fraction 400', histos = [ [b_neutral_em_EF_400], [b_neutral_em_EF_400_full] ], texX = "b neutral em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# neutral electromagnetic energy fraction b jet | pt > 30

b_neutral_em_EF_30      = fastSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
b_neutral_em_EF_30_full = fullSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')

b_neutral_em_EF_30.legendText      = 'FastSim'
b_neutral_em_EF_30_full.legendText = 'FullSim'

## styles
b_neutral_em_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_neutral_em_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b neutral em energy fraction 30', histos = [ [b_neutral_em_EF_30], [b_neutral_em_EF_30_full] ], texX = "b neutral em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

#################### 
# neutral electromagnetic energy fraction ISR | pt > 400

ISR_neutral_em_EF_400      = fastSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
ISR_neutral_em_EF_400_full = fullSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')

ISR_neutral_em_EF_400.legendText      = 'FastSim'
ISR_neutral_em_EF_400_full.legendText = 'FullSim'

## styles
ISR_neutral_em_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_neutral_em_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR neutral em energy fraction 400', histos = [ [ISR_neutral_em_EF_400], [ISR_neutral_em_EF_400_full] ], texX = "ISR neutral em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# neutral electromagnetic energy fraction ISR jet | pt > 30

ISR_neutral_em_EF_30      = fastSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
ISR_neutral_em_EF_30_full = fullSim.get1DHistoFromDraw('Jet_neEmEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')

ISR_neutral_em_EF_30.legendText      = 'FastSim'
ISR_neutral_em_EF_30_full.legendText = 'FullSim'

## styles
ISR_neutral_em_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_neutral_em_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR neutral em energy fraction 30', histos = [ [ISR_neutral_em_EF_30], [ISR_neutral_em_EF_30_full] ], texX = "ISR neutral em energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
 
##################################################
# neutral hadron energy fraction b jet | pt > 400

b_neutral_hadron_EF_400      = fastSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
b_neutral_hadron_EF_400_full = fullSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')

b_neutral_hadron_EF_400.legendText      = 'FastSim'
b_neutral_hadron_EF_400_full.legendText = 'FullSim'

## styles
b_neutral_hadron_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_neutral_hadron_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b neutral hadron energy fraction 400', histos = [ [b_neutral_hadron_EF_400], [b_neutral_hadron_EF_400_full] ], texX = "b neutral hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# neutral hadron energy fraction b jet | pt > 30

b_neutral_hadron_EF_30      = fastSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
b_neutral_hadron_EF_30_full = fullSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')

b_neutral_hadron_EF_30.legendText      = 'FastSim'
b_neutral_hadron_EF_30_full.legendText = 'FullSim'

## styles
b_neutral_hadron_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_neutral_hadron_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b neutral hadron energy fraction 30', histos = [ [b_neutral_hadron_EF_30], [b_neutral_hadron_EF_30_full] ], texX = "b neutral hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
 
####################
# neutral hadron energy fraction ISR | pt > 400

ISR_neutral_hadron_EF_400      = fastSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
ISR_neutral_hadron_EF_400_full = fullSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')

ISR_neutral_hadron_EF_400.legendText      = 'FastSim'
ISR_neutral_hadron_EF_400_full.legendText = 'FullSim'

## styles
ISR_neutral_hadron_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_neutral_hadron_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR neutral hadron energy fraction 400', histos = [ [ISR_neutral_hadron_EF_400], [ISR_neutral_hadron_EF_400_full] ], texX = "ISR neutral hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# neutral hadron energy fraction ISR jet | pt > 30

ISR_neutral_hadron_EF_30      = fastSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
ISR_neutral_hadron_EF_30_full = fullSim.get1DHistoFromDraw('Jet_neHEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')

ISR_neutral_hadron_EF_30.legendText      = 'FastSim'
ISR_neutral_hadron_EF_30_full.legendText = 'FullSim'

## styles
ISR_neutral_hadron_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_neutral_hadron_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR neutral hadron energy fraction 30', histos = [ [ISR_neutral_hadron_EF_30], [ISR_neutral_hadron_EF_30_full] ], texX = "ISR neutral hadron energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

##################################################
# muon energy fraction b jet | pt > 400

b_muon_EF_400      = fastSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
b_muon_EF_400_full = fullSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')

b_muon_EF_400.legendText      = 'FastSim'
b_muon_EF_400_full.legendText = 'FullSim'

## styles
b_muon_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_muon_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b muon energy fraction 400', histos = [ [b_muon_EF_400], [b_muon_EF_400_full] ], texX = "b muon energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# muon energy fraction b jet | pt > 30

b_muon_EF_30      = fastSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
b_muon_EF_30_full = fullSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')

b_muon_EF_30.legendText      = 'FastSim'
b_muon_EF_30_full.legendText = 'FullSim'

## styles
b_muon_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
b_muon_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'b muon energy fraction 30', histos = [ [b_muon_EF_30], [b_muon_EF_30_full] ], texX = "b muon energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
 
####################
# muon energy fraction ISR | pt > 400

ISR_muon_EF_400      = fastSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
ISR_muon_EF_400_full = fullSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')

ISR_muon_EF_400.legendText      = 'FastSim'
ISR_muon_EF_400_full.legendText = 'FullSim'

## styles
ISR_muon_EF_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_muon_EF_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR muon energy fraction 400', histos = [ [ISR_muon_EF_400], [ISR_muon_EF_400_full] ], texX = "ISR muon energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
####################
# muon energy fraction ISR jet | pt > 30

ISR_muon_EF_30      = fastSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
ISR_muon_EF_30_full = fullSim.get1DHistoFromDraw('Jet_muEF', [20,0,1], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')

ISR_muon_EF_30.legendText      = 'FastSim'
ISR_muon_EF_30_full.legendText = 'FullSim'

## styles
ISR_muon_EF_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
ISR_muon_EF_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)

# do actual plotting
plotting.draw(
    Plot.fromHisto(name = 'ISR muon energy fraction 30', histos = [ [ISR_muon_EF_30], [ISR_muon_EF_30_full] ], texX = "ISR muon energy fraction", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)
 
##################################################
