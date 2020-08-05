from helpers import *

SM_WH = ""

GEN_H = ""

DEFAULT_VAR = "mT"
VAR = DEFAULT_VAR

DEFAULT_INDEP_VAR = "FatJet_pT"
INDEP_VAR = DEFAULT_INDEP_VAR

DEFAULT_THRESHOLD = "150"
THRESHOLD = DEFAULT_THRESHOLD

BASE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/" 

# Fix accomadations for mct. Cp from mt plot directory to mct subidrectories before moving to mt subdirectories
PATHS = []

BKGS_IDX = 1
SIGNAL_700_1 = 7
SIGNAL_650_300 = 8
SIGNAL_225_75 = 9
DATA_IDX = 10

IDEXS = [BKGS_IDX, SIGNAL_700_1, SIGNAL_650_300, SIGNAL_225_75, DATA_IDX]

SKIP_IDEXS = []

BINNING = array.array('d', [200,400,1000])
N_BINS = len(BINNING)-1
BINNING_FOR_TH1D = (N_BINS, BINNING)

LABELS = ['t#bar{t}, single top, ttV, W + Jets, diboson',
          'signal (700,1)',
          'signal (650,300)',
          'signal (225,75)',
          'data']

def initialize(options):
    global BASE_PATH
    print BASE_PATH
    print options.variable
    print options.plotVariable
    BASE_PATH = appendToPath(BASE_PATH, options.variable)
    BASE_PATH = appendToPath(BASE_PATH, options.plotVariable)
    if options.SMWH:
        SM_WH = "/SM_WH/"
        LABELS[0] += ', SM WH'
        BASE_PATH = appendToPath(BASE_PATH, SM_WH)
        for idxCount in range(len(IDEXS)):
            if not IDEXS[idxCount] == BKGS_IDX:
                IDEXS[idxCount] += 1
    if options.GenH:
        GEN_H = "/Gen_H/"
        BASE_PATH = appendToPath(BASE_PATH, GEN_H)
    THRESHOLD = options.threshold
    PATHS.append(appendToPath(BASE_PATH, "g" + THRESHOLD + "/root/lin"))
    PATHS.append(appendToPath(BASE_PATH, "l" + THRESHOLD + "/root/lin"))

if __name__ == "__main__":
    
    (options, args) = addCmdlineOptions().parse_args()
    print BASE_PATH
    initialize(options)
    print BASE_PATH
    allFiles = getFiles(options, PATHS, printInfo = True)
    grouping = generateGrouping(options, printInfo = True)
    fileGroups = groupFiles(allFiles, grouping, printInfo = True)
    titles = generateTitles(grouping, printInfo = True)
    outNames = generateOutNames(grouping, printInfo = True)
#    savePath = generateSavePath(options, printInfo = True)

    # For background mistag efficiencies. Signals will be here too, but we don't have to plot them
    allMistagGraphLists = []
    allMistagInclusiveLists = []
    allMistagLegends = []
    for fileGroupCount, fileGroup in enumerate(fileGroups):
        mistagGraphs, mistagInclusives = generateMistags(fileGroup, titles[fileGroupCount], IDEXS, N_BINS, BINNING_FOR_TH1D, LABELS)
        mistagLegend = generateLegend(0.5, 0.75, 0.9, 0.9, mistagGraphs, mistagInclusives, LABELS)
        allMistagGraphLists.append(mistagGraphs)
        allMistagInclusiveLists.append(mistagInclusives)
        allMistagLegends.append(mistagLegend)

    # For background scale factors. Signal will be here too, but we don't have to plot them
    allSFGraphLists = []
    allSFInclusiveLists = []
    allSFLegends = []
    allSFOutNames = []
    for fileGroupCount, fileGroup in enumerate(fileGroups):
        if not isSignalRegion(fileGroup[0]): # Any index (that exists) will work
            SFGraphs, SFInclusives = generateSFs(allMistagGraphLists[fileGroupCount], titles[fileGroupCount], allMistagInclusiveLists[fileGroupCount])
            SFLegend = generateLegend(0.5, 0.75, 0.9, 0.9, SFGraphs, SFInclusives, LABELS)
            allSFGraphLists.append(SFGraphs)
            allSFInclusiveLists.append(SFInclusives)
            allSFLegends.append(SFLegend)
            allSFOutNames.append(outNames[fileGroupCount] + "_SF")



    # Look at the command line arguments and figures out what files to get from what directories with option to print what is happening
    # Get and group the files from those directories with option to print what is happening
    # Generates titles for each grouping since each grouping amounts to a single canvas and plot
    # Generates png names for same reason as titles
    # generates path to save to
    
    # Have a print all info function
    # Add in all indices, just have a "SKIP_IDEXS" to skip them. You don't have to manually exclude them yourself (especially since you are going to use skip anyway....lol)
