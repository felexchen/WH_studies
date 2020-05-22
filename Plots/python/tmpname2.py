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
fullSim.setSelectionString("Flag_goodVertices&&Flag_globalSuperTightHalo2016Filter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilterV2")

fastSim.setSelectionString("Flag_goodVertices&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilterV2")

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

## ##################################################
## # charged electromagnetic energy b jet | pt > 400
## 
## b_charged_em_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## b_charged_em_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## 
## b_charged_em_energy_400.legendText      = 'FastSim'
## b_charged_em_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## b_charged_em_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_charged_em_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b charged em energy 400', histos = [ [b_charged_em_energy_400], [b_charged_em_energy_400_full] ], texX = "b charged em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # charged electromagnetic energy b jet | pt > 30
## 
## b_charged_em_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## b_charged_em_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## 
## b_charged_em_energy_30.legendText      = 'FastSim'
## b_charged_em_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## b_charged_em_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_charged_em_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b charged em energy 30', histos = [ [b_charged_em_energy_30], [b_charged_em_energy_30_full] ], texX = "b charged em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## 
## #################### 
## # charged electromagnetic energy ISR | pt > 400
## 
## ISR_charged_em_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## ISR_charged_em_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## 
## ISR_charged_em_energy_400.legendText      = 'FastSim'
## ISR_charged_em_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## ISR_charged_em_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_charged_em_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR charged em energy 400', histos = [ [ISR_charged_em_energy_400], [ISR_charged_em_energy_400_full] ], texX = "ISR charged em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # charged electromagnetic energy ISR jet | pt > 30
## 
## ISR_charged_em_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## ISR_charged_em_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chEmEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## 
## ISR_charged_em_energy_30.legendText      = 'FastSim'
## ISR_charged_em_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## ISR_charged_em_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_charged_em_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR charged em energy 30', histos = [ [ISR_charged_em_energy_30], [ISR_charged_em_energy_30_full] ], texX = "ISR charged em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
##  
## ##################################################
## # charged hadron energy b jet | pt > 400
## 
## b_charged_hadron_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## b_charged_hadron_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## 
## b_charged_hadron_energy_400.legendText      = 'FastSim'
## b_charged_hadron_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## b_charged_hadron_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_charged_hadron_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b charged hadron energy 400', histos = [ [b_charged_hadron_energy_400], [b_charged_hadron_energy_400_full] ], texX = "b charged hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # charged hadron energy b jet | pt > 30
## 
## b_charged_hadron_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## b_charged_hadron_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## 
## b_charged_hadron_energy_30.legendText      = 'FastSim'
## b_charged_hadron_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## b_charged_hadron_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_charged_hadron_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b charged hadron energy 30', histos = [ [b_charged_hadron_energy_30], [b_charged_hadron_energy_30_full] ], texX = "b charged hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## 
## #################### 
## # charged hadron energy ISR | pt > 400
## 
## ISR_charged_hadron_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## ISR_charged_hadron_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## 
## ISR_charged_hadron_energy_400.legendText      = 'FastSim'
## ISR_charged_hadron_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## ISR_charged_hadron_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_charged_hadron_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR charged hadron energy 400', histos = [ [ISR_charged_hadron_energy_400], [ISR_charged_hadron_energy_400_full] ], texX = "ISR charged hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # charged hadron energy ISR jet | pt > 30
## 
## ISR_charged_hadron_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## ISR_charged_hadron_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_chHEF', [25,1,1600], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## 
## ISR_charged_hadron_energy_30.legendText      = 'FastSim'
## ISR_charged_hadron_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## ISR_charged_hadron_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_charged_hadron_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR charged hadron energy 30', histos = [ [ISR_charged_hadron_energy_30], [ISR_charged_hadron_energy_30_full] ], texX = "ISR charged hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
##  
## ##################################################
## # neutral electromagnetic energy b jet | pt > 400
## 
## b_neutral_em_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## b_neutral_em_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## 
## b_neutral_em_energy_400.legendText      = 'FastSim'
## b_neutral_em_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## b_neutral_em_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_neutral_em_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b neutral em energy 400', histos = [ [b_neutral_em_energy_400], [b_neutral_em_energy_400_full] ], texX = "b neutral em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # neutral electromagnetic energy b jet | pt > 30
## 
## b_neutral_em_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## b_neutral_em_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## 
## b_neutral_em_energy_30.legendText      = 'FastSim'
## b_neutral_em_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## b_neutral_em_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_neutral_em_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b neutral em energy 30', histos = [ [b_neutral_em_energy_30], [b_neutral_em_energy_30_full] ], texX = "b neutral em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## 
## #################### 
## # neutral electromagnetic energy ISR | pt > 400
## 
## ISR_neutral_em_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## ISR_neutral_em_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## 
## ISR_neutral_em_energy_400.legendText      = 'FastSim'
## ISR_neutral_em_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## ISR_neutral_em_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_neutral_em_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR neutral em energy 400', histos = [ [ISR_neutral_em_energy_400], [ISR_neutral_em_energy_400_full] ], texX = "ISR neutral em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # neutral electromagnetic energy ISR jet | pt > 30
## 
## ISR_neutral_em_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## ISR_neutral_em_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neEmEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## 
## ISR_neutral_em_energy_30.legendText      = 'FastSim'
## ISR_neutral_em_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## ISR_neutral_em_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_neutral_em_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR neutral em energy 30', histos = [ [ISR_neutral_em_energy_30], [ISR_neutral_em_energy_30_full] ], texX = "ISR neutral em energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
##  
## ##################################################
## # neutral hadron energy b jet | pt > 400
## 
## b_neutral_hadron_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## b_neutral_hadron_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## 
## b_neutral_hadron_energy_400.legendText      = 'FastSim'
## b_neutral_hadron_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## b_neutral_hadron_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_neutral_hadron_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b neutral hadron energy 400', histos = [ [b_neutral_hadron_energy_400], [b_neutral_hadron_energy_400_full] ], texX = "b neutral hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # neutral hadron energy b jet | pt > 30
## 
## b_neutral_hadron_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## b_neutral_hadron_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## 
## b_neutral_hadron_energy_30.legendText      = 'FastSim'
## b_neutral_hadron_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## b_neutral_hadron_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_neutral_hadron_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b neutral hadron energy 30', histos = [ [b_neutral_hadron_energy_30], [b_neutral_hadron_energy_30_full] ], texX = "b neutral hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
##  
## ####################
## # neutral hadron energy ISR | pt > 400
## 
## ISR_neutral_hadron_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## ISR_neutral_hadron_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## 
## ISR_neutral_hadron_energy_400.legendText      = 'FastSim'
## ISR_neutral_hadron_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## ISR_neutral_hadron_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_neutral_hadron_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR neutral hadron energy 400', histos = [ [ISR_neutral_hadron_energy_400], [ISR_neutral_hadron_energy_400_full] ], texX = "ISR neutral hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # neutral hadron energy ISR jet | pt > 30
## 
## ISR_neutral_hadron_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## ISR_neutral_hadron_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_neHEF', [25,1,1200], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## 
## ISR_neutral_hadron_energy_30.legendText      = 'FastSim'
## ISR_neutral_hadron_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## ISR_neutral_hadron_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_neutral_hadron_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR neutral hadron energy 30', histos = [ [ISR_neutral_hadron_energy_30], [ISR_neutral_hadron_energy_30_full] ], texX = "ISR neutral hadron energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## 
## ##################################################
## # muon energy b jet | pt > 400
## 
## b_muon_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## b_muon_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,1200], weightString='genWeight', selectionString=bPresel400, addOverFlowBin='upper')
## 
## b_muon_energy_400.legendText      = 'FastSim'
## b_muon_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## b_muon_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_muon_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b muon energy 400', histos = [ [b_muon_energy_400], [b_muon_energy_400_full] ], texX = "b muon energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # muon energy b jet | pt > 30
## 
## b_muon_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## b_muon_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,1200], weightString='genWeight', selectionString=bPresel30, addOverFlowBin='upper')
## 
## b_muon_energy_30.legendText      = 'FastSim'
## b_muon_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## b_muon_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## b_muon_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'b muon energy 30', histos = [ [b_muon_energy_30], [b_muon_energy_30_full] ], texX = "b muon energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
##  
## ####################
## # muon energy ISR | pt > 400
## 
## ISR_muon_energy_400      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,3000], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## ISR_muon_energy_400_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,3000], weightString='genWeight', selectionString=ISRPresel400, addOverFlowBin='upper')
## 
## ISR_muon_energy_400.legendText      = 'FastSim'
## ISR_muon_energy_400_full.legendText = 'FullSim'
## 
## ## styles
## ISR_muon_energy_400.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_muon_energy_400_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR muon energy 400', histos = [ [ISR_muon_energy_400], [ISR_muon_energy_400_full] ], texX = "ISR muon energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
## ####################
## # muon energy ISR jet | pt > 30
## 
## ISR_muon_energy_30      = fastSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,3000], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## ISR_muon_energy_30_full = fullSim.get1DHistoFromDraw('Jet_pt*Jet_muEF', [25,1,3000], weightString='genWeight', selectionString=ISRPresel30, addOverFlowBin='upper')
## 
## ISR_muon_energy_30.legendText      = 'FastSim'
## ISR_muon_energy_30_full.legendText = 'FullSim'
## 
## ## styles
## ISR_muon_energy_30.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
## ISR_muon_energy_30_full.style = styles.lineStyle(ROOT.kBlue+1,   width=2, errors=True)
## 
## # do actual plotting
## plotting.draw(
##     Plot.fromHisto(name = 'ISR muon energy 30', histos = [ [ISR_muon_energy_30], [ISR_muon_energy_30_full] ], texX = "ISR muon energy", texY = "a.u."),
##     plot_directory = plot_path,
##     logX = False, logY = True, sorting = False,
##     scaling = {1:0},
##     ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange': (0.1,3.0)},
## )
##  
## ##################################################

