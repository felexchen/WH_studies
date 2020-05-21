'''
Some plots for comparing FastSim and FullSim for SUSY signals
This uses the RootTools package to handle samples, make histograms and produce plots

'''

import ROOT

from RootTools.core.standard import *

import glob

### 2017
## FullSim samples
#fullSim      = Sample.fromDirectory("FullSim",    "/hadoop/cms/store/user/dspitzba/nanoAOD/SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_102X_mc2017_realistic_v7-v1/") # original file
#fullSim      = Sample.fromFiles("FullSim",    ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FullSim_JEC.root"])
allFull = glob.glob('/hadoop/cms/store/user/fechen/nanoAOD/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/0*.root')
fullSim = Sample.fromFiles("FullSim", allFull)
#hadoop = "/hadoop/cms/store/user/fechen/nanoAOD/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAODv6-PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/"
#fullSim = Sample.fromFiles("FullSim", [hadoop + "002DC5D6-3515-D949-BD26-59B897A7E0B4.root",
#                                       hadoop + "0092D3B4-722E-214B-9402-C885AD7C6DD8.root",
#                                       hadoop + "0858B12E-E3FC-E841-994E-725321AAFA43.root",
#                                       hadoop + "093A1F81-29A1-B848-9464-E27FF5432FC9.root",
#                                       hadoop + "0AD64945-42B2-2F43-B41A-FCF1504C7545.root",
#                                       hadoop + "0B711A4B-9FC6-C84A-A01E-87DAAAF69CCB.root",
#                                       hadoop + "0CEABD0E-3715-3148-8CE3-F862873BF556.root",
#                                       hadoop + "0F9769D4-425A-F94B-AA7B-309179396F0D.root",
#                                       hadoop + "10D46CE8-70CA-494D-BA8E-94E362998DAA.root",
#                                       hadoop + "1B6191AA-449D-3A45-9CDF-C0D4202AAF81.root",
#                                       hadoop + "1BF8E3C7-7247-934D-B135-8C6491CC4E6C.root",
#                                       hadoop + "220567B5-ED66-1243-ABF0-5EB8729568A7.root",
#                                       hadoop + "22416824-5291-D94E-8475-9A8DDCF25CE6.root",
#                                       hadoop + "4AA64837-7A3A-2C4A-A7FE-CCD5FEFB6775.root",
#                                       hadoop + "5328123C-B5B1-7240-982C-91C22BFBFF59.root",
#                                       hadoop + "54F3FC94-9AD4-2449-A288-64EF3965D04D.root",
#                                       hadoop + "557A957A-E9E5-E246-8229-D0A0AE495B30.root",
#                                       hadoop + "5A259BBC-8757-0046-88B8-4122052FD74D.root",
#                                       hadoop + "5DE0ADD6-4F10-8F40-A396-BD9A1D431642.root",
#                                       hadoop + "5E83033F-A5CC-7C4D-8736-0E6A7C9DA3E6.root",
#                                       hadoop + "667864B5-00BD-824E-8027-4AE3890A36BF.root",
#                                       hadoop + "673D0556-5988-BA48-8BE8-965B2B36B63E.root",
#                                       hadoop + "6EE0B929-E374-ED45-8F8D-24D201F928CA.root",
#                                       hadoop + "819BA76F-CA87-9340-9AC4-2DDA4D581FD0.root",
#                                       hadoop + "81EFDA64-5B49-354D-9484-85DE7D05FA2F.root",
#                                       hadoop + "848B8154-682D-CE4B-BDF7-B28086C6ACE8.root",
#                                       hadoop + "8633326F-CA38-4446-9629-10B1347ED382.root",
#                                       hadoop + "946E1F89-7B57-1E4C-8A71-2AF1F9842B79.root",
#                                       hadoop + "96005C55-A3C7-3549-B1CF-3709EFEF43A2.root",
#                                       hadoop + "99E550CD-9057-D948-BDC7-D411E3A8567B.root",
#                                       hadoop + "9C97DE2B-F887-6343-93BA-480D284758A7.root",
#                                       hadoop + "A0C1F62F-4E50-D64E-90FD-DF4597E80672.root",
#                                       hadoop + "A349BF70-4E19-2D48-96F0-4B0C0CCDE394.root",
#                                       hadoop + "AF090711-780B-8642-94E1-338103A17F67.root",
#                                       hadoop + "B2E1513F-B352-784B-A60C-BE2F9D96E4D7.root",
#                                       hadoop + "B9C94331-05BF-1A45-90E8-06A8A009B159.root",
#                                       hadoop + "BEFED70C-D7E6-994A-8BEA-B526C3B359AD.root",
#                                       hadoop + "C2B1234D-724B-C842-B9A1-F302E2689FE7.root",
#                                       hadoop + "D4A65BDD-FB33-D046-A2F5-1E5B8B3D4A85.root",
#                                       hadoop + "D948ED2A-ABEA-1E4F-A98D-D922A009A9B4.root",
#                                       hadoop + "D960041D-C435-A94E-8D09-6F76DEFF672D.root",
#                                       hadoop + "DCE0E5C3-7C9E-F148-92F6-72C76C3CD10D.root",
#                                       hadoop + "DEF2FBF1-1839-AF48-8922-136706F1FFC9.root",
#                                       hadoop + "E08EBF0E-A0DB-2A4F-AD98-0A097EFF8B8B.root",
#                                       hadoop + "E277E6ED-F3E8-AF45-8C01-A9895DDD5E0E.root",
#                                       hadoop + "E80005ED-3698-C446-B3A1-E0FBE7080560.root",
#                                       hadoop + "EF2BE14B-C2F0-1C41-BC59-83990AB4ECFE.root",
#                                       hadoop + "F08E36CF-94D2-0946-BFBE-BBC75FE0AE71.root",
#                                       hadoop + "FC93EBFA-C1D6-6C47-B662-BD18B10F2965.root",
#                                       hadoop + "FE7F7C99-F9B1-7F49-A767-193CCAFB4DF7.root"
#                                       ])

