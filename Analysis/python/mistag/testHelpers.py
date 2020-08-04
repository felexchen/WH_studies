from helpers import *

BASE_PATH = "/home/users/fechen/CMSSW_8_0_20/src/mywh_draw/plots/mistag/mT/"

PATHS = [BASE_PATH + "/FatJet_pT/SM_WH/g150/root/lin/",
         BASE_PATH + "/FatJet_pT/SM_WH/l150/root/lin/"]

if __name__ == "__main__":
    
    (options, args) = addCmdlineOptions().parse_args()
    initialize(options)
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
        mistagGraphs, mistagInclusives = generateMistags(fileGroup, titles[fileGroupCount])
        mistagLegend = generateLegend(0.5, 0.75, 0.9, 0.9, mistagGraphs, mistagInclusives)
        allMistagGraphLists.append(mistagsGraphs)
        allMistagInclusiveLists.append(mistagInclusives)
        allMistagLegends.append(mistagLegend)

    # For background scale factors. Signal will be here too, but we don't have to plot them
    allSFGraphLists = []
    allSFInclusiveLists = []
    allSFLegends = []
    allSFOutNames = []
    for fileGroupCount, fileGroup in enumerate(fileGroups):
        if not isSignalRegion(fileGroup[0]): # Any index (that exists) will work
            SFGraphs, SFInclusives, SFLegend = generateSFs(allMistagGraphsLists[fileGroupCount], titles[fileGroupCount], allMistagInclusiveLists[fileGroupCount])
            allSFGraphs.append(SFGraphs)
            allSFInclusiveLists.append(SFInclusives)
            allSFLegends.append(SFLegend)
            allSFOutNames.append(outNames[fileGroupCount] + "_SF")



    # Look at the command line arguments and figures out what files to get from what directories with option to print what is happening
    # Get and group the files from those directories with option to print what is happening
    # Generates titles for each grouping since each grouping amounts to a single canvas and plot
    # Generates png names for same reason as titles
    # generates path to save to
    
