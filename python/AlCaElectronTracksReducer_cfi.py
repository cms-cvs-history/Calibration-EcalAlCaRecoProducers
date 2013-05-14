import FWCore.ParameterSet.Config as cms

alcaElectronTracksReducer = cms.EDProducer("AlCaElectronTracksReducer",
                                       electronLabel = cms.InputTag("gsfElectrons"),
                                       alcaTrackCollection = cms.string('alCaElectronTracks'),
                                       generalTracksLabel = cms.InputTag("generalTracks"),
                                       alcaTrackExtraCollection = cms.string('alCaElectronTracksExtra'),
                                       generalTracksExtraLabel = cms.InputTag("generalTracksExtra"),

                                       )