## FastSim sample, only 850,1 mass point
#fastSim      = Sample.fromFiles("FastSim",    ["/hadoop/cms/store/user/dspitzba/WH_studies/WH_FastSim_JEC.root"])
#fastSim      = Sample.fromFiles("FastSim",    ["/home/users/fechen/CMSSW_10_2_9/src/myWH_studies/postProcessing/5004E483-28E4-574A-A927-2EED3AA3309C_Skim.root"])
allFast = glob.glob('/home/users/fechen/CMSSW_10_2_9/src/myWH_studies/postProcessing/*Skim.root')
fastSim = Sample.fromFiles("FastSim", allFast)
print(allFast)
# Apply MET filters
#fullSim.setSelectionString("Flag_goodVertices&&Flag_globalSuperTightHalo2016Filter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_ecalBadCalibFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilterV2")
fullSim.setSelectionString("Flag_goodVertices&&Flag_globalSuperTightHalo2016Filter&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_ecalBadCalibFilterV2")

#fastSim.setSelectionString("Flag_goodVertices&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_ecalBadCalibFilter&&Flag_BadPFMuonFilter&&Flag_BadChargedCandidateFilter&&Flag_ecalBadCalibFilter")
fastSim.setSelectionString("Flag_goodVertices&&Flag_HBHENoiseFilter&&Flag_HBHENoiseIsoFilter&&Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_BadPFMuonFilter&&Flag_ecalBadCalibFilterV2")

# Select events with one higgs tag (medium WP)
presel  = 'nFatJet>0&&Sum$(FatJet_pt>200&&FatJet_deepTagMD_HbbvsQCD>0.8695)>0'
preselHighPt  = 'nFatJet>0&&Sum$(FatJet_pt>500&&FatJet_deepTagMD_HbbvsQCD>0.8695)>0'

plot_path = './FatJet_FastFull/'

## JECs and jet responses
#h_profile_JEC_full = fullSim.get1DHistoFromDraw(variableString="FatJet_pt/(FatJet_pt*(1-FatJet_rawFactor)):FatJet_pt", binning=[170, 200, 250, 300, 400, 600, 1000, 1500, 2000], binningIsExplicit=True, isProfile=True, selectionString=presel)
#h_profile_JEC_fast = fastSim.get1DHistoFromDraw(variableString="FatJet_corr_JEC:FatJet_pt_nom", binning=[170, 200, 250, 300, 400, 600, 1000, 1500, 2000], binningIsExplicit=True, isProfile=True, selectionString=presel)

