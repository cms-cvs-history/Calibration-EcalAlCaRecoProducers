import FWCore.ParameterSet.Config as cms

#
#  run on collection of electrons to make a collection of AlCaReco electrons 
#
from Calibration.EcalAlCaRecoProducers.alCaIsolatedElectrons_cfi import *
from Calibration.EcalAlCaRecoProducers.ewkHLTFilter_cfi import *
from Calibration.EcalAlCaRecoProducers.electronFilter_cfi import *
seqALCARECOEcalCalElectronRECO = cms.Sequence(alCaIsolatedElectrons)
seqALCARECOEcalCalElectron = cms.Sequence(ewkHLTFilter*electronFilter*seqALCARECOEcalCalElectronRECO) ##HLT selection: on

#ewkHLTFilter.HLTPaths = ['HLT_IsoEle15_L1I', 'HLT_DoubleIsoEle10_L1I', 'HLT_IsoEle18_L1R', 'HLT_DoubleIsoEle12_L1R']
ewkHLTFilter.HLTPaths = ['HLT_LooseIsoEle15_LW_L1R']

