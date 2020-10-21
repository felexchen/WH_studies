#!/bin/bash 
# Background mistags (2 plots)
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/FatJet_pT/SM_WH/combYearscombJetscombBkgs/high.pdf ./mistagEffs/yComb_2or3jets_mtg150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/FatJet_pT/SM_WH/combYearscombJetscombBkgs/high.png ./mistagEffs/yComb_2or3jets_mtg150.png
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/FatJet_pT/SM_WH/combYearscombJetscombBkgs/low.pdf ./mistagEffs/yComb_2or3jets_mtl150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/FatJet_pT/SM_WH/combYearscombJetscombBkgs/low.png ./mistagEffs/yComb_2or3jets_mtl150.png
# Background SFs (1 plot)
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/FatJet_pT/SM_WH/combYearscombJetscombBkgs/SFs.pdf ./mistagEffs/yComb_2or3jets_mtl150_SF.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/FatJet_pT/SM_WH/combYearscombJetscombBkgs/SFs.png ./mistagEffs/yComb_2or3jets_mtl150_SF.png
# Input yields for background mistags
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtg150_lin.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtg150_log.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtg150_lin.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtg150_log.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtg150_lin.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtg150_log.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtl150_log.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtl150_lin.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtl150_lin.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtl150_log.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtl150_lin.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs/yComb_2or3jets_0btags_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs/yComb_2or3jets_1btags_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs/yComb_2or3jets_2btags_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs/yComb_2or3jets_0btags_Higgstag_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs/yComb_2or3jets_1btags_Higgstag_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/FatJet_pT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs/yComb_2or3jets_2btags_Higgstag_mtl150_log.png

# Now for signals
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/signal_2016_low_tag_ratio.pdf ./signalTagEffs/2016_mtl150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/signal_2016_high_tag_ratio.pdf ./signalTagEffs/2016_mtg150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/signal_2017_low_tag_ratio.pdf ./signalTagEffs/2017_mtl150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/signal_2017_high_tag_ratio.pdf ./signalTagEffs/2017_mtg150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/signal_2018_low_tag_ratio.pdf ./signalTagEffs/2018_mtl150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/ANsignal/FatJet_pT/Gen_H/combJetscombBkgs/signal_2018_high_tag_ratio.pdf ./signalTagEffs/2018_mtg150.pdf

# input distributions to signals
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/lin/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/lin/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/lin/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/lin/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/lin/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/lin/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtg150_lin.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/lin/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/lin/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/lin/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/lin/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/lin/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/lin/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtl150_lin.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/log/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/log/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/log/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/log/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/log/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/root/log/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtg150_log.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/log/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/log/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/log/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/log/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/log/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/root/log/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtl150_log.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/lin/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/lin/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/lin/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/lin/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/lin/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/lin/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtg150_lin.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/lin/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/lin/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/lin/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/lin/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/lin/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/lin/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtl150_lin.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/log/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/log/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/log/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/log/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/log/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/png/log/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtg150_log.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/log/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/log/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/log/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/log/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/log/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/png/log/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtl150_log.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/lin/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/lin/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/lin/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/lin/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/lin/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/lin/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtg150_lin.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/lin/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/lin/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/lin/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/lin/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/lin/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/lin/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtl150_lin.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/log/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/log/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/log/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/log/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/log/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/g150/pdf/log/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtg150_log.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/log/y2016*ngoodjetsge*GenHF* ./signalTagEffs/2016_2or3jets_GenH_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/log/y2016*ngoodjetsge*GenHHiggs* ./signalTagEffs/2016_2or3jets_GenH_Higgstag_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/log/y2017*ngoodjetsge*GenHF* ./signalTagEffs/2017_2or3jets_GenH_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/log/y2017*ngoodjetsge*GenHHiggs* ./signalTagEffs/2017_2or3jets_GenH_Higgstag_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/log/y2018*ngoodjetsge*GenHF* ./signalTagEffs/2018_2or3jets_GenH_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/Gen_H/l150/pdf/log/y2018*ngoodjetsge*GenHHiggs* ./signalTagEffs/2018_2or3jets_GenH_Higgstag_mtl150_log.pdf