h_CaloMET_reco    = fastSim.get1DHistoFromDraw('CaloMET_pt',  [25,0,1000], weightString='genWeight', selectionString=presel, addOverFlowBin='upper')
#h_CaloMET_jec     = fastSim.get1DHistoFromDraw('CaloMET_pt_nom',  [25,0,2000], weightString='genWeight', selectionString=presel, addOverFlowBin='upper')
h_CaloMET_full    = fullSim.get1DHistoFromDraw('CaloMET_pt',  [25,0,1000], weightString='genWeight', selectionString=presel, addOverFlowBin='upper')

h_CaloMET_incl_reco    = fastSim.get1DHistoFromDraw('CaloMET_pt',       [25,0,2000], weightString='genWeight', selectionString='(1)', addOverFlowBin='upper')
#h_CaloMET_incl_jec     = fastSim.get1DHistoFromDraw('CaloMET_pt_nom',   [25,0,2000], weightString='genWeight', selectionString='(1)', addOverFlowBin='upper')
h_CaloMET_incl_full    = fullSim.get1DHistoFromDraw('CaloMET_pt',       [25,0,2000], weightString='genWeight', selectionString='(1)', addOverFlowBin='upper')

h_CaloMET_coarse_reco    = fastSim.get1DHistoFromDraw('CaloMET_pt',       [0,125,200,300,400,600], binningIsExplicit=True, weightString='genWeight', selectionString='(1)', addOverFlowBin='upper')
#h_CaloMET_coarse_jec     = fastSim.get1DHistoFromDraw('CaloMET_pt_nom',   [0,125,200,300,400,600], binningIsExplicit=True, weightString='genWeight', selectionString='(1)', addOverFlowBin='upper')
h_CaloMET_coarse_full    = fullSim.get1DHistoFromDraw('CaloMET_pt',       [0,125,200,300,400,600], binningIsExplicit=True, weightString='genWeight', selectionString='(1)', addOverFlowBin='upper')

