#!/usr/bin/env bash

# bkg means all backgrounds are combined. As in 4. in the corresponding python script
# mCT > 200 is encompassed in mT > 150 from mistag_mT_b_jet_bkg.py

# 0 b tags

python mistag_mCT_b_jet_bkg.py plots/2016_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2016*mctl200*b0*lin*root
	     										    
python mistag_mCT_b_jet_bkg.py plots/2017_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2017*mctl200*b0*lin*root
											    
python mistag_mCT_b_jet_bkg.py plots/2018_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2018*mctl200*b0*lin*root
											    
# 1 b tag										    
											    
python mistag_mCT_b_jet_bkg.py plots/2016_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2016*mctl200*b1*lin*root
											    
python mistag_mCT_b_jet_bkg.py plots/2017_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2017*mctl200*b1*lin*root
	     										    
python mistag_mCT_b_jet_bkg.py plots/2018_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2018*mctl200*b1*lin*root
											    
# 2 b tags										    
											    
python mistag_mCT_b_jet_bkg.py plots/2016_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2016*mctl200*b2*lin*root
	     										    
python mistag_mCT_b_jet_bkg.py plots/2017_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2017*mctl200*b2*lin*root
	     										    
python mistag_mCT_b_jet_bkg.py plots/2018_mctl200_bkg ~/CMSSW_8_0_20/src/mywh_draw/plots/mctl200plots/y2018*mctl200*b2*lin*root