chmod +r ./signalTagEffs/*root
chmod +r ./signalTagEffs/*pdf
chmod +r ./signalTagEffs/*png
chmod +r ./mistagEffs/*root
chmod +r ./mistagEffs/*pdf
chmod +r ./mistagEffs/*png

# pie charts
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/mTpie/plots/SM_WH/combYearscombJetscombBkgs/*bkgs* ./bDistributions/
chmod +r ./bDistributions/*bkgs*

# signal effs with very loose cutsy2016__FatJet_pt0__pfmetg125_mctg200_mbbg90_mbbl150_ngoodbtags2_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_ngoodjetsge2_ngoodjetsle3_mt_met_lepl150_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/noCuts/*ratio* ./signalTagEffs_looseCuts/

# input distributions
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root ./signalTagEffs_looseCuts/2016_GenH_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root ./signalTagEffs_looseCuts/2016_GenH_Higgstag_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root ./signalTagEffs_looseCuts/2017_GenH_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root ./signalTagEffs_looseCuts/2017_GenH_Higgstag_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root ./signalTagEffs_looseCuts/2018_GenH_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.root ./signalTagEffs_looseCuts/2018_GenH_Higgstag_lin.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.pdf ./signalTagEffs_looseCuts/2016_GenH_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.pdf ./signalTagEffs_looseCuts/2016_GenH_Higgstag_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.pdf ./signalTagEffs_looseCuts/2017_GenH_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.pdf ./signalTagEffs_looseCuts/2017_GenH_Higgstag_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.pdf ./signalTagEffs_looseCuts/2018_GenH_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.pdf ./signalTagEffs_looseCuts/2018_GenH_Higgstag_lin.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.png ./signalTagEffs_looseCuts/2016_GenH_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.png ./signalTagEffs_looseCuts/2016_GenH_Higgstag_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.png ./signalTagEffs_looseCuts/2017_GenH_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.png ./signalTagEffs_looseCuts/2017_GenH_Higgstag_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.png ./signalTagEffs_looseCuts/2018_GenH_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_lin.png ./signalTagEffs_looseCuts/2018_GenH_Higgstag_lin.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.root ./signalTagEffs_looseCuts/2016_GenH_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.root ./signalTagEffs_looseCuts/2016_GenH_Higgstag_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.root ./signalTagEffs_looseCuts/2017_GenH_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.root ./signalTagEffs_looseCuts/2017_GenH_Higgstag_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.root ./signalTagEffs_looseCuts/2018_GenH_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.root ./signalTagEffs_looseCuts/2018_GenH_Higgstag_log.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.pdf ./signalTagEffs_looseCuts/2016_GenH_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.pdf ./signalTagEffs_looseCuts/2016_GenH_Higgstag_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.pdf ./signalTagEffs_looseCuts/2017_GenH_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.pdf ./signalTagEffs_looseCuts/2017_GenH_Higgstag_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.pdf ./signalTagEffs_looseCuts/2018_GenH_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.pdf ./signalTagEffs_looseCuts/2018_GenH_Higgstag_log.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.png ./signalTagEffs_looseCuts/2016_GenH_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2016__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.png ./signalTagEffs_looseCuts/2016_GenH_Higgstag_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.png ./signalTagEffs_looseCuts/2017_GenH_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2017__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.png ./signalTagEffs_looseCuts/2017_GenH_Higgstag_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHFatJet250ge1__weightxyearWeight__lumi_nonorm_log.png ./signalTagEffs_looseCuts/2018_GenH_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/ANsignal/FatJet_pT/y2018__FatJet_pt0__pfmetg125_nvetoleps1_pass_PassTrackVeto_PassTauVeto_hasNanog0_WHLeptons1_nGenHHiggsFatJet250ge1__weightxyearWeight__lumi_nonorm_log.png ./signalTagEffs_looseCuts/2018_GenH_Higgstag_log.png

chmod +r ./signalTagEffs_looseCuts/*png
chmod +r ./signalTagEffs_looseCuts/*pdf
chmod +r ./signalTagEffs_looseCuts/*root

# cutflows
cp ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*Mistag*pdf ./mistagSFcutflows/
ls ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*Mistag*pdf
cp ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*2016_lumi_3*pdf ./mistagSFcutflows/
ls -1 ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*2016_lumi_3*pdf 
cp ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*2017_lumi_4*pdf ./mistagSFcutflows/
ls -1 ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*2017_lumi_4*pdf 
cp ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*2018_lumi_6*pdf ./mistagSFcutflows/
ls -1 ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*2018_lumi_6*pdf
cp ~/CMSSW_8_0_20/src/wh_draw/*cutflow_SR*comb_lumi_*pdf ./mistagSFcutflows/

#cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2016_without_over_withMistagSF_lumi_35p9.pdf ./mistagSFcutflows/
#cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2017_without_over_withMistagSF_lumi_41p5.pdf ./mistagSFcutflows/
#cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2018_without_over_withMistagSF_lumi_60p0.pdf ./mistagSFcutflows/

cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2016_without_over_withMistagSFUp_lumi_35p9.pdf ./mistagSFcutflows/
cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2016_without_over_withMistagSFDown_lumi_35p9.pdf ./mistagSFcutflows/
cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2016_without_over_withMistagSF_lumi_35p9.pdf ./mistagSFcutflows/

cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2017_without_over_withMistagSFUp_lumi_41p5.pdf ./mistagSFcutflows/
cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2017_without_over_withMistagSFDown_lumi_41p5.pdf ./mistagSFcutflows/
cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2017_without_over_withMistagSF_lumi_41p5.pdf ./mistagSFcutflows/

cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2018_without_over_withMistagSFUp_lumi_60p0.pdf ./mistagSFcutflows/
cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2018_without_over_withMistagSFDown_lumi_60p0.pdf ./mistagSFcutflows/
cp ~/CMSSW_8_0_20/src/wh_draw/tables/cutflows/higgsMistagSF/signal_cutflow_SR_2018_without_over_withMistagSF_lumi_60p0.pdf ./mistagSFcutflows/

chmod +r ./mistagSFcutflows/*


# Background mistags (2 plots) (against mCT)
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/mCT/SM_WH/combYearscombJetscombBkgs/high.pdf ./mistagEffs_against_mCT/yComb_2or3jets_mtg150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/mCT/SM_WH/combYearscombJetscombBkgs/high.png ./mistagEffs_against_mCT/yComb_2or3jets_mtg150.png
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/mCT/SM_WH/combYearscombJetscombBkgs/low.pdf ./mistagEffs_against_mCT/yComb_2or3jets_mtl150.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/mCT/SM_WH/combYearscombJetscombBkgs/low.png ./mistagEffs_against_mCT/yComb_2or3jets_mtl150.png
# Background SFs (1 plot) (against mCT)
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/mCT/SM_WH/combYearscombJetscombBkgs/SFs.pdf ./mistagEffs_against_mCT/yComb_2or3jets_mtl150_SF.pdf
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/plots/mT/mCT/SM_WH/combYearscombJetscombBkgs/SFs.png ./mistagEffs_against_mCT/yComb_2or3jets_mtl150_SF.png
# Input yields for background mistags (against mCT)
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtg150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtg150_lin.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtg150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/root/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtg150_log.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtg150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtg150_lin.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtg150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtg150_log.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtg150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtg150_lin.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtg150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/g150/png/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtg150_log.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtl150_log.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtl150_log.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtl150_lin.root
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/root/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtl150_lin.root

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtl150_lin.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtl150_lin.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtl150_log.pdf
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/pdf/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtl150_log.pdf

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtl150_lin.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/lin/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtl150_lin.png

cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nHiggsFat*b0* ./mistagEffs_against_mCT/yComb_2or3jets_0btags_Higgstag_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nHiggsFat*b1* ./mistagEffs_against_mCT/yComb_2or3jets_1btags_Higgstag_mtl150_log.png
cp ~/CMSSW_8_0_20/src/wh_draw/plots/mistag/mT/mCT/SM_WH/l150/png/log/yComb*ngoodjetsge2*nHiggsFat*b2* ./mistagEffs_against_mCT/yComb_2or3jets_2btags_Higgstag_mtl150_log.png

chmod +r ./mistagEffs_against_mCT/*


# signal SFs
cp ~/CMSSW_10_2_9/src/WH_studies/Analysis/python/mistag/signalSFs/* ./signalSFs/

chmod +r ./signalSFs/*