h_CaloMET_reco.legendText = 'FastSim'
#h_CaloMET_jec.legendText  = 'FastSim, JEC reapplied'
h_CaloMET_full.legendText = 'FullSim'
h_CaloMET_reco.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
#h_CaloMET_jec.style       = styles.lineStyle(ROOT.kRed+1,   width=2, errors=True)
h_CaloMET_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

h_CaloMET_incl_reco.legendText = 'FastSim'
#h_CaloMET_incl_jec.legendText  = 'FastSim, JEC reapplied'
h_CaloMET_incl_full.legendText = 'FullSim'
h_CaloMET_incl_reco.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
#h_CaloMET_incl_jec.style       = styles.lineStyle(ROOT.kRed+1,   width=2, errors=True)
h_CaloMET_incl_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

h_CaloMET_coarse_reco.legendText = 'FastSim'
#h_CaloMET_coarse_jec.legendText  = 'FastSim, JEC reapplied'
h_CaloMET_coarse_full.legendText = 'FullSim'
h_CaloMET_coarse_reco.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
#h_CaloMET_coarse_jec.style       = styles.lineStyle(ROOT.kRed+1,   width=2, errors=True)
h_CaloMET_coarse_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

plotting.draw(
    Plot.fromHisto(name = 'CaloMET_pt', histos = [ [h_CaloMET_reco], [h_CaloMET_full] ], texX = "Calo p_{T}^{miss} (GeV)", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},#, 2:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

plotting.draw(
    Plot.fromHisto(name = 'CaloMET_pt_incl', histos = [ [h_CaloMET_incl_reco], 
                                                        #[h_CaloMET_incl_jec], 
                                                        [h_CaloMET_incl_full] ], texX = "Calo p_{T}^{miss} incl (GeV)", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},#, 2:0},
    ratio = {'histos': [(0,1)
                        #(0,2), 
                        #(1,2)
                        ], 'texY': 'x / FullSim'},
)

plotting.draw(
    Plot.fromHisto(name = 'CaloMET_pt_coarse', histos = [ [h_CaloMET_coarse_reco], 
                                                          #[h_CaloMET_coarse_jec], 
                                                          [h_CaloMET_coarse_full] ], texX = "Calo p_{T}^{miss} coarse (GeV)", texY = "a.u."),
    plot_directory = plot_path,
    logX = False, logY = True, sorting = False,
    scaling = {1:0},#, 2:0},
    ratio = {'histos': [(0,1),
                        #(0,2), 
                        #(1,2)
                        ], 'texY': 'x / FullSim'},
)
