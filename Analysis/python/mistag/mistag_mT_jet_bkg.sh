#!/usr/bin/env bash

# bkg means all backgrounds are combined. As in 3. in the corresponding python script

python mistag_mT_jet_bkg.py plots/2016_mtg150_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/y2016*ngoodjets*mt_met_lepg150*lin*root
python mistag_mT_jet_bkg.py plots/2016_mtl150_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/y2016*ngoodjets*mt_met_lepl150*lin*root
											  
python mistag_mT_jet_bkg.py plots/2017_mtg150_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/y2017*ngoodjets*mt_met_lepg150*lin*root
python mistag_mT_jet_bkg.py plots/2017_mtl150_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/y2017*ngoodjets*mt_met_lepl150*lin*root
											  
python mistag_mT_jet_bkg.py plots/2018_mtg150_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/y2018*ngoodjets*mt_met_lepg150*lin*root
python mistag_mT_jet_bkg.py plots/2018_mtl150_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/y2018*ngoodjets*mt_met_lepl150*lin*root
											   