#h_profile_response_b_full = fullSim.get1DHistoFromDraw(variableString="Jet_pt/GenJet_pt[Jet_genJetIdx]:Jet_pt", binning=[30,50,70,100,130, 170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&Jet_hadronFlavour==5&&Jet_genJetIdx>-1')
h_profile_response_b_full = fullSim.get1DHistoFromDraw(variableString="Jet_pt/GenJet_pt[Jet_genJetIdx]:Jet_pt", binning=[(i+1)*30 for i in range(40)], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_hadronFlavour==5&&Jet_genJetIdx>-1&&PV_ndof>4 && sqrt(PV_x*PV_x+PV_y*PV_y)<=2 && abs(PV_z)<=24')
#h_profile_response_b_fast = fastSim.get1DHistoFromDraw(variableString="Jet_pt_nom/GenJet_pt[Jet_genJetIdx]:Jet_pt_nom", binning=[30,50,70,100,130,170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&Jet_hadronFlavour==5&&Jet_genJetIdx>-1')
h_profile_response_b_fast = fastSim.get1DHistoFromDraw(variableString="Jet_pt_nom/GenJet_pt[Jet_genJetIdx]:Jet_pt_nom", binning=[(i+1)*30 for i in range(40)], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_hadronFlavour==5&&Jet_genJetIdx>-1&&PV_ndof>4 && sqrt(PV_x*PV_x+PV_y*PV_y)<=2 && abs(PV_z)<=24')

#h_profile_response_ISR_full = fullSim.get1DHistoFromDraw(variableString="Jet_pt/GenJet_pt[Jet_genJetIdx]:Jet_pt", binning=[30,50,70,100,130, 170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&!(Jet_hadronFlavour==5)&&Jet_btagDeepB<0.4941&&Jet_genJetIdx>-1')
h_profile_response_ISR_full = fullSim.get1DHistoFromDraw(variableString="Jet_pt/GenJet_pt[Jet_genJetIdx]:Jet_pt", binning=[(i+1)*30 for i in range(40)], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&!(Jet_hadronFlavour==5)&&Jet_genJetIdx>-1&&PV_ndof>4 && sqrt(PV_x*PV_x+PV_y*PV_y)<=2 && abs(PV_z)<=24')
#h_profile_response_ISR_fast = fastSim.get1DHistoFromDraw(variableString="Jet_pt_nom/GenJet_pt[Jet_genJetIdx]:Jet_pt_nom", binning=[30,50,70,100,130,170, 200, 250, 300, 400, 600, 1000], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&Jet_jetId&&!(Jet_hadronFlavour==5)&&Jet_btagDeepB<0.4941&&Jet_genJetIdx>-1')
h_profile_response_ISR_fast = fastSim.get1DHistoFromDraw(variableString="Jet_pt_nom/GenJet_pt[Jet_genJetIdx]:Jet_pt_nom", binning=[(i+1)*30 for i in range(40)], binningIsExplicit=True, isProfile=True, selectionString='Jet_pt>0&&abs(Jet_eta)<2.4&&!(Jet_hadronFlavour==5)&&Jet_genJetIdx>-1&&PV_ndof>4 && sqrt(PV_x*PV_x+PV_y*PV_y)<=2 && abs(PV_z)<=24')

## styles
#h_profile_JEC_fast.legendText = 'FastSim'
#h_profile_JEC_full.legendText = 'FullSim'
#h_profile_JEC_fast.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
#h_profile_JEC_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

h_profile_response_b_fast.legendText = 'FastSim'
h_profile_response_b_full.legendText = 'FullSim'
h_profile_response_b_fast.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
h_profile_response_b_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

h_profile_response_ISR_fast.legendText = 'FastSim'
h_profile_response_ISR_full.legendText = 'FullSim'
h_profile_response_ISR_fast.style      = styles.lineStyle(ROOT.kGreen+1,   width=2, errors=True)
h_profile_response_ISR_full.style      = styles.lineStyle(ROOT.kBlue+1,    width=2, errors=True)

#plotting.draw(
#    Plot.fromHisto(name = '2017_SingleLept_JEC_AK8', histos = [ [h_profile_JEC_fast], [h_profile_JEC_full] ], texX = "p_{T} (AK8) (GeV)", texY = "jet energy correction"),
#    plot_directory = plot_path,
#    logX = False, logY = False, sorting = False,
#    #scaling = {1:0, 2:0},
#    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim', 'yRange':(0.95,1.35)},
#)

plotting.draw(
    Plot.fromHisto(name = '2017_SingleLept_response_b', histos = [ [h_profile_response_b_fast], [h_profile_response_b_full] ], texX = "p_{T} (b-jet) (GeV)", texY = "response"),
    plot_directory = plot_path,
    logX = False, logY = False, sorting = False,
    yRange = (0.9,1.8),
    #scaling = {1:0, 2:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

plotting.draw(
    Plot.fromHisto(name = '2017_SingleLept_response_ISR', histos = [ [h_profile_response_ISR_fast], [h_profile_response_ISR_full] ], texX = "p_{T} (light jet) (GeV)", texY = "response"),
    plot_directory = plot_path,
    logX = False, logY = False, sorting = False,
    yRange = (0.9,1.8),
    #scaling = {1:0, 2:0},
    ratio = {'histos': [(0, 1)], 'texY': 'x / FullSim'},
)

