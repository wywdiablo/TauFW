from TauFW.PicoProducer.storage.Sample import MC as M
from TauFW.PicoProducer.storage.Sample import Data as D
storage  = None #"/eos/user/${USER::1}/$USER/samples/nano/$ERA/$DAS"
url      = None #"root://cms-xrd-global.cern.ch/"
filelist = None #"samples/files/2016/$SAMPLE.txt"
samples  = [
  
  # DRELL-YAN
  #M('DY','DYJetsToLL_M-10to50',
  #  "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv6-Nano25Oct2019_102X_upgrade2018_realistic_v20-v1/NANOAODSIM",
  #  store=storage,url=url,files=filelist,opts='zpt=True'),
  M('DY','DYJetsToLL_M-50',
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='zpt=True'),
  M('DY','DY1JetsToLL_M-50',
    "/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='zpt=True'),
  M('DY','DY2JetsToLL_M-50',
    "/DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='zpt=True'),
  M('DY','DY3JetsToLL_M-50',
    "/DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='zpt=True'),
  M('DY','DY4JetsToLL_M-50',
    "/DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='zpt=True'),
  M('DY','DYJetsToMuTauh_M-50',
    "/DYJetsToTauTauToMuTauh_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='zpt=True'),
  
  # TTBAR
  M('TT','TTTo2L2Nu',
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='toppt=True'),
  M('TT','TTToSemiLeptonic',
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='toppt=True'),
  M('TT','TTToHadronic',
    "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist,opts='toppt=True'),
  
  # W+JETS
  M('WJ','WJetsToLNu',
    "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('WJ','W1JetsToLNu',
    "/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('WJ','W2JetsToLNu',
    "/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('WJ','W3JetsToLNu',
    "/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('WJ','W4JetsToLNu',
    "/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  
  # SINGLE TOP
  M('ST','ST_tW_antitop',
    "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('ST','ST_tW_top',
    "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('ST','ST_t-channel_antitop',
    "/ST_t-channel_antitop_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('ST','ST_t-channel_top',
    "/ST_t-channel_top_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  
  # DIBOSON
  M('VV','WW',
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('VV','WZ',
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  M('VV','ZZ',
    "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer19UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM",
    store=storage,url=url,files=filelist),
  
  # SINGLE MUON
  D('Data','SingleMuon_Run2018A',"/SingleMuon/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
   store=storage,url=url,files=filelist,channels=["skim*",'mutau','mumu','emu']),
  D('Data','SingleMuon_Run2018B',"/SingleMuon/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'mutau','mumu','emu']),
  D('Data','SingleMuon_Run2018C',"/SingleMuon/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
   store=storage,url=url,files=filelist,channels=["skim*",'mutau','mumu','emu']),
  D('Data','SingleMuon_Run2018D',"/SingleMuon/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
   store=storage,url=url,files=filelist,channels=["skim*",'mutau','mumu','emu']),
  
  # SINGLE ELECTRON
  D('Data','EGamma_Run2018A',"/EGamma/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'etau','ee']),
  D('Data','EGamma_Run2018B',"/EGamma/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'etau','ee']),
  #D('Data','EGamma_Run2018C',"", # MISSING
  #  store=storage,url=url,files=filelist,channels=["skim*",'etau','ee']),
  D('Data','EGamma_Run2018D',"/EGamma/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'etau','ee']),
  
  # TAU
  D('Data','Tau_Run2018A',"/Tau/Run2018A-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'tautau']),
  D('Data','Tau_Run2018B',"/Tau/Run2018B-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'tautau']),
  D('Data','Tau_Run2018C',"/Tau/Run2018C-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'tautau']),
  D('Data','Tau_Run2018D',"/Tau/Run2018D-UL2018_MiniAODv1_NanoAODv2-v1/NANOAOD",
    store=storage,url=url,files=filelist,channels=["skim*",'tautau']),
  